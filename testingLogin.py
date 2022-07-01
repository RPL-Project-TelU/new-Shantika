from pickle import TRUE
import unittest
import main_project

class TestProject(unittest.TestCase):

    def test_login(self):
        login = main_project.Ok(" ", " ")
        self.assertEqual(login, TRUE)
