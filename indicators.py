
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

# All calculations for technical indicators are based off of the calculation provided by Investopedia.
# https://www.investopedia.com

def ma(data, period, col = "Adj Close", **kwarg):
    '''Function to calculate a moving average for timeseries data.
    Takes a Pandas dataframe object with date as index and ticker close data
    and concatenates a new column with the moving average. '''
    if 'colname' in kwarg:
        colname = kwarg['colname']
    else:
        colname = "MA{}".format(period)
    data[colname] = data[col].rolling(window = period).mean()
    return data

def bb(data, period = 20, stdmult = 2, col = "Adj Close"):
    '''Function to calculates bollinger bands for timeseries data.
    Takes a Pandas dataframe object with date as index and ticker close data
    and concatenates new columns with the lower band, upper band, and moving avg. '''
    std = data[col].rolling(window = period).std()
    data['BB MA{}'.format(period)] = data[col].rolling(window = period).mean()
    for (mult,band) in [(-1*stdmult, "Lower"), (stdmult, "Upper")]:
        data['BB {}'.format(band)] = data['BB MA{}'.format(period)] + mult * std
    return data

def ema(data, period, col = "Adj Close", **kwarg):
    '''Function to calculate a moving average for timeseries data.
    Takes a Pandas dataframe object with date as index and ticker close data
    and concatenates a new column with the exponential moving average. '''
    if 'colname' in kwarg:
        colname = kwarg['colname']
    else:
        colname = "EMA{}".format(period)
    alpha = 2 / (period + 1)
    data[colname] = data[col].ewm(alpha = alpha).mean()
    return data

def macd(data, col = "Adj Close"):
    '''Function to calculate the moving average convergence divergence indicator.
    Takes a Pandas dataframe object with date as index and ticker close data and 
    concatenates new columns with EMA12, EMA26, MACD, MACD signal line, and MACD 
    Histrogram data. '''
    data = ema(data, 12)
    data = ema(data, 26)
    data['MACD'] = data['EMA12'] - data['EMA26']
    data = ema(data, 9, col = "MACD", colname = "MACD Sig")
    data['MACD Hist'] = data['MACD'] - data['MACD Sig']
    return data

def rsi(data, period):
    '''Function to calculates the relative strength index for timeseries data.
    Takes a Pandas dataframe object with date as index and ticker close data
    and concatenates a new column with the relative strength. '''
    pass


if __name__ == "__main__":
    plt.style.use('seaborn')
    data = web.DataReader('AAPL','yahoo', start = '2018-02-01', end = '2019-02-01')
    print(data.tail())

 

