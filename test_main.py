import unittest
from main import add

class TestSomething(unittest.TestCase):

    def test_example(self):
        self.assertEqual(add(2,3), 5)

if __name__ == "__main__":
    unittest.main()
