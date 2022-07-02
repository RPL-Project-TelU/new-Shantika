from pickle import TRUE
from tkinter import Button
import unittest
import main_project

class TestProject(unittest.TestCase):

    def test_add(self):
        self.assertEqual("EXIT", TRUE)
    
    def test_button(self):
        self.assertEqual(Button, "SEARCH")
    
    def test_button(self):
        self.assertEqual(Button, "Book Now")
