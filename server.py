#!eikonrest/bin/python
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps
import eikon as ek
import yaml

app = Flask(__name__)
api = Api(app)
conf = yaml.load(open('config.yml'))
ek.set_app_id(conf['eikon']['apikey'])

class Query(Resource):
    def get(self, syms, fields):
        df, err = ek.get_data(syms.split(','), fields.split(','))
        result = {'data': df, 'error': err}
        return jsonify(result)

if __name__ == '__main__':
    app.run(port='1368')