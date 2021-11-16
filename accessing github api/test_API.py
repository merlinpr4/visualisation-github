from unittest import TestCase 
from github import Github
from pprint import pprint

from username import print_repo

class Test(TestCase):
    def test_username(self):
        
        username = "merlinpr4" 
        g = Github()
        user = g.get_user(username)
        repo = user.get_repos(1)
        print("Full name:", repo.full_name)
    
        self.assertEqual(repo.full_name,"merlinpr4/branch-practise","Full name:")
        self.assertEqual(repo.language,"Java","language:")
        
         