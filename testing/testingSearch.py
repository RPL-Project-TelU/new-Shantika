
from tkinter import Button
import unittest
import main_project

class TestProject(unittest.TestCase):

    def test_button(self):
        self.assertTrue(Button, "EXIT")

    def test_button(self):
        self.assertTrue(Button, "SEARCH")
    
    def test_button(self):
        self.assertTrue(Button, "BOOK NOW")
