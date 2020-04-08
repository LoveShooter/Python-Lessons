import pymongo
import requests

myclient = pymongo.MongoClient('mongodb+srv://sysadm:Ff121314@cluster0-gpxwq.mongodb.net/')

mydb = myclient['testdb']

print(mydb)

print(myclient.list_database_names())

dblist = myclient.list_database_names()
if "testdb" in dblist:
    print("The database Exists.")


#response = requests.get('https://jsonplaceholder.typicode.com/users')

#print (response) 
#print (response.status_code)

#for x in response.json():
#    print(x)

#for x in response.json():
#   if x['website'] == 'kale.biz':
#        print(x['name'])
#        print(x['phone'])

