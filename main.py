from datetime import date, timedelta
import datetime
import pandas as pd
import quandl
import json
from math import log10, floor

import matplotlib.pyplot as plt

import numpy as np

close = np.random.random(100)

#setup for debug
import logging
logging.basicConfig(level=logging.INFO)

API = "z3xWGdrRdxGC1sFtyimA"

df_reframe = []
today = np.datetime64('today','D')

global df_reframe
global stock_num
global df
stock_num = "00700"
period_vector = 52*2
end_date = today-np.timedelta64(1,'D')
start_date = today - np.timedelta64(period_vector,'W')
df = quandl.get("HKEX/"+stock_num, start_date=start_date, end_date=end_date, authtoken=API)#HSI:BCIW/_HSI
df_reset = df.reset_index()
df_reframe = pd.DataFrame(df_reset, columns=['Date', 'High','Low', 'Share Volume (000)','Previous Close'])
df_reframe = df_reframe.dropna(how='any')
df_reframe = df_reframe.to_records(index=False)

# plotting the points   
plt.plot(df_reframe['Date'], rsiPrice)  
    
# naming the x axis  
plt.ylabel('Price')  
 
# giving a title to my graph  
plt.title('Stock Price of 00700')  
    
# function to show the plot  
plt.show() 
