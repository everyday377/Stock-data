# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 22:47:36 2020
This will be used to capture data from Yahoofinance.com, 
the captured data will be used to predict future stock price.
@author: 12259
"""

import datetime
import urllib.request, urllib.error, urllib.parse
from os import path
import numpy as np
import csv


def setupDateURL(urlBase):
    fromdate=int(datetime.datetime(2010, 1, 1, 0, 0, 0).timestamp()) 
    #(year,month,date,hour,minite,second)
    todate=int(datetime.datetime(2011, 1, 1, 0, 0, 0).timestamp())
    interval='1d' 
    #'1wk' represents 1 week Interval; '1mo' represents 1 month Interval; '1d' represents 1 day Interval
    return urlBase.replace('__Fromdate__',str(fromdate))\
                    .replace('__Todate__',str(todate))\
                    .replace('__Interval__',interval)\

def fetchCSV(fileName, url):
    #if file already downloaded, then open the local file
    if path.isfile(fileName):
        print(('fetch CSV from local: ' + fileName))
        with open(fileName,newline='') as csvfile:
            f=csv.DictReader(csvfile)
            l = [row for row in f]
        return l
    # if not downloaded, then download the file from the url
    else:
        print(('fetch CSV from url: ' + url))
        csvurlfile = urllib.request.urlopen(url).read()
        with open(fileName, 'wb') as csvfile:
            csvfile.write(csvurlfile)
        with open(fileName,newline='') as csvfile:
            f=csv.DictReader(csvfile)
            l = [row for row in f]
        return l


def fetchYahooFinance(name):
    #name is the ID of stock, should be string type.
    fileName = 'index_%s.csv' % name
    url = setupDateURL('https://query1.finance.yahoo.com/v7/finance/download/%s?period1=__Fromdate__&period2=__Todate__&interval=__Interval__&events=history' % name)
    csvfile = fetchCSV(fileName, url)
    return csvfile
    
