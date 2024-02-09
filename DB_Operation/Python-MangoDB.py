#Install pymongo in Terminal or CMD prompt(pymongo)
import pymongo as pm

myclient=pm.MongoClient("mongodb://localhost:27017/")

#mydb=myclient["databaseName"]
mydb=myclient["MyDatabase"]

#Check if DB exists or not
#print(myclient.list_database_names())
# dblist=myclient.list_database_names()
# if "MyDatabase" in dblist:
#     print("The database exists.")
# else:
#     print("Database is not exists")

#mycol=mydb["collectionName"]
mycol=mydb["MyCollection"]

#Check if Colletion Exists
# print(mydb.list_collection_names())
# collist=mydb.list_collection_names()
# if "MyCollection" in collist:
#     print("The Collection is exists.")
# else:
#     print("Collection Not Exists.")

#Single row or document insert operation
# mydict={
#     'name':'James',
#     'address':'180, Vadodara'
# }
# x=mycol.insert_one(mydict)
# print("Row inserted: ", x)

#Multiple rows or Documents insert operation
# mylist=[{'name':'Amy','address':'181, Apple'},
# {'name':'Hannah','address':'182, Mountain'},
# {'name':'Micheal','address':'193, Valley'},
# {'name':'Sandy','address':'121, Occen blvd'},
# {'name':'Betty','address':'123, Sky st'},
# {'name':'Susan','address':'167, Park Lane'},
# {'name':'Ben','address':'145, Centerl st'},
# {'name':'William','address':'122, Main Road'},
# {'name':'Chuck','address':'143, Sideway'}
# ]
# x=mycol.insert_many(mylist)
# print("Many Records inserted: ", x)
#
# #print list of inserted documents _id values (x.inserted_ids)
# print(x.inserted_ids)

# Find One
# x=mycol.find_one()
# print(x)

# Find Many
# for x in mycol.find():
#     print(x)

#Update
# myquery={'address':'180, Vadodara'}
# newvalues={'$set':{'address':'Canyon 123'}}
#
# mycol.update_one(myquery, newvalues)
#
# for x in mycol.find():
#     print(x)

# limit
# myresult=mycol.find().limit(5)
# #print the result
# for x in myresult:
#     print(x)

# delete
# x=mycol.delete_many({})
# print(x.deleted_count, "documents deleted.")

# Delete Collection
mycol=mydb["MyCollection"]
mycol.drop()