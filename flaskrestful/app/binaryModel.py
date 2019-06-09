#!/usr/bin/python
# -*- coding: utf-8 -*-
import dill
import sen2vec
from sklearn.svm import SVC

class BinaryModel:
    def __init__(self):
        self.load()

    def load(self):
        self.sad_model = dill.load(open("./sad_svm.model","rb"))
        self.adhd_model = dill.load(open("./adhd_svm.model","rb"))
        self.schi_model = dill.load(open("./schizophrenia_svm.model","rb"))

    def predict(self, content):
        temp = [('1', '1', content, 1)]
        sen2vecs = sen2vec.Sentence2Vec()
        test_vec = sen2vecs.get_vector(temp)
        sad_prob = self.sad_model.predict_proba(test_vec)
        adhd_prob = self.adhd_model.predict_proba(test_vec)
        schizophrenia_prob = self.schi_model.predict_proba(test_vec)
        return [sad_prob.tolist()[0], adhd_prob.tolist()[0], schizophrenia_prob.tolist()[0]]