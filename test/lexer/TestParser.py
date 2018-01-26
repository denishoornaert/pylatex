import unittest
import sys

sys.path.append('../../src/lexer/')
sys.path.append('../../src/lexer/struct/')
sys.path.append('../../src/lexer/error/')

from Parser import Parser

class TestParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setup")

    @classmethod
    def tearDownClass(cls):
        print("teardown")

    def test_upper(self):
        pass

if __name__ == '__main__':
    unittest.main()
