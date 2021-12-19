
import pymongo              # for mongodb access
import pprint               # for pretty printing db data
import json
# Let's get the repo object from the db


print("Repo information from mongodb")


# Establish connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a database
db = client.classDB




with open('commits.csv', 'w') as f:
        f.write('Repo,Commits\n')
        dct = db.githubrepo.find({'repo': {'$exists': True}})
        for repo in dct:
            pprint.pprint(repo)
            print()
            f.write(repo['repo'] + ','   + str(repo['total_commits']) + '\n')
          

with open('data.csv', 'w') as f:
    f.write('User,RepoCount\n')
    dct = db.githubuser.find({'user': {'$exists': True}})
    for user in dct:
        pprint.pprint(user)
        print()
        f.write(user['user'] + ',' + str(user['public_repos']) + '\n')
    

