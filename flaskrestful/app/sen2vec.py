import numpy as np
import korea_nlp_twitter
import gensim.models.keyedvectors as word2vec


class Sentence2Vec:
    def __init__(self): 
        
        self.load("ko_300.bin")
        self.tokenizer = korea_nlp_twitter.Tokenizer()
        self.scores = {}
        
    def load(self, model_file):
        self.model = word2vec.KeyedVectors.load_word2vec_format(model_file, binary=True)
    
    def get_vector(self, sentence):
        sentence_list = []
        for i in range(0,len(sentence),1):
            temp = sentence[i][2]
            token = self.tokenizer.tokenize(temp,self.scores)
            vectors = [self.model.wv[w] for w in token
                if w in self.model.wv if self.check_conson_vowel(w)]
            v = np.zeros(self.model.vector_size)
            if (len(vectors) > 0):
                v = (np.array([sum(x) for x in zip(*vectors)])) / v.size
            sentence_list.append(v)
        return sentence_list
    
    def get_vector_noun(self, sentence):
        sentence_list = []
        for i in range(0,len(sentence),1):
            temp = sentence[i][2]
            token = self.tokenizer.noun_extract(temp,self.scores)
            vectors = [self.model.wv[w] for w in token
                if w in self.model.wv if self.check_conson_vowel(w)]
            v = np.zeros(self.model.vector_size)
            if (len(vectors) > 0):
                v = (np.array([sum(x) for x in zip(*vectors)])) / v.size
            sentence_list.append(v)
        return sentence_list
        
    def check_conson_vowel(self, token):
        conson_vowel = ['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ',\
               'ㄳ','ㅄ','ㅀ','ㄼ','ㅏ','ㅑ','ㅓ','ㅕ','ㅗ','ㅛ','ㅜ','ㅠ','ㅡ','ㅣ','ㅢ',\
               'ㅐ','ㅒ','ㅔ','ㅖ','ㅟ','ㅚ','ㅙ']
        for w in conson_vowel:
            if w in token:
                return False
        return True