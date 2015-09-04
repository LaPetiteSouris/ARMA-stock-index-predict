__author__ = 'tung'

from fetch_data import data
from arma_model import ARMA
from save_prediction import Storage
import datetime as date
import matplotlib.pyplot as plt
import statsmodels.api as sm


# first, loading historical index point from Yahoo Finance
data_loader = data()
current_date = date.datetime.now().date()
data = data_loader.load_yahoo_finance_data(current_date)
fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)

array_data_without_index = data_loader.convert_data_to_array(data)
data.plot(ax=ax1, title='EURONEXT 100')


# Start Modelling Process
arma_modeling_helper = ARMA(array_data_without_index)
arma_model = arma_modeling_helper.start_modeling()
resid = arma_model.resid
ax2=fig.add_subplot(212)
sm.qqplot(resid, line='q',ax=ax2, fit='True')


# Prediction
predicted_stock = arma_modeling_helper.prediction(arma_model)
print predicted_stock

#Save to database for comparision
predicted_stock_next_day=predicted_stock[0]
storage_worker=Storage()
storage_worker.save_to_pickle(predicted_stock_next_day)


plt.grid()
plt.show()
