import pandas as pds
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime as dt
#By using these libraries I am able to obtain data on any 
#ticker symbol, and all the information that I could need

plt.style.use('seaborn')

AAPL = yf.Ticker('AAPL')
stockinfo = AAPL.info

for key,value in stockinfo.items():
           print(key,":", value)

print(AAPL.recommendations)
print(AAPL.splits)

df = AAPL.dividends
data = df.resample('Y').sum()
data = data.reset_index()
data['Year'] = data['Date'].dt.year

plt.figure()
plt.bar(data['Year'], data['Dividends'])
plt.ylabel('Dividend Yield')
plt.xlabel('Year')
plt.title('Apple Dividend')
plt.xlim(2010, 2022)
plt.show()