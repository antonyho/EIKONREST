#!eikonrest/bin/python
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps

app = Flask(__name__)
api = Api(app)

if __name__ == '__main__':
    app.run()