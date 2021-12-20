
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
      

with open('data.csv', 'w') as f:
    f.write('User,RepoCount\n')
    dct = db.githubuser.find({'user': {'$exists': True}})
    for user in dct:
    #    pprint.pprint(user)
        # print()
        f.write(user['user'] + ',' + str(user['public_repos']) + '\n')


repo_list = []
commits_list = []
language_list = []
description_list = []
with open('commits.csv', 'w') as f:
        f.write('Repo,Commits,Language,Description\n')
        dct = db.githubrepo.find({'repo': {'$exists': True}})
        for repo in dct:
            pprint.pprint(repo)
            print()
            repo_list.append(repo['repo'])
            commits_list.append(str(repo['total_commits']))
            
            language = "N/A" 
            try:
                language =  repo['language'] 
            except KeyError: #some repos dont have a language
             pass
         
            # description = "empty"
            # try:
            #     description =  repo['description'] 
            # except KeyError: #some repos dont have a language
            #  pass
             
     
            f.write(repo['repo'] + ','   + str(repo['total_commits']) +','  + language  + "," +  str(repo['size']) + "\n")



dictionary = dict(zip(repo_list,commits_list))

with open ("repoCommits","w") as outfile:
    json.dump(dictionary,outfile,indent=2)



        
# dct =  db.githubuser.find({'user': {'$exists': True}})   
# json_object = json.dumps(dct)
# print ("repo" + json_object)





# with open("repo.json", "w") as outfile:
#     outfile.write(json_object)
    

