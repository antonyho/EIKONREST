#!eikonrest/bin/python
from functools import wraps
from flask import Flask, request, Response, jsonify
from flask_restful import Resource, Api
# from json import dumps
import eikon as ek
import yaml

app = Flask(__name__)
api = Api(app)
conf = yaml.load(open('config.yml'))
ek.set_app_id(conf['eikon']['apikey'])


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        #  Check UUID in Bearer of API request. This is a simple wrapper.
        token = request.headers.get('Authorization', None)
        if token is None:
            return Response('Not authenticated', 401, {'WWWAuthenticate':'Token realm="Authentication Required"'})
        method, tokenstr = token.split()
        if method.lower() == "bearer" and tokenstr == conf['pywrapper']['apikey']:
            return f(*args, **kwargs)
        else:
            return Response('Not authenticated', 401, {'WWWAuthenticate':'Token realm="Authentication Required"'})
    return decorated

class Query(Resource):
    @requires_auth
    def get(self, syms, fs, params=''):
        df = ek.get_data(instruments=str(syms).split(','), fields=str(fs).split(','), parameters=params,
                         raw_output=True)
        return jsonify(df)

class Interval(Resource):
    @requires_auth
    def get(self, syms, start, end, fs='*', itrvl='weekly'):
        calc=request.args.get('calc')
        if calc is None or calc == '':
            calc='tradingdays'
        df = ek.get_timeseries(rics=str(syms).split(','), start_date=start, end_date=end, interval=str(itrvl),
                               fields=str(fs).split(','), calendar=calc, raw_output=True)
        return jsonify(df)


# Example: To search with a wildcard HK Heng Seng Index symbol '0#HSI*.HF'
# /get_data/0%23HSI*.HF/PUT_CALL,CF_LAST,CF_ASK,CF_BID,PCTCHNG
# Use %23 to replace pound '#' as it represents anchor/bookmark on URL
api.add_resource(Query, '/get_data/<string:syms>/<string:fs>', '/query/<string:syms>/<string:fs>/<string:params>')
api.add_resource(Interval, '/get_timeseries/<string:syms>/<string:start>/<string:end>/<string:fs>',
                 '/get_timeseries/<string:syms>/<string:start>/<string:end>/<string:fs>/<string:itrvl>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1368)
