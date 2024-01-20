import requests
from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('mongodb+srv://cat2998:test@cluster0.gfobnbx.mongodb.net/?retryWrites=true&w=majority')
db = client.dbjungle

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/todo/list")
def todoList():
    result = list(db.todo.find({}, {'_id':0}))
    return jsonify({'result':'success', 'todos': result})

@app.route("/todo/insert", methods=["POST"])
def todoInsert():
    seq = findSeq()
    todo_value = request.form['todo_value']
    todo = {
        'seq':seq, 'todo':todo_value, 'completeYn':'N'
    }
    db.todo.insert_one(todo)
    return jsonify({'result':'success'})

@app.route("/todo/complete", methods=["POST"])
def todoComplete():
    seq = request.form["seq"]
    db.todo.update_one({"seq":int(seq)}, {"$set":{"completeYn":"Y"}})
    return jsonify({'result':'success'})

@app.route("/todo/update", methods=["POST"])
def todoUpdate():
    seq = request.form["seq"]
    todo = request.form["todo"]
    db.todo.update_one({"seq":int(seq)}, {"$set":{"todo":todo}})
    return jsonify({'result':'success'})

@app.route("/todo/delete", methods=["POST"])
def todoDelete():
    seq = request.form["seq"]
    db.todo.delete_one({"seq":int(seq)})
    return jsonify({'result':'success'})

def findSeq():
    sequence = 0
    seq = list(db.todo.find({},{'_id':0, 'seq':1}).sort({'seq':-1}).limit(1))
    if len(seq) != 0:
        sequence = seq[0]["seq"] + 1
    return sequence

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000, debug=True)