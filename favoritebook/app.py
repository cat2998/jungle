import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('mongodb+srv://cat2998:test@cluster0.gfobnbx.mongodb.net/?retryWrites=true&w=majority')
db = client.dbjungle

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/api/book/list", methods=["GET"])
def listBook():
    all_books = list(db.books.find({}, {'_id':0}).sort("like", -1))
    return jsonify({"result":"success", "all_books":all_books})

@app.route("/api/book/like", methods=["POST"])
def likeBook():
    id = request.form["id"]
    db.books.update_one({"id":int(id)}, {"$inc":{"like":1}})
    like = db.books.find_one({'id':int(id)}, {"_id":0, "like":1})
    return jsonify({"result":"success", "like":like["like"]})

@app.route("/api/book/update", methods=["POST"])
def updateBook():
    id = request.form["id"]
    auth = request.form["auth"]
    title = request.form["title"]
    db.books.update_one({"id":int(id)}, {"$set":{"auth":auth, "title":title}})
    return jsonify({"result":"success"})

@app.route("/api/book/delete", methods=["POST"])
def deleteBook():
    id = request.form["id"]
    db.books.delete_one({"id":int(id)})
    return jsonify({"result":"success"})

if __name__ == "__main__":
    app.run('0.0.0.0', port=5003, debug=True)