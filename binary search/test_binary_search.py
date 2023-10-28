import unittest
from binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    
    def test_simple_collection(self):
        simple_collection = [i for i in range(30)]
        for i in range(len(simple_collection)):
            with self.subTest(i=i):
                self.assertEqual(binary_search(i, simple_collection), i)


if __name__ == "__main__":
    unittest.main()
 