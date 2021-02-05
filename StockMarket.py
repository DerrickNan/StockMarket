#! /usr/local/bin/python3.9

import os
import sys
import getopt
import pandas as pd
import tushare as ts
import datetime

if __name__ == "__main__":

    stock = ts.get_today_all()
    stock['date'] = datetime.date.today()
    stock.to_csv('stock_data.csv',encoding = 'utf-8',index=None)

    stock_data = pd.read_csv('stock_data.csv',sep=',')
    df = pd.concat([stock,stock_data])
    df.to_csv('stock_data.csv',encoding = 'utf-8',index=None)
