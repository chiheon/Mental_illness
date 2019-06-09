from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from binaryModel import BinaryModel
from util import Util
import json
import ast

app = Flask(__name__)
api = Api(app)


class Graph(Resource):
    def post(self):
        return {'result': 'ok'}
    def get(self):
        with open('date_value.txt', 'r') as file:
            date_value = file.read()
        date_value = ast.literal_eval(date_value)
        with open('date.txt', 'r') as file:
            date = file.read()
        date = ast.literal_eval(date)
        return {'date': date,
                'data': date_value}

class Wordcloud(Resource):
    def post(self):
        return {'result': 'ok'}
    def get(self):
        with open('sliced_schizophrenia_free_noun_descending.txt', 'r') as file:
             aa = file.read()
        sliced_schizophrenia_free_descending_txt = ast.literal_eval(aa)
        with open('sliced_adhd_free_noun_descending.txt', 'r') as file:
             aa = file.read()
        sliced_adhd_free_descending_txt = ast.literal_eval(aa)
        with open('sliced_sad_noun_descending.txt', 'r') as file:
             aa = file.read()
        sliced_sad_descending_txt = ast.literal_eval(aa)
        
        sliced_schizophrenia_descending = Util().sliced_dic(sliced_schizophrenia_free_descending_txt, 100)
        sliced_adhd_descending = Util().sliced_dic(sliced_adhd_free_descending_txt, 100)
        sliced_sad_descending = Util().sliced_dic(sliced_sad_descending_txt, 100)
        
        return {'sad': sliced_sad_descending,
                'adhd': sliced_adhd_descending,
                'schizophrenia': sliced_schizophrenia_descending}
    
    
class Test(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('contents', type=str)
        args = parser.parse_args()
        print(args)
        contents = args['contents']
        print(contents)
        prob = BinaryModel().predict(contents)
        print(prob)
        return {'sad': str(prob[0]),'adhd':str(prob[1]), 'schi':str(prob[2])}


api.add_resource(Graph, '/graph/data')
api.add_resource(Wordcloud, '/wordcloud/data')
api.add_resource(Test, '/test')


if __name__ == '__main__':
    app.run(debug=True)