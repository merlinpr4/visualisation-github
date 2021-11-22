#these files were run in pycharm to test access requires my user access token if you get rate limited but tests can be configured to vscode
import base64

from github import Github


class API:
    import requests
    from pprint import pprint

    # github username   using this website to learn more #https://www.thepythoncode.com/article/using-github-api-in-python
    # username = "x4nth055"
    username = "merlinpr4"
    # url to request
    url = f"https://api.github.com/users/{username}"
    # make the request and return the json
    user_data = requests.get(url).json()
    # pretty print JSON data
    # pprint(user_data)

    import base64
    from github import Github
    from pprint import pprint

    # Github username
    ##username = "x4nth055"  #note using a username without authentication means rateLimit is lower
    username = "merlinpr4"
    # pygithub object  put in authorisation code if rate limited
    g = Github("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")
    # get that user by username
    user = g.get_user(username)

    # for repo in user.get_repos():
    #     print(repo)

    def hi(self):
        return "hi"

    def LCA_repo(self):
        username = "merlinpr4"
        # pygithub object  put in authorisation code if rate limited
        g = Github("")
        # get that user by username
        user = g.get_user(username)

        repo = user.get_repo("LCA")
        return repo




