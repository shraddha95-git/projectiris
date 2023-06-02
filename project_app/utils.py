
import pickle
import json
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import config


class Iris():
    def __init__(self, SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm):
        self.SepalLengthCm = SepalLengthCm
        self.SepalWidthCm = SepalWidthCm
        self.PetalLengthCm = PetalLengthCm
        self.PetalWidthCm = PetalWidthCm
       
    def load_models(self):
        with open (config.MODEL_FILE_PATH, 'rb') as f:
            self.model = pickle.load(f)
    
    def get_predicted_type(self):

        self.load_models()                # creating instance of model

        test_array = np.array([[self.SepalLengthCm, self.SepalWidthCm, self.PetalLengthCm, self.PetalWidthCm]]) 

        print("Test Array: ", test_array)

        prediction = self.model.predict(test_array)[0]

        return prediction

if __name__ == "__main__":
    SepalLengthCm  =  6.4
    SepalWidthCm   =  1.8
    PetalLengthCm  =  1.1
    PetalWidthCm   =  1.5

    iris = Iris(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm) 
    prediction = iris.get_predicted_type() 
    print("The Species of flower will be:", prediction)