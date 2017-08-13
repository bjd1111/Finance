
# coding: utf-8

# # import packages

# In[320]:



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


# # functions to get stock return data

# In[321]:

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





# # portfolio data

# In[322]:

# portfolio securities:

ticker = 'ibm'
start_date = dt.datetime(2016,1,1) 
end_date = dt.datetime(2016,12,31)
ibmdf = get_stock_rtn(start_date,end_date,ticker)


# hedge securities:

ticker = 'spy'
spydf = get_stock_rtn(start_date,end_date,ticker)




# In[ ]:




# # return - min var hedge ratio

# In[323]:

from scipy.optimize import minimize
def min_var(c):
    return np.var((ibmdf + c*spydf)['return'])
min_var(-1)


# # min var = 0.000096

# In[324]:

res = minimize(min_var, 1,
                method='nelder-mead', options={'xtol':1e-8,'disp': True})


# # hedge ratio = -0.92992296

# In[325]:

res.x


# In[326]:

plt.plot([min_var(i) for i in np.linspace(-2,1,100) ])


# # s-s0  difference

# In[327]:


start_date = dt.datetime(2016,1,1) 
end_date = dt.datetime(2016,12,31)


ibmp = pd.DataFrame(data.DataReader('ibm','google',start=start_date,end=end_date)['Close'])
ibmpc = (ibmp-ibmp.shift(1)).dropna()


spyp = pd.DataFrame(data.DataReader('spy','google',start=start_date,end=end_date)['Close'])
spypc = (spyp-spyp.shift(1)).dropna()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:





# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



