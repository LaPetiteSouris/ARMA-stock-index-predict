__author__ = 'tung'
import pickle


class Storage:
    def save_to_pickle(self, data):
        previous_prediction = pickle.load(open("../prediction_result", "rb"))
        previous_prediction.append(data)
        pickle.dump(previous_prediction, open("../prediction_result", "wb"))
