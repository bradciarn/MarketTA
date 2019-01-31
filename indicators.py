
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

# All calculations for technical indicators are based off of the calculation provided by Investopedia.
# https://www.investopedia.com

def ma(data, period, col = "Adj Close"):
    '''Function to calculate a moving average for timeseries data.
    Takes a Pandas dataframe object with date as index and ticker close data
    and concatenates a new column with the moving average. '''
    data['MA{}'.format(period)] = data[col].rolling(window = period).mean()
    return data

def bb(data, period):
    '''Function to calculates bollinger bands for timeseries data.
    Takes a Pandas dataframe object with date as index and ticker close data
    and concatenates new columns with the lower band, upper band, and moving avg. '''
    pass

def rsi(data, period):
    '''Function to calculates the relative strength index for timeseries data.
    Takes a Pandas dataframe object with date as index and ticker close data
    and concatenates a new column with the relative strength. '''
    pass


if __name__ == "__main__":
    plt.style.use('ggplot')
    data = web.DataReader('AAPL','yahoo', start = '2018-01-01', end = '2019-01-01')
    data = ma(data,20)
    print(data.tail())
    data['Adj Close'].plot()
    data['MA20'].plot()
    plt.show()
 

