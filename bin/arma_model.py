__author__ = 'tung'

import statsmodels.api as sm
import numpy as np


class ARMA:
    def __init__(self, data):
        self._data = data

    def start_modeling(self):
        arma_model_array = self.construct_arma_array()
        best_arma_model = self.find_optimal_model(arma_model_array)
        return best_arma_model

    def construct_arma_array(self):
        arma_array = []
        for p in range(0, 10):
            for q in range(0, 10):
                arma = self.fit_models(p, q)
                arma_array.append(arma)
        return arma_array
        # fit data into an ARMA model with order (p,q)

    def fit_models(self, p, q):
        arma = sm.tsa.ARMA(self._data, (4, 0)).fit(disp=0)
        aic = arma.aic
        return arma

    # Return the optimal ARMA model based on finding min of AIC
    def find_optimal_model(self, arma_array):
        # cosntruct an array of AIC from ARMA models
        aic_list = []
        for arma_model in arma_array:
            aic_list.append(arma_model.aic)
        aic_list_np = np.array(aic_list)
        min_index = aic_list_np.argmin()
        # return index of aic min in the array
        return arma_array[min_index]
