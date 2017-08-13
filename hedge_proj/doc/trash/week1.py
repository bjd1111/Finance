# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 18:47:36 2017

@author: ky
"""


import datetime as dt
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.special import beta
from scipy.optimize import minimize
from scipy.stats import skewnorm
from pandas_datareader import data, wb


# think of making this a class, so only have to compute weights once 


def bod_const(n,q):
    return 1/(n-q+(q*q-1.)/(3.*n))

def bod_est(y,n,q):
    '''
    '''
    c = (n-q+(q*q-1.)/(3*n))
    return c*np.sum((y-np.mean(y))**2)

def get_stock_rtn(start_date,end_date,ticker):
    '''
    ticker: 'SPY'
    start_date: dt.datetime(2011,1,4) 
    end_date: dt.datetime(2017,5,1)
    '''
    price_df = data.DataReader(ticker,'google',start=start_date,end=end_date)['Close']
    rtndf = pd.DataFrame(price_df.pct_change().dropna())
    return rtndf
def c1_const(q,w):
    '''
    n - total number of overlapping returns
    q - overlap window size
    w - vector of weights (1 by n)
    ## CHECK ALL LENGTHS OF THE TERMS ARE CORRECT
    '''
    n = len(w)

    indlst = range(0,n+q-1)
    indlst1 = indlst[0:q-1]
    indlst2 = indlst[q-1:n]
    indlst3 = indlst[n::]
    
    #[np.sum(w[0:i+1])**2 for i in xrange(0,q-1)]
    t1 = np.sum(np.array([np.sum(w[0:i+1])**2 for i in indlst1]))
    t2 = np.sum(np.array([np.sum(w[i-q+1:i+1])**2 for i in indlst2]))
    t3 = np.sum(np.array([np.sum(w[(i-q+1):n+1])**2 for i in indlst3])) # finish

    return 1. - 1./float(q)*(t1+t2+t3)

def wgt_var(y,w,q):
    ybar = np.dot(w,y)
    tmpsum = np.dot(w,(y - ybar)**2)
    return tmpsum/c1_const(q,w)

def c2_const(q,w):
    '''
    '''
    n = len(w)
    tmpsum = 0
    for i in xrange(1,n):
        for j in xrange(1,n):
            if abs(i-j) < q:
                tmpsum = tmpsum + w[i-1]*w[j-1]*(q-abs(i-j))

    t0 = 3/q*tmpsum

    indlst = range(0,n+q-1)
    indlst1 = indlst[0:q-1]
    indlst2 = indlst[q-1:n]
    indlst3 = indlst[n::]

    t1 = np.sum(np.array([np.sum(w[0:i+1])**3 for i in indlst1]))
    t2 = np.sum(np.array([np.sum(w[i-q+1:i+1])**3 for i in indlst2]))
    t3 = np.sum(np.array([np.sum(w[(i-q+1):n+1])**3 for i in indlst3])) # finish

    return 1 - t0 + 2./q*(t1+t2+t3)

def wgt_skewness(y,w,q): 
    '''
    '''
    ybar = np.dot(w,y)
    tmpsum = np.dot(w,(y - ybar)**3)
    return tmpsum/c2_const(q,w)

def skew_t_dist_std(t,a,b):
    '''
    '''
    const = 2.**(a+b-1)*beta(a,b)*np.sqrt(a+b)
    fact1 = (1.+t/(a+b+t*t)**0.5)**(a+0.5)
    fact2 = (1.-t/(a+b+t*t)**0.5)**(b+0.5)
    return 1/const*fact1*fact2

def skew_t_dist_likli(x,mu,sig,a,b):
    '''
    '''
    n = len(x)
    
    sm = np.sum(np.log(1+(x-mu)/((a+b)*sig*sig+(x-mu)**2)))
    return -n*sig - n*beta(a,b) + (a+b+1.)*sm

def sknormal_skewness_stats(a,b,c):
    '''
    first three moments of a skewness dist
    '''
    d = c/np.sqrt(1+c*c)

    mean = a + b*d*np.sqrt(2./np.pi)
    var = b*b*(1-2*d*d/np.pi)

    fact1 = (4-np.pi)/2.
    fact2 = (d*np.sqrt(2/np.pi))**3
    fact3 = 1/(1-2*d*d/np.pi)**(1.5)
    skewness = fact1*fact2*fact3

    return (mean,var,skewness)

if __name__ == "__main__":



# Download return, mean, variance and skew of ibm and spy 
    ticker = 'ibm'
    start_date = dt.datetime(2016,1,1) 
    end_date = dt.datetime(2016,12,31)
    ibmdf = get_stock_rtn(start_date,end_date,ticker)


    ticker = 'spy'
    spydf = get_stock_rtn(start_date,end_date,ticker)
    
    
    # Single simulation first to test performance of estimators 
    five_year_spy_df = get_stock_rtn(dt.datetime(2016,1,1),dt.datetime(2017,05,31),'SPY')
    fit_param = skewnorm.fit(five_year_spy_df)
    mn1,var1,skew1 = sknormal_skewness_stats(fit_param[1],fit_param[2],fit_param[0])
    
    # Single simulation first to test performance of estimators 
    five_year_ibm_df = get_stock_rtn(dt.datetime(2016,1,1),dt.datetime(2016,12,31),'ibm')
    fit_param = skewnorm.fit(five_year_ibm_df)
    mn2,var2,skew2 = sknormal_skewness_stats(fit_param[1],fit_param[2],fit_param[0])

# calculate h*

import math
stdspy=math.sqrt(var1)
stdibm=math.sqrt(var2)
      
covariance=np.cov(spydf['Close'],ibmdf['Close'])[0][1]
correlation=covariance/(stdspy*stdibm)
hstar=correlation*(stdibm/stdspy)


# construction of hedged portfolio and calculation of return

price_ibm = data.DataReader('ibm','google',start=start_date,end=end_date)['Close']
price_spy = data.DataReader('spy','google',start=start_date,end=end_date)['Close']
price_portfolio=price_ibm-hstar*price_spy

rtnibm = pd.DataFrame(price_ibm.pct_change().dropna())
rtnport = pd.DataFrame(price_portfolio.pct_change().dropna())

rtnibm.plot()
rtnport.plot()
# performance metrics of ibm and hedged portfolio

rf=0.024
from scipy.stats import norm


#ibm

returns=rtnibm
mu = np.mean(returns)
std = np.std(returns)
valueAtRisk_ibm = norm.ppf(0.05, mu, std)

volatility_ibm=returns.std()*np.sqrt(252)

sharpe_ratio_ibm = (returns.mean() - rf) / volatility_ibm

covariance1=np.cov(price_spy,price_ibm)[0][1]
variance1=np.var(price_spy)
beta_ibm=covariance1/variance1


Roll_Max = pd.rolling_max(price_spy, 252, min_periods=1)
Daily_Drawdown = price_spy/Roll_Max - 1.0
Max_Daily_Drawdown = pd.rolling_min(Daily_Drawdown, 252, min_periods=1)
Daily_Drawdown.plot()
Max_Daily_Drawdown.plot()


#portfolio
returns=rtnport
mu = np.mean(returns)
std = np.std(returns)
valueAtRisk_portfolio = norm.ppf(0.05, mu, std)

volatility_portfolio=returns.std()*np.sqrt(252)

sharpe_ratio_portfolio = (returns.mean() - rf) / volatility_portfolio

covariance2=np.cov(price_spy,price_portfolio)[0][1]
variance1=np.var(price_spy)
beta_portfolio=covariance2/variance1

Roll_Max = pd.rolling_max(price_portfolio, 252, min_periods=1)
Daily_Drawdown = price_portfolio/Roll_Max - 1.0
Max_Daily_Drawdown = pd.rolling_min(Daily_Drawdown, 252, min_periods=1)
Daily_Drawdown.plot()
Max_Daily_Drawdown.plot()

#Conclusion: Due to the right timing