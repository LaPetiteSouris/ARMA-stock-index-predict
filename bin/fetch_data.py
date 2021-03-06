__author__ = 'tung'

import datetime as date
import pandas.io.data as web


class data:
    # Load training data from Yahoo finance API. This data contains closing point of N100 index in year of 2015
    def load_yahoo_finance_data(self, end_date):
        start = date.datetime(2000, 1, 1)
        result = web.DataReader('^N100', 'yahoo', start, end_date)
        # Adj closing point of the index
        cls_point = result.loc[:, ['Adj Close']]
        return cls_point

    def convert_data_to_array(self, data):
        length = len(data.index)
        data_value_array = []
        for i in range(0, length - 1):
            data_val=data.iloc[i].values[0]
            data_value_array.append(data_val)
        return data_value_array
