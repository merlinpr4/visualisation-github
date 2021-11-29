
# a script to do python based access to the github api
# step 4 - Let's store our data in a mongodb
# remember to pip install pymongo

print("Demonstration python based github api access");

from dotenv import load_dotenv
load_dotenv("C:/Users/merli/Desktop/git v/visualisation-github/api.env")

from github import Github   # github api access
import json                 # for converting a dictionary to a string
import pymongo              # for mongodb access
import os

#we initialise a PyGithub Github object with our access token.
#     note that this token is ours, and now deleted. You must 
#     crete your own access token and use here instead. 
token = os.getenv("TOKEN")
g = Github(token)

#Let's get the user object and build a data dictionary
usr = g.get_user()

dct = {'user':         usr.login,
       'fullname':     usr.name,
       'location':     usr.location,
       'company':      usr.company,
       'public_repos': usr.public_repos
       }

print ("dictionary is " + json.dumps(dct))

# now let's store the dictionary in a mongodb

# first we need to remove null fields from the dictionary, because
# if we don't we'll end up with null fields in the db. This will cause us
# lots of debugging problems later. The convention is only store actual data
# in the database.

for k, v in dict(dct).items():
    if v is None:
        del dct[k]

print ("cleaned dictionary is " + json.dumps(dct))

# now let's store the data.

# Establish connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a database
db = client.classDB

db.githubuser.insert_many([dct])

# now for demo purposes we'll get some data. We'll get the accounts followers
# and for each of them we'll get and add a count of the number of repos they have
fc = usr.followers
print ("followers: " + str(fc))

# now lets get those followers
fl = usr.get_followers()

for f in fl:
    dct = {'user':         f.login,
           'fullname':     f.name,
           'location':     f.location,
           'company':      f.company,
           'public_repos': f.public_repos
           }
    for k, v in dict(dct).items():
        if v is None:
            del dct[k]
        
    print("follower: " + json.dumps(dct))

