from flask import Flask, jsonify
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

nacoes = open("./data/nacoes.json", "r", encoding="utf-8")
nacoes = nacoes.read()
nacoes = json.loads(nacoes)

@app.route('/nacoes' , methods=['GET'])
def get_nacoes():
    return jsonify(nacoes)

personagens = open("./data/personagens.json", "r", encoding="utf-8")
personagens = personagens.read()
personagens = json.loads(personagens)

@app.route('/personagens' , methods=['GET'])
def get_personagens():
    return jsonify(personagens)


if __name__ == "__main__":
    app.run()
