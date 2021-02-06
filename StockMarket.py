#! /usr/local/bin/python3.9

import os
import sys
import getopt
import pandas as pd
import tushare as ts
import datetime

tushare_token = '2dcc4c37955662e3e70506934cba9e021f8ebb918ffa08307098ab3d'

ingenic_stock_code = '300223.SZ'

# Tushare infterface
#
# Main Parameters :
#
#     exchange    : SSE  ( Shang Hai Stock )
#                   SZSE ( Shen Zhen Stock )
#                   HKSE ( Xiang Gang Stock : reserved )
#
#     ts_code     : stock code
#
#     list_status : L ( list )
#                   D ( delist )
#                   P ( Suspend list )
#
#     is_hs       : h ( Shang Hai Tong )
#                   s ( Shen Zhen Tong )
#
# Main functions :
#
#    stock_basic   : get real-time stock quotes
#    stock_company : get stock company information
#    

class tushare_if :
    'tushare interface'
    def __init__ ( self ) :
        ts.set_token( tushare_token )
        self.pro = ts.pro_api()

    def get_basic_info ( self, stock_code = '' ) :
        data = self.pro.stock_basic( exchange = '', ts_code = stock_code, list_status = 'L',
                                     fields = 'ts_code,symbol,name,area,industry,list_date' )
        print ( data )

    def get_company_info ( self, stock_code = '' ) :
        data = self.pro.stock_company( exchange = 'SZSE', ts_code = stock_code,
                                       fields = 'ts_code,chairman,manager,secretary,reg_capital,setup_date,province' )
        print ( data )

    def get_stock_daily ( self, stock_code = '' ) :
        data = self.pro.daily( ts_code = stock_code, start_date='20180701', end_date='20210205' )
        print ( data )

    def get_stock_weekly ( self, stock_code = '' ) :
        data = self.pro.weekly( ts_code = stock_code, start_date='20180701', end_date='20210205' )
        print ( data )

    def get_stock_monthly ( self, stock_code = '' ) :
        data = self.pro.monthly( ts_code = stock_code, start_date='20180701', end_date='20210205' )
        print ( data )

    def get_new_share ( self ) :
        data = self.pro.new_share( start_date='20180901', end_date='20181018' )
        print ( data )

if __name__ == "__main__":

    tsif = tushare_if()
    tsif.get_basic_info( ingenic_stock_code )
    tsif.get_company_info( ingenic_stock_code )
    tsif.get_stock_daily( ingenic_stock_code )
    tsif.get_stock_weekly( ingenic_stock_code )
    tsif.get_stock_monthly( ingenic_stock_code )
    tsif.get_new_share()
