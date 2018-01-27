import unittest

from src.interpreter.Interpreter import Interpreter

class TestInterpreter(unittest.TestCase):

    def test_SimplePrint(self):
        res = Interpreter.execute('print("Blabla")')
        self.assertEqual(res, "Blabla\n")

    def test_SimpleOperationPrint(self):
        res = Interpreter.execute('print(1+2)')
        self.assertEqual(res, "3\n")

    def test_EmptyStringInput(self):
        res = Interpreter.execute('')
        self.assertEqual(res, "")

    def test_ErrorReporting(self):
        res = Interpreter.execute('123/0')
        self.assertEqual(res, "division by zero")

if __name__ == '__main__':
    unittest.main()
