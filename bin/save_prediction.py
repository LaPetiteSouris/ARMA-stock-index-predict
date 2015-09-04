__author__ = 'tung'
import pandas as pd


class Storage:
    def store(self, current_date, data):
        df = self.create_prediction_dataframe(current_date, data)
        storage_load = self.load_from_pickle()
        storage_load.append(df)
        self.save_to_pickle(storage_load)

    def create_prediction_dataframe(self, current_date, data):
        df = pd.DataFrame(data, index=current_date, colums='Prediction')
        return df

    def load_from_pickle(self):
        data_frame = pd.load('../prediction_result')
        return data_frame

    def save_to_pickle(self, dataframe):
        dataframe.save('../prediction_result')
