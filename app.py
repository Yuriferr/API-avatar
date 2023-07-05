from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app)

elementos = open("./data/elementos.json", "r", encoding="utf-8")
elementos = elementos.read()
elementos = json.loads(elementos)

@app.route('/' , methods=['GET'])
def get_dados():
    return jsonify(elementos)

dobras = open("./data/dobras.json", "r", encoding="utf-8")
dobras = dobras.read()
dobras = json.loads(dobras)

@app.route('/dobras' , methods=['GET'])
def get_dobras():
    return jsonify(dobras)


if __name__ == "__main__":
    app.run()
