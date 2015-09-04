__author__ = 'tung'

from fetch_data import data
from arma_model import ARMA
import datetime as date
import matplotlib.pyplot as plt



# first, loading historical index point from Yahoo Finance
data_loader = data()
current_date = date.datetime.now().date()
data = data_loader.load_yahoo_finance_data(current_date)

#Start modeling data using ARMA with optimal order
arma_modeling_helper=ARMA(data)
optimal_order_ARMA=arma_modeling_helper.start_modeling()



predict_stock=optimal_order_ARMA.predict('2015-09-07', '2015-09-10', dynamic="True")
data.plot(y='Adj Close')
legend = plt.legend()
legend.get_texts()[0].set_text('EURONEXT 100-Closing price')
print predict_stock
plt.plot(predict_stock)
plt.grid()
plt.show()
'''

# Plot
data.plot(y='Adj Close')
legend = plt.legend()
legend.get_texts()[0].set_text('EURONEXT 100-Closing price')
plt.grid()
plt.show()
'''