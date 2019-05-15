from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from rfModel import RfModel
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

class Test(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('contents', type=str)
        args = parser.parse_args()
        contents = args['contents']
        check = RfModel().predict(contents)
        check_3 = RfModel().predict_3(contents)
        return {'result': str(check[0]),'result_3':str(check_3[0])}


api.add_resource(Graph, '/graph/data')
api.add_resource(Test, '/test')


if __name__ == '__main__':
    app.run(debug=True)