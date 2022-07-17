import pymongo
client = pymongo.MongoClient("mongodb+srv://maruthi:Prasad9951@cluster0.4qgequa.mongodb.net/?retryWrites=true&w=majority")
db = client.test
db.client.test
print(db)

client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    'name':'sudhnshu',
    'emailid':'sudhanshu@ineuron.ai',
    'surname':'kumar'
}

db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)