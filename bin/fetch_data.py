__author__ = 'tung'

import datetime as date
import pandas.io.data as web


class data:
    # Load training data from Yahoo finance API. This data contains closing point of N100 index in year of 2015
    def load_yahoo_finance_data(self):
        start = date.datetime(2015, 8, 15)
        end = date.datetime(2015, 8, 31)
        result = web.DataReader('^N100', 'yahoo', start, end)
        # Adj closing point of the index
        cls_point = result.loc[:, ['Adj Close']]
        return cls_point
