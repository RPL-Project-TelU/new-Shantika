from tkinter import Label
import unittest
import main_project

class TestingStringMethods(unittest.TestCase):

    def test_label(self):
        self.assertTrue(Label,'NAME')

    def test_string_case(self):
        self.assertEqual('address'.upper(), 'ADDRESS')

    def test_is_string_upper(self):
        self.assertTrue('NAME'.isupper())
        self.assertFalse('Name'.isupper())
        
unittest.main()