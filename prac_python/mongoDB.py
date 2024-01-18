import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()

rowlist = rjson['RealtimeCityAir']['row']
for l in rowlist:
    if (l['IDEX_MVL'] < 70):
        print(l['MSRSTE_NM'], " : ", l['IDEX_MVL'])

# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = 'https://www.yes24.com/Product/Category/BestSeller?categoryNumber=001&pageNumber=1&pageSize=24'
yes = requests.get(url)

soup = BeautifulSoup(yes.text, 'html.parser')
books = soup.select('#yesBestList > li')
for book in books:
    print(book.select_one('a.gd_name').text.strip())

client = MongoClient('mongodb+srv://cat2998:test@cluster0.gfobnbx.mongodb.net/?retryWrites=true&w=majority')
db = client.cluster0

usr = {
    "name" : "동환",
    "age" : 28
}
usr2 = {
    "name" : "지현",
    "age" : 27
}

# db.users.insert_one(usr);
# db.users.insert_one(usr2);
all_users = db.users.find( {}, {'_id':False} )
# print(user[0]);
for usr in all_users:
    print(usr['name'], usr['age'])
print("-----")
user = list(db.users.find({"age":{"$gte":30}}, {'_id':0}))
for u in user:
    print(u['name'], u['age'])
print("-----")
db.users.update_one({'age':30}, {'$set':{'name':'동환'}})
all_users = db.users.find( {}, {'_id':False} )
for usr in all_users:
    print(usr['name'], usr['age'])
