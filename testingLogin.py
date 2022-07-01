from pickle import FALSE, TRUE
import unittest
import main_project

class TestProject(unittest.TestCase):
    def test_login(self):
        try:
            print("","Login Success")
        except:
            print("","Incorrent Username and Password")
