import data
import pymongo

collection_name = "inputCN"
'''client = pymongo.MongoClient("mongodb://demo:demo@demo-cluster-shard-00-00.93rbk.mongodb.net:27017,demo-cluster-shard-00-01.93rbk.mongodb.net:27017,demo-cluster-shard-00-02.93rbk.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-1391ze-shard-0&authSource=admin&retryWrites=true&w=majority")'''
client = pymongo.MongoClient(host = 'mongodb://mongo:27017/')
mydb = client['Input']
mycollection = mydb[collection_name]
list_of_doc = []
list_of_doc = data.documents()
for i in range(0,len(list_of_doc)):
	mycollection.insert_one(list_of_doc[i])