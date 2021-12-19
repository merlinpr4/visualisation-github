
print("Accessing logged in users data");

from dotenv import load_dotenv
load_dotenv("C:/Users/merli/Desktop/git v/visualisation-github/api.env")

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
g = Github(token)


#Let's get the user object and build a data dictionary
usr = g.get_user()


dct = {'user':         names[usr.login].replace(" ", ""), # anonymising
       'fullname':     names[usr.name],  # anonymising
       'location':     usr.location,
       'company':      usr.company,
       'public_repos': usr.public_repos
       
       }

for k, v in dict(dct).items():
    if v is None:
        del dct[k]
        
#print ("dictionary is " + json.dumps(dct))
        
# Establish connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a database
db = client.classDB

db.githubuser.insert_many([dct])     
   
    # iterate over all public repositories uncomment to see above function in action
# for repo in usr.get_repos():
#     print_repo(repo)
#     print("="*100)
        
        
for r in usr.get_repos():
  
    commits = 0      
    try:
     commits = r.get_commits().totalCount
    except Exception: #empty repos with 0 commits default to 0
      pass
    
    dct = {     "name": r.full_name,
                # repository description
                "description": r.description,
                # the date of when the repo was created
                "date created": r.created_at,
                # the date of the last git push
                "date of last push": r.pushed_at,
                #number of commits 
                "number of commits:": commits,
                # programming language
                "language": r.language
                }
    for k, v in dict(dct).items():
        if v is None:
            del dct[k] 
            
            
    print ("repo:" + json.dumps(dct, indent=4, sort_keys=True, default=str))  #this removes the wierd indentation issues
  #  db.githubuser.insert_many([dct]) 
    
  
    
# with open('graph.csv', 'w') as f:
#     f.write('Repo,Commits\n')
#     for repo in dct:
#         pprint.pprint(repo)
#         print()
#         f.write(repo['name'] + ',' + str(repo["commits"]) + '\n')
       
    
    
    
     
  
 
    

 

            
  
    
    