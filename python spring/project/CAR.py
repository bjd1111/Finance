import pandas_datareader.data as pdr
import pandas as pd
import numpy as np
import datetime, os, csv
import statsmodels.api as sm



os.chdir( "C:/Users/bjd/git/Finance/python spring/project")



input_path10K1A = "10-K1A.csv"
csvFile10K1A = open(input_path10K1A, "r")
csvReader10K1A = csv.reader(csvFile10K1A, delimiter=",")
csvData10K1A = list(csvReader10K1A)



input_path = "CompanyTickerList.csv"
csvFile = open(input_path, "r")
csvReader = csv.reader(csvFile, delimiter=",")
csvData = list(csvReader)


start = datetime.datetime(2006, 1, 1) #<==change start time here
end = datetime.datetime(2017, 1, 1) #<==change end time here

# Read-in data for SPY
spy = pdr.DataReader("SPY", 'yahoo', start, end)
spy_adj = spy['Adj Close']
spy_ret = np.log(spy_adj).diff().dropna()

## Read-in data for stocks
stocks = []
for rowData in csvData[1:]:
    ticker = rowData[0]
    stocks.append(ticker)
price = pdr.DataReader(stocks, 'yahoo', start, end)
key_word = 'Adj Close'
cleanData = price.ix[key_word]
adj_close = pd.DataFrame(cleanData)
ret = np.log(adj_close).diff().dropna()
rows = ret.shape[0]

headers = sorted(stocks)




for i in range(1): # <===N=20 securities in this portfolio. Change this to fit the size of your portfolio
    stock = ret.ix[:, i]
    stock_name = headers[i]
    spy_ret = sm.add_constant(spy_ret)
    model = sm.OLS(stock, spy_ret).fit()
    ret[stock_name] = model.resid #<===dataframe of residual

car = []
for rowData in csvData10K1A[1:]:
    ticker = rowData[0]
    filingdate = rowData[2]
    positive_pct = rowData[5]
    negative_pct = rowData[7]

    try:
        tic_index = headers.index(ticker)
    except ValueError:
        print "ticker not in list."
    residual = ret.ix[:, tic_index]
    date_index = residual.index.get_loc(filingdate)
    x = 3 #<==analayze 3 days before and 3 days after the report date.
    date_start = date_index - x
    for i in range(1, 2+2*x):
        row = [sum(residual[date_start: date_start + i]), positive_pct, negative_pct]
        car.append(row)

df = pd.DataFrame(car, columns=['CAR', 'positive_pct', 'negative_pct'])

Y = df['CAR']
X = df[['positive_pct', 'negative_pct']]
X = sm.add_constant(X)
reg = sm.OLS(Y, X.astype(float)).fit()
print reg.summary()