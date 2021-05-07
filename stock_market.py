#! /usr/local/bin/python3.9

################################################################################
#                   (C) COPYRIGHT Derrick Limited.
#
# File Name   : stock_market.py
# Author      : Derrick Nan
# Email       : 563001383@qq.com
# Created     : 2021-05-07 16:32:17 (CST)
# Description : 
################################################################################

import os
import sys
import getopt
import time

from tsif.tushare_if import tushare_if

ingenic_stock_code = '300223.SZ'

class stock_if :
    def __init__ ( self ) :
        self.tsif = tushare_if()
        self.tsif.set_time( '%d' % ( int( time.strftime('%Y%m%d') ) - 10000 ), time.strftime('%Y%m%d') )

        self.stock_list = []

    def get_stock_list ( self ) :
        data = self.tsif.get_basic_info()
        for index, row in data.iterrows() :
            self.stock_list.append( row['ts_code'] )

if __name__ == "__main__":

    stif = stock_if()
    stif.get_stock_list()
    print ( stif.tsif.get_stock_moneyflow( ingenic_stock_code ) )
