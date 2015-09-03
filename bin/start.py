__author__ = 'tung'

from fetch_data import data
from arma_model import ARMA
import datetime as date
import matplotlib.pyplot as plt



# first, loading historical index point from Yahoo Finance
data_loader = data()
current_date = date.datetime.now().date()
data = data_loader.load_yahoo_finance_data(current_date)
arma_modeling_helper=ARMA(data)
optimal_order_ARMA=arma_modeling_helper.start_modeling()

'''

# Plot
data.plot(y='Adj Close')
legend = plt.legend()
legend.get_texts()[0].set_text('EURONEXT 100-Closing price')
plt.grid()
plt.show()
'''