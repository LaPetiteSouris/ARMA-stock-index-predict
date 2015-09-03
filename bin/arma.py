__author__ = 'tung'

from fetch_data import  data
import matplotlib.pyplot as plt
data_loader=data()
#first, loading historical index point from Yahoo Finance
euronext_index_training=data_loader.load_yahoo_finance_data()
print euronext_index_training
euronext_index_training.plot(y='Adj Close')
legend=plt.legend()
legend.get_texts()[0].set_text('EURONEXT 100-Closing price')
plt.show()


