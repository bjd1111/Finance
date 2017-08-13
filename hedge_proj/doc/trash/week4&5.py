# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 13:07:23 2017

@author: ky
"""

import datetime as dt
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
import seaborn as sns
from scipy.special import beta
from scipy.optimize import minimize
from scipy.stats import skewnorm
from pandas_datareader import data, wb



import matplotlib
matplotlib.style.use('ggplot')


def get_stock_rtn(start_date,end_date,ticker):
    '''
    ticker: 'SPY'
    start_date: dt.datetime(2011,1,4) 
    end_date: dt.datetime(2017,5,1)
    '''
    price_df = data.DataReader(ticker,'google',start=start_date,end=end_date)['Close']
    rtndf = pd.DataFrame(price_df.pct_change().dropna())
    rtndf.columns = ['return']
    return rtndf




start_date = dt.datetime(2016,1,1) 
end_date = dt.datetime(2016,12,31)
ticker = ('jpm')
price_jpm = data.DataReader(ticker,'google',start=start_date,end=end_date)['Close']
rtn_jpm= pd.DataFrame(price_jpm.pct_change().dropna())

ticker = ('spy')
price_spy = data.DataReader(ticker,'google',start=start_date,end=end_date)['Close']
rtn_spy = pd.DataFrame(price_spy.pct_change().dropna())

ticker = ('iyf')
price_iyf = data.DataReader(ticker,'google',start=start_date,end=end_date)['Close']
rtn_iyf = pd.DataFrame(price_iyf.pct_change().dropna())

ticker = ('csj')
price_csj = data.DataReader(ticker,'google',start=start_date,end=end_date)['Close']
rtn_csj = pd.DataFrame(price_csj.pct_change().dropna())

def min_var(h):
    return np.var((r_jpm+h[0]*r_spy+h[1]*r_iyf+h[2]*r_csj))

a=[]
for i in range (0,5):
    r_jpm=rtn_jpm[i:i+5]
    r_spy=rtn_spy[i:i+5]
    r_iyf=rtn_iyf[i:i+5]
    r_csj=rtn_csj[i:i+5]
    res = minimize(min_var,[0,0,0],method='nelder-mead', options={'xtol':1e-8,'disp': True})
    a.append(res.x)
    i=i+1
    
b=pd.DataFrame(a,columns=['spy','iyf','csj'])

b.plot()





