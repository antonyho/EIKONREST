#!eikonrest/bin/python
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
# from json import dumps
import eikon as ek
import yaml

app = Flask(__name__)
api = Api(app)
conf = yaml.load(open('config.yml'))
ek.set_app_id(conf['eikon']['apikey'])


class Query(Resource):
    def get(self, syms, fs, params=''):
        #  Check UUID in Bearer of API request. This is a simple wrapper.
        token = request.headers.get('Authorization', None)
        if token is None:
            return None
        method, tokenstr = token.split()
        if method.lower() == "bearer" and tokenstr == conf['pywrapper']['apikey']:
            df = ek.get_data(instruments=str(syms).split(','), fields=str(fs).split(','), parameters=params,
                             raw_output=True)
            return jsonify(df)
        else:
            return None


class ListHSIOptions(Resource):
    def get(self, fs, params=''):
        #  Check UUID in Bearer of API request. This is a simple wrapper.
        token = request.headers.get('Authorization', None)
        if token is None:
            return None
        method, tokenstr = token.split()
        if method.lower() == "bearer" and tokenstr == conf['pywrapper']['apikey']:
            df = ek.get_data(instruments='0#HSI*.HF', fields=str(fs).split(','), parameters=params,
                             raw_output=True)
            return jsonify(df)
        else:
            return None


api.add_resource(Query, '/query/<string:syms>/<string:fs>', '/query/<string:syms>/<string:fs>/<string:params>')
api.add_resource(ListHSIOptions, '/allHSI/<string:fs>', '/allHSI/<string:fs>/<string:params>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1368)
