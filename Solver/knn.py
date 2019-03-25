import pandas as pd
import numpy as np
import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals import joblib
import os.path

class colorrec:
    def __init__(self):
        if os.path.exists('Param2.joblib'):
            self.knn = joblib.load('Param2.joblib')
        else:
            data = pd.read_csv('Trainingdata2.csv',header=None)
            (length,cols) = data.shape
            Train_X = data.iloc[0:length,0:3]
            Train_y = data.iloc[0:length,3:4]
            self.knn = KNeighborsClassifier(n_neighbors = 3)
            self.knn.fit(Train_X,Train_y.values.ravel())
            joblib.dump(self.knn,'Param2.joblib')

    def color(self,data):
        return self.knn.predict(data)

    def accuracy(self):
        data = pd.read_csv('Trainingdata2.csv',header=None)
        (length,cols) = data.shape
        Test_X = data.iloc[0:length,0:3]
        Test_y = data.iloc[0:length,3:4]
        return self.knn.score(Test_X,Test_y)