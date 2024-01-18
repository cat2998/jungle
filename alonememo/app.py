import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from flask import Flask, render_template, jsonify

app = Flask(__name__)

client = MongoClient('mongodb+srv://cat2998:test@cluster0.gfobnbx.mongodb.net/?retryWrites=true&w=majority')
client.alonememo

@app.route("/")
def home():
    return render_template('index.html')

# @app.route("/memo", method=["GET"])
# def listing():


# @app.route("/memo", method=["POST"])
# def saving():


if __name__ == '__main__':
    app.run('0.0.0.0',port=5002,debug=True)