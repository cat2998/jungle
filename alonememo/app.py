import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('mongodb+srv://cat2998:test@cluster0.gfobnbx.mongodb.net/?retryWrites=true&w=majority')
db = client.alonememo

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/memo", methods=["GET"])
def listing():
    result = list(db.article.find({}, {'_id':0}))
    return jsonify({'result':'success', 'articles': result})

@app.route("/memo", methods=["POST"])
def saving():
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']

    if "http" not in url_receive:
        url_receive = "http://" + url_receive

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    og_image = soup.select_one('meta[property="og:image"]')
    og_title = soup.select_one('meta[property="og:title"]')
    og_desc = soup.select_one('meta[property="og:description"]')
    url_image = og_image['content']
    url_title = og_title['content']
    url_desc = og_desc['content']

    article = {
        'url':url_receive, 'title':url_title, 'desc':url_desc, 'image':url_image, 'comment':comment_receive
    }

    db.article.insert_one(article)

    return jsonify({'result':'success'})

if __name__ == '__main__':
    app.run('0.0.0.0',port=5002,debug=True)
