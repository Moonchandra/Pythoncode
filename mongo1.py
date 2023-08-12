import random
import string
import pymongo

myclient = pymongo.MongoClient('mongodb+srv://chandra97:Munapunel1988@cluster0.ltfwgka.mongodb.net/?appName=mongosh+1.5.4')


#myclient = mongosh "mongodb+srv://chandra97:Munapunel1988cluster0.ltfwgka.mongodb.net/" --apiVersion 1 --username chandra97
#mydb = myclient["mydatabase"]
#print(myclient.list_database_names())
# mycol = mydb["customers"]
# mydict = { "name": "John", "address": "Highway 37" }
#
# x = mycol.insert_one(mydict)

li =[]
mydt = {}
for i in range(7000):
    mydt = {}
    mydt['_id']=''.join(random.choices(string.ascii_uppercase+string.digits, k=6))
    mydt['name']=''.join(random.choices(string.ascii_lowercase, k=8))
    mydt['address'] = ''.join(random.choices(string.ascii_lowercase, k=12))
    mydt['age']=random.randint(10,30)
    li.append(mydt)


mydb = myclient["mydatabase"]
mycol = mydb["large_datasets"]
mycol.insert_many(li)
res = mycol.find()
j = 0
for i in res:
	j+=1

j
#mycol.index_information()
mycol.find({'age':15}).explain()
mycol.create_index('age')