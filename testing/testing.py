from tkinter import Button, Label
import unittest
import main_project

class TestProject(unittest.TestCase):

    def test_login(self):
        self.assertTrue("user", "123")

    def test_button(self):
        self.assertTrue(Button, "Login")
    
    def test_label(self):
        self.assertTrue(Label,"UserName")
    
    def test_label(self):
        self.assertTrue(Label,"Password")
    
    

    

    

    

