from sqlite3 import DatabaseError
import unittest
import design_pattern as dp

class TestAdd(unittest.TestCase):
    def test_tambah(self):
        p1 = dp.tambah_bus()
        p2 = dp.tambah_bus()
        self.assertEqual(dp.tambah_bus.busdatabase(p1), dp.tambah_bus.busdatabase(p2), "not equal")
        bus = dp.shantika.getdatabase("tambah_bus")
        print(f"tambah_bus: {bus.busdatabase()}")
    
if __name__ == '__main__':
    unittest.main()