#access github api and stores data into a database
print("Accessing logged in users data from Github API");

#make sure to create a env file called api.env in visualise folder with TOKEN = "your authenication token" or NAME = "username you want to search" 
from dotenv import load_dotenv
load_dotenv("api.env")

from github import Github   # github api access
import json                 # for converting a dictionary to a string
import pymongo              # for mongodb access
import os

import pprint               # for pretty printing db data
import json

#user token from env file.
# supply your username  or use token to do authenicated requests
#if neither is supplied it defaults to my username  however usernames get rate limited

token = os.getenv("TOKEN")
if token != "place-token-here" and token != None:
    print(token)
    g = Github(token)
    usr = g.get_user()
else:
  username = os.getenv("NAME")
  print(username)
  if username == None:
        username = "merlinpr4"
        print("username is empty using default")
  g = Github()
  usr = g.get_user(username)

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
db = client.classDB

#logged in users stats  
def accessUserInfo():
  dct = {'user':         usr.login, 
        'fullname':     usr.name, 
        'location':     usr.location,
        'company':      usr.company,
        'repos':        usr.public_repos,
        "followers"   : usr.followers,
        "following"   : usr.following,
        "profile_pic" : usr.avatar_url
        
        }

  for k, v in dict(dct).items():
      if v is None:
          del dct[k]
          
  print ("dictionary is " + json.dumps(dct))
  db.githubuser.insert_many([dct])     
    
 #getting information about the logged in users repositories   
def accessRepoInfo():     
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
                  "contributors" : r.get_contributors().totalCount,
                  "size": r.size,
                  # top programming language
                  "language": r.language
                  }
      for k, v in dict(dct).items():
          if v is None:
              del dct[k] 
              
      #uncomment if you want to see the database contents for debugging 
      #print ("repo:" + json.dumps(dct, indent=4, sort_keys=True, default=str))  #indent removes the wierd indentation issues with dates
      db.githubrepo.insert_many([dct]) 
    
def main():
      accessUserInfo()
      accessRepoInfo()
      
    
if __name__ == '__main__':
  main()
    
    
    
 
    

 

            
  
    
    