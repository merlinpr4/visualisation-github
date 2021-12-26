print("Accessing logged in users data");

#make sure to create a env file called api.env with TOKEN = "your authenication key"
from dotenv import load_dotenv
load_dotenv("api.env")

from github import Github   # github api access
import json                 # for converting a dictionary to a string
import pymongo              # for mongodb access
import os

import pprint               # for pretty printing db data
import json

#user token from env file
token = os.getenv("TOKEN")
print("token" + token)
g = Github(token)
usr = g.get_user()

#alt version taking username warning gets rate limited
#g = Github("username")
# g = Github()
# #Let's get the user object and build a data dictionary
# usr = g.get_user("Username")


dct = {'user':         usr.login, 
       'fullname':     usr.name, 
       'location':     usr.location,
       'company':      usr.company,
       'repos': usr.public_repos,
       "followers"   : usr.followers,
       "following"   : usr.following,
       "profile_pic" : usr.avatar_url
       
       }

for k, v in dict(dct).items():
    if v is None:
        del dct[k]
        
print ("dictionary is " + json.dumps(dct))
        
# Establish connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a database
db = client.classDB

db.githubuser.insert_many([dct])     
   

#getting information about the logged in users repositories        
for r in usr.get_repos():
#    print( r.get_stats_commit_activity().totalCount)
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
                "contributors" : r.get_contributors().totalCount,
               # "total deletions" : r.get_stats_code_frequency,
                 "size": r.size,
                # main programming language
                "language": r.language
                }
    for k, v in dict(dct).items():
        if v is None:
            del dct[k] 
            
    #uncomment if you want to see the database contents for debugging 
    #print ("repo:" + json.dumps(dct, indent=4, sort_keys=True, default=str))  #indent removes the wierd indentation issues with dates
    db.githubrepo.insert_many([dct]) 
    
    
    
 
    

 

            
  
    
    