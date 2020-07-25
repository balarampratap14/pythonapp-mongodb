import data
import examine
import populate as pl
import copy as cp
import pymongo
import json
import random as rd

def pk_gen():
    pk = "_id"
    mydb = client['Output']
    colls = mydb.collection_names()
    mycollection = mydb[colls[0]]
    pk_list = [x[pk] for x in mycollection.find({},{ pk : 1 }) ]
    x = random.choice(pk_list)
    pk_list.remove(x)
    return x

def data_merge(a, b):
    """merges b into a and return merged list_of_config
    a = {'a': {1:{"a":"A"},2:{"b":"B","c":"C1"}}, 'b': 25.3659, 'c': [61,2]}
    b = {'a': {2:{"c":""},3:{"d":"D"}}, 'c': [5]}
    c = {}
    c = data_merge(a, b)
    c   //{'a': {1: {'a': 'A'}, 2: {'b': 'B', 'c': ''}, 3: {'d': 'D'}}, 'b': 25.3659, 'c': [61,2,5]}
    NOTE: tuples and arbitrary objects are not handled as it is totally ambiguous what should happen"""
    key = None
    
    if a is None or isinstance(a, str)or isinstance(a, int) or isinstance(a, float):
        if str(b) != "":
            a = b
    elif isinstance(a, list):
        if isinstance(b, list) and bool(b) == True :
            a.extend(b)
    elif isinstance(a, dict):
            # dicts must be merged
        if isinstance(b, dict) and bool(b) == True:
            for key in b:
                if key in a:
                    a[key] = data_merge(a[key], b[key])
                else:
                    a[key] = b[key]
    return a

sample_amount = 3
fake_documents_count = 5
pk = "_id"
fkey = "fkey-id"
sample_docs = []
config_from_outside = {}
fake_docs_list = []
'''client = pymongo.MongoClient("mongodb://demo:demo@demo-cluster-shard-00-00.93rbk.mongodb.net:27017,demo-cluster-shard-00-01.93rbk.mongodb.net:27017,demo-cluster-shard-00-02.93rbk.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-1391ze-shard-0&authSource=admin&retryWrites=true&w=majority")'''
client = pymongo.MongoClient(host = 'mongodb://mongo:27017/') 
mydb = client['Input']
colls = mydb.collection_names()
for col in colls:
    mycollection = mydb[col]
    doc=mycollection.aggregate( [ { '$sample': {'size': sample_amount} } ] )  
    for i in doc:
        sample_docs.append(i)
    list_of_config = []
    for i in range(0,len(sample_docs)):
        doc_i = sample_docs[i]
        for key, value in doc_i.items():
            val = examine.examine(key,value)
            doc_i[key] = val
        list_of_config.append(doc_i)
    count = 0
    for i in range(0,len(list_of_config)):
        print("CONFIG OF DOC -",count,":-", list_of_config[i], "\n")
        count = count + 1
    aggregated_config = {}
    for j in range(0,len(list_of_config)):
        config_j = list_of_config[j]
        data_merge(aggregated_config, config_j)
        print("Config Of Document ", j,"is MERGED!!" )
    print("\n Aggregated CONFIG is :- ", aggregated_config,"\n")
    
    data_merge(aggregated_config,config_from_outside)
    
    for i in range(0,fake_documents_count):
        fake_doc_i = cp.deepcopy(aggregated_config)
        for key, value in fake_doc_i.items():
            val = pl.populate(value)
            fake_doc_i[key] = val
        fake_docs_list.append(fake_doc_i)

    count = 0
    for i in range(0,len(fake_docs_list)):
        print("Fake DOC -",count,":-", fake_docs_list[i], "\n")
        count = count + 1
    c = "in-3"
    mydb = client['Output']
    mycollection = mydb[col]
    for i in range(0,len(fake_docs_list)):
        mycollection.insert_one(fake_docs_list[i])

mydb = client['Output']
colls = mydb.collection_names()
for i in range(1, len(colls)):
    mycollection = mydb[colls[i]]
    #mycollection.update_many({},{ "$set": { fk : pk_gen() } })
    for doc in mycollection.find():
        mycollection.update_one({"_id": doc["_id"]},{ "$set": {"fkey": pk_gen()}})

print("CODE EXECUTION DONE SUCESSFULLY")