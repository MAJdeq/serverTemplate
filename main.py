from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = A

@app.route("/")
def home():
    return "Home"

if __name__=="__main__":
    app.run(debug=True)