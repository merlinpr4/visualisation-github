
# a a script to clear the db
print("Demonstration python based mongodb access");


import pymongo              # for mongodb access
import pprint               # for pretty printing db data
import os

# Establish connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a database
db = client.classDB

db.githubuser.delete_many({})
db.githubrepo.delete_many({})

#delete the csv files
if os.path.exists("commits.csv"):  
    os.remove("commits.csv")
    
if os.path.exists("user_info.csv"):  
    os.remove("user_info.csv")

