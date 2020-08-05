import unittest
class some_Test(unittest.TestCase):
    def test_never_true(self):
        self.assertTrue(1==2)
    def test_always_true(self):
        self.assertTrue(1==1)
    
if __name__ == "__main__":
    unittest.main()