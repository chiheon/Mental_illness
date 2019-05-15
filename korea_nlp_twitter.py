from konlpy.tag import Twitter
from soynlp.tokenizer import MaxScoreTokenizer

class Tokenizer:

    def __init__(self):
        self.t = Twitter()
        pass;
        
    def tokenize(self, sentence, score_dic):
        scores = score_dic
        tokenizer = MaxScoreTokenizer(scores=scores)
        token = tokenizer.tokenize(sentence)
        token_list = []

        for num, input in enumerate(token):
            twit_token = self.t.pos(token[num],norm=True,stem=True)
            for i in range(0,len(twit_token),1):
                if twit_token[i][1] != "Josa" and twit_token[i][1] != "Punctuation" and \
                twit_token[i][1] != "KoreanParticle" :
                    token_list.append(twit_token[i][0])

        return token_list
    
    def noun_extract(self, sentence, score_dic):
        scores = score_dic
        tokenizer = MaxScoreTokenizer(scores=scores)
        token = tokenizer.tokenize(sentence)
        noun_list = []
        compared_noun_list = self.t.nouns(sentence)
        
        for num, input in enumerate(token):
            if (token[num] in scores) == True:
                noun_list.append(token[num])
            elif (token[num] in scores) == False:
                twit_token = self.t.nouns(token[num])
                noun_list= noun_list + twit_token
        
        diff_noun_list = list(set(noun_list) - set(compared_noun_list))
        diff_noun_list = list(set(diff_noun_list) - set(score_dic.keys()))

        noun_list = list(set(noun_list) - set(diff_noun_list))
        return noun_list    

    def noun_extract_dup(self, sentence, score_dic):
        scores = score_dic
        tokenizer = MaxScoreTokenizer(scores=scores)
        token = tokenizer.tokenize(sentence)
        noun_list = []
        compared_noun_list = self.t.nouns(sentence)
        
        for num, input in enumerate(token):
            if (token[num] in scores) == True:
                noun_list.append(token[num])
            elif (token[num] in scores) == False:
                twit_token = self.t.nouns(token[num])
                noun_list= noun_list + twit_token
        
        diff_noun_list = list(set(noun_list) - set(compared_noun_list))
        diff_noun_list = list(set(diff_noun_list) - set(score_dic.keys()))

        noun_list = list(set(noun_list) - set(diff_noun_list))
        return noun_list
    
    def noun_counter(self, sentence, score_dic, word):
        noun_list = self.noun_extract(sentence,score_dic)
        number = 0
        for num, input in enumerate(noun_list):
            if input == word:
                number = number + 1
        
        return number