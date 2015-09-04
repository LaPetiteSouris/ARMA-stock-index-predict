__author__ = 'tung'

import statsmodels.api as sm



class ARMA:
    def __init__(self, data):
        self._data = data

    def start_modeling(self):
        best_arma_order = self.find_optimal_model_order()
        arma_model = self.fit_models(best_arma_order)
        print 'Optimal ARMA order(p,q) is: '
        print best_arma_order
        return arma_model

    # fit data into an ARMA model with order (p,q)

    def fit_models(self, res):
        arma = sm.tsa.ARMA(self._data, res).fit(disp=0)
        return arma

    # Return the optimal ARMA model based on finding min of AIC
    def find_optimal_model_order(self):
        p = 5
        q = 5
        residual = sm.tsa.stattools.arma_order_select_ic(self._data, p, q, ic='aic', trend='nc')
        return residual.aic_min_order

    # Predict stock index in the next 3 days
    def prediction(self, arma_model):
        lenght_data = len(self._data)
        predicted_stock = arma_model.predict(lenght_data, lenght_data+4, dynamic="True")
        return predicted_stock
