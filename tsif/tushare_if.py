# !/usr/bin/env python

################################################################################
#                   (C) COPYRIGHT Derrick Limited.
#
# File Name   : tushare_if.py
# Author      : Derrick Nan
# Email       : 563001383@qq.com
# Created     : 2021-05-07 15:33:17 (CST)
# Description : Tushare infterface
#
#               Main Parameters :
#
#                   exchange    : SSE  ( Shang Hai Stock )
#                                 SZSE ( Shen Zhen Stock )
#                                 HKSE ( Xiang Gang Stock : reserved )
#
#                   ts_code     : stock code
#
#                   list_status : L ( list )
#                                 D ( delist )
#                                 P ( Suspend list )
#
#                   is_hs       : h ( Shang Hai Tong )
#                                 s ( Shen Zhen Tong )
#
#               Main functions :
#
#                   stock_basic   : get real-time stock quotes
#                   stock_company : get stock company information
#    
################################################################################

import os
import sys
import pandas as pd
import tushare as ts

tushare_token = '2dcc4c37955662e3e70506934cba9e021f8ebb918ffa08307098ab3d'

class tushare_if :
    'tushare interface'
    def __init__ ( self ) :

        ts.set_token( tushare_token )

        self.pro = ts.pro_api()
        self.start_date = ''
        self.end_data   = ''

    def set_time( self, start_time, end_time ) :

        self.start_date = start_time
        self.end_date   = end_time

    def get_basic_info ( self, stock_code = '', fields = '' ) :

        field_list = 'ts_code,symbol,name,area,industry,list_date' if fields == '' else fields

        if stock_code == '' :
            return self.pro.stock_basic( exchange = '', list_status = 'L', fields = field_list )
        else :
            return self.pro.stock_basic( exchange = '', ts_code = stock_code, list_status = 'L', fields = field_list )

    def get_company_info ( self, stock_code = '', fields = '' ) :

        field_list = 'ts_code,chairman,manager,secretary,reg_capital,setup_date,province' if fields == '' else fields

        if stock_code == '' :
            return self.pro.stock_company( exchange = 'SZSE', fields = field_list )
        else :
            return self.pro.stock_company( exchange = 'SZSE', ts_code = stock_code, fields = field_list )

    def get_new_share ( self ) :

        return self.pro.new_share( start_date = self.start_date, end_date = self.end_date )

    def get_stock_quotes ( self, stock_code = '', period_type = 'daily' ) :

        if period_type == 'weekly' :
            return self.pro.weekly( ts_code = stock_code, start_date = self.start_date, end_date = self.end_date )

        if period_type == 'monthly' :
            return self.pro.monthly( ts_code = stock_code, start_date = self.start_date, end_date = self.end_date )

        return self.pro.daily( ts_code = stock_code, start_date = self.start_date, end_date = self.end_date )

    def get_stock_moneyflow( self, stock_code = '', start_date = '', end_date = '' ) :

        if start_date == '' or end_date == '' :
            return self.pro.moneyflow( ts_code = stock_code, start_date = self.start_date, end_date = self.end_date )
        else :
            return self.pro.moneyflow( ts_code = stock_code, start_date = start_date, end_date = end_date )
