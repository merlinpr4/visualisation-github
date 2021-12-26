
# a a script to clear the db
# step 7 - Let's do a useful search

print("Demonstration python based mongodb access");


import pymongo              # for mongodb access
import pprint               # for pretty printing db data
import os
#Let's get the user object from the db

# Establish connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a database
db = client.classDB

db.githubuser.delete_many({})
db.githubrepo.delete_many({})


if os.path.exists("commits.csv"):  
    os.remove("commits.csv")
    
if os.path.exists("user_info.csv"):  
    os.remove("user_info.csv")

