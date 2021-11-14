import requests
from pprint import pprint

# github username   using this website to learn more #https://www.thepythoncode.com/article/using-github-api-in-python
username = "x4nth055"
# url to request
url = f"https://api.github.com/users/{username}"
# make the request and return the json
user_data = requests.get(url).json()
# pretty print JSON data
#pprint(user_data)

import base64
from github import Github
from pprint import pprint

# Github username
username = "x4nth055"
#username = "merlinpr4"
# pygithub object
g = Github()
# get that user by username
user = g.get_user(username)

for repo in user.get_repos():
    print(repo)


def print_repo(repo):
    # repository full name
    print("Full name:", repo.full_name)
    # repository description
    print("Description:", repo.description)
    # the date of when the repo was created
    print("Date created:", repo.created_at)
    # the date of the last git push
    print("Date of last push:", repo.pushed_at)
    # home website (if available)
    print("Home Page:", repo.homepage)
    # programming language
    print("Language:", repo.language)
    # number of forks
    print("Number of forks:", repo.forks)
    # number of stars
    print("Number of stars:", repo.stargazers_count)
    print("-"*50)
    # repository content (files & directories)
    print("Contents:")
    for content in repo.get_contents(""):
        print(content)
    try:
        # repo license
        print("License:", base64.b64decode(repo.get_license().content.encode()).decode())
    except:
        pass