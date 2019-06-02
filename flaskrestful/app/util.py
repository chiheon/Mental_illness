import itertools

    
class Util:
    def __init__(self): 
        return
        
    def dict_to_str(self, dic, size):
        temp = ''
        end = size
        for i in range(0,end,1):
            if i != (end - 1):
                temp += "{\'"+str(list(dic.items())[i][0])+"\': "+str(list(dic.items())[i][1])+"}, "
            else:
                temp += "{\'"+str(list(dic.items())[i][0])+"\': "+str(list(dic.items())[i][1])+"}"
        return temp
    
    def sliced_dic(self, dic, size):
        sliced_dict = dict(itertools.islice(dic.items(), size))
        return sliced_dict