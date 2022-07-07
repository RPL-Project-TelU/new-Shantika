import unittest 
import design_pattern as dp

class testLogin(unittest.TestCase):
    def test_user(self) :
        self.assertEqual(dp.log_in.username, ("jahfal"))

    def test_pass(self) :
        self.assertEqual(dp.log_in.password, ("123"))


if __name__ == "__main__" :
    unittest.main