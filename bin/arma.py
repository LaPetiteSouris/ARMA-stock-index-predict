__author__ = 'tung'

from fetch_data import  data
data_loader=data()
#first, loading historical index point from Yahoo Finance
euronext_index_training=data_loader.load_yahoo_finance_data()
print euronext_index_training
