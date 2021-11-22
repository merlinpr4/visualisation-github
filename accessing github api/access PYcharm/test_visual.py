from unittest import TestCase
from github import Github
from pprint import pprint

from visual import API


class Test(TestCase):
    def test_pycharm(self):
            a = API()
            self.assertEqual(a.hi(), "hi" , "checking")

    def test_single_repo(self):
        username = "merlinpr4"
        # pygithub object  put in authorisation code if rate limited
        g = Github("")
        # get that user by username
        user = g.get_user(username)

        repo = user.get_repo("LCA")

        self.assertEqual(repo.full_name, "merlinpr4/LCA", "Full name:")
        self.assertEqual(repo.language, "Java", "Language:")
        self.assertEqual(repo.get_commits().totalCount, 47, "Commits:")

    def test_repo_fuction(self):
        a = API()
        self.assertEqual(a.LCA_repo().full_name, "merlinpr4/LCA", "checking")
        self.assertEqual(a.LCA_repo().full_name, "merlinpr4/LCA", "Full name:")
        self.assertEqual(a.LCA_repo().language, "Java", "Language:")
        self.assertEqual(a.LCA_repo().get_commits().totalCount, 47, "Commits:")



