
print("Accessing logged in users data");

from dotenv import load_dotenv
load_dotenv("api.env")



from github import Github   # github api access
import json                 # for converting a dictionary to a string
import pymongo              # for mongodb access
import os

import pprint               # for pretty printing db data
import json

# Load the faker and its providers
from faker import Faker     # for anonymising names
from collections import defaultdict
faker  = Faker()
names  = defaultdict(faker.name)


#user token from env file
token = os.getenv("TOKEN")
print("token" + token)
g = Github(token)
usr = g.get_user()

#alt version taking username warning gets rate limited
#g = Github("bluesmiley")
# g = Github()
# #Let's get the user object and build a data dictionary
# usr = g.get_user("Username")


dct = {'user':         names[usr.login].replace(" ", ""), # anonymising
       'fullname':     names[usr.name],  # anonymising
       'location':     usr.location,
       'company':      usr.company,
       'public_repos': usr.public_repos
       
       }

#print ("dictionary is " + json.dumps(dct))

for k, v in dict(dct).items():
    if v is None:
        del dct[k]
        
print ("cleaned dictionary is " + json.dumps(dct))
        
# Establish connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a database
db = client.classDB

db.githubuser.insert_many([dct])     
   


# now lets get those followers
fl = usr.get_followers()

for f in fl:
    dct = {'user':         names[f.login].replace(" ",""), # anonymising
           'fullname':     names[f.name], # anonymising
           'location':     f.location,
           'company':      f.company,
           'public_repos': f.public_repos
           }
    for k, v in dict(dct).items():
        if v is None:
            del dct[k]
        
    print("follower: " + json.dumps(dct))
    db.githubuser.insert_many([dct])    


 
        
for r in usr.get_repos():

    commits = 0      
    try:
     commits = r.get_commits().totalCount
    except Exception: #empty repos with 0 commits default to 0
      pass
    
    dct = {     "repo": r.name,
                # repository description
                "description": r.description,
                # the date of when the repo was created
                "created": r.created_at,
                # the date of the last git push
                "last_push": r.pushed_at,
                #total number of commits 
                "total_commits": commits,
                 "total size": r.size,
                # main programming language
                "language": r.language
                }
    for k, v in dict(dct).items():
        if v is None:
            del dct[k] 
            
            
    print ("repo:" + json.dumps(dct, indent=4, sort_keys=True, default=str))  #indent removes the wierd indentation issues with dates
    db.githubrepo.insert_many([dct]) 
    
    
    
 
    

 

            
  
    
    