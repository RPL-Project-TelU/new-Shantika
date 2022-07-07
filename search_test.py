from sqlite3 import DatabaseError
import unittest
import design_pattern as dp

class TestSearch(unittest.TestCase):
    def test_cari(self):
        p1 = dp.cari_bus()
        p2 = dp.cari_bus2()
        self.assertEqual(dp.cari_bus.busdatabase(p1), dp.cari_bus.busdatabase(p2), "not equal")
        bus = dp.shantika.getdatabase("cari_bus")
        print(f"cari_bus: {bus.busdatabase()}")
    
if __name__ == '__main__':
    unittest.main()