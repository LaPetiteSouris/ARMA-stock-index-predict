__author__ = 'tung'

from fetch_data import data
from arma_model import ARMA
import datetime as date
import matplotlib.pyplot as plt
# first, loading historical index point from Yahoo Finance
data_loader = data()
current_date = date.datetime.now().date()
data = data_loader.load_yahoo_finance_data(current_date)
arma_modeling = ARMA(data)
# This is the optimal ARMA model (which has smallest AIC)
arma_optimal_model = arma_modeling.start_modeling()
print 'AIC of optimal ARMA Model is: '
print arma_optimal_model.aic

# Plot
data.plot(y='Adj Close')
legend = plt.legend()
legend.get_texts()[0].set_text('EURONEXT 100-Closing price')
plt.grid()
plt.show()
