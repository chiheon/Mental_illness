import korea_nlp_twitter
from soynlp.normalizer import *
from collections import OrderedDict

class Ngram:
    
    def __init__(self):
        self.tokenizer = korea_nlp_twitter.Tokenizer()

    #어절 n-gram 분석
    #sentence: 분석할 문장, num_gram: n-gram 단위
    def word_ngram(self, sentence, num_gram, scores):
      # in the case a file is given, remove escape characters
        token = self.tokenizer.tokenize(sentence,scores)
        text = tuple(token)
        ngrams = [text[x:x+num_gram] for x in range(0, len(text))]
        return ngrams

    #음절 n-gram 분석
    #sentence: 분석할 문장, num_gram: n-gram 단위
    def phoneme_ngram(self, sentence, num_gram):
        text = tuple(sentence) # split the sentence into an array of characters
        ngrams = [text[x:x+num_gram] for x in range(0, len(text))]
        return ngrams

    #n-gram 빈도 리스트 생성
    def make_freqlist(self, ngrams):
        freqlist = {}

        for ngram in ngrams:
            if (ngram in freqlist):
                freqlist[ngram] += 1
            else:
                freqlist[ngram] = 1

        return freqlist
    
    def find_nearest_group(self,data,group1,group2,group3):
        predict = []
        for i in range(0,len(data),1):
            dist1 = 0
            dist2 = 0
            dist3 = 0
            ngram_data = []
            temp = self.word_ngram(data[i][2],2,{})
            ngram_data = ngram_data + temp
            fre_data = self.make_freqlist(ngram_data)
            fre_descending = OrderedDict(sorted(fre_data.items(), 
                                          key=lambda kv: kv[1], reverse=True))    
            for key in fre_descending:
                if key in group1:
                    dist1 = dist1 + abs(list(group1.keys()).index(key)-list(fre_descending.keys()).index(key))
                else :
                    dist1 = dist1 + len(group1)
                if key in group2:
                    dist2 = dist2 + abs(list(group2.keys()).index(key)-list(fre_descending.keys()).index(key))
                else :
                    dist2 = dist2 + len(group2)
                if key in group3:
                    dist3 = dist3 + abs(list(group3.keys()).index(key)-list(fre_descending.keys()).index(key))
                else :
                    dist3 = dist3 + len(group3)

            if dist1 == min(dist1,dist2,dist3):
                predict.append(1)
            elif dist2 == min(dist1,dist2,dist3):
                predict.append(2)
            else:
                predict.append(3)
        return predict