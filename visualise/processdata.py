#processes the data stored in the database into a csv files for the frontend
import pymongo              # for mongodb access
import pprint               # for pretty printing db data
import json

from datetime import datetime #for date strings

print("Processing data from mongadb database into csv files")


# Establish connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a database
db = client.classDB
      
with open('commits.csv', 'w') as f:
        f.write('Repo,Commits,Language,Size,Contributors,Days\n')
        dct = db.githubrepo.find({'repo': {'$exists': True}})
        for repo in dct:
            pprint.pprint(repo)
            print()
        
            language = "N/A" 
            try:
                language =  repo['language'] 
            except KeyError: #some repos dont have a language
             pass
         
            #find the number of days spend on the project by counting the days from when the repo was created and the last push to the repository
            date1 = repo["created"]
            date2 = repo["last_push"]
            days_spend = abs(date2 - date1).days 
            print(days_spend)
         
            f.write(repo['repo'] + ','   + str(repo['total_commits']) +','  + language  + "," +  str(repo['size']) + "," + str(repo['contributors']) + "," + str(days_spend)  + "\n")


with open("user_info.csv","w") as f :
    f.write("Username,Name,Followers,Following,Repos,Location,PP\n")
    dct = db.githubuser.find()

    for user in db.githubuser.find(): 
        f.write(user["user"] + "," + user["fullname"] +  "," + str(user["followers"]) + "," + str(user["following"]) +","+ str(user["repos"]) +"," + user["location"] + ","+ user["profile_pic"] + "\n" )
  
       
    
    