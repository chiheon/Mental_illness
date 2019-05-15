#!/usr/bin/python
# -*- coding: utf-8 -*-
import dill
from sen2vec import Sentence2Vec
from sklearn.ensemble import RandomForestClassifier

class RfModel:
    def __init__(self):
        self.load("binary_rf.model")
        self.load_3("3_rf.model")

    def load(self, model_file):
        self.model = dill.load(open("./" + model_file,"rb"))

    def load_3(self, model_file):
        self.model_3 = dill.load(open("./" + model_file,"rb"))

    def predict(self, content):
        temp = [('1','1',content)]
        sen2vec = Sentence2Vec()
        vec = sen2vec.get_vector(temp)
        y_pred = self.model.predict(vec)
        return y_pred

    def predict_3(self, content):
        temp = [('1', '1', content)]
        sen2vec = Sentence2Vec()
        vec = sen2vec.get_vector(temp)
        y_pred = self.model_3.predict(vec)
        return y_pred