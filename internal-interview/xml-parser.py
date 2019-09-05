import xmltodict, json, pymongo
from pymongo import MongoClient
#from bson import json_util
fp = open('../internal-interview/sample.xml', 'r')
rows = fp.read()
o = xmltodict.parse(rows)
j = json.dumps(o)

client = MongoClient()
db = client.db_test
xm = db.xm

jp = open('../internal-interview/sample.json', 'w+')
jp.write(j)

with open('../internal-interview/sample.json') as f:
    file_data = json.load(f)

xm.insert_one(file_data)  

result = xm.find()
print(result)

for i in result:
    print(i)
    
client.close()
