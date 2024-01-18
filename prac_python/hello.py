a = 3
b = 2.5
print(a + b)
print(a - b)
print(a / b)
print(a // b)
print(a % b)

print(a * b)
print(a ** b)

fruits = ['사과','배','감','귤']

for i in range(len(fruits)):  # i 가 0, 1, 2, 3일 때 
    fruit = fruits[i]	
    print(fruit)

# 사과
# 배
# 감
# 귤
    
fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
cnt = 0;

for i in fruits:
    if i == '사과':
        cnt += 1

print(cnt)

people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

def findPeople(name):
    for i in range(len(people)):
        if (people[i]["name"] == name):
            return people[i]["age"]
    return "없음"

print(findPeople("bob"))

import requests # requests 라이브러리 설치 필요

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()

gus = rjson['RealtimeCityAir']['row']

for gu in gus:
    print(gu['MSRSTE_NM'], gu['IDEX_MVL'])