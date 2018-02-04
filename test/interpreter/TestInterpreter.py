import unittest

from src.interpreter import Interpreter
from src.fileController import FileController

class TestInterpreter(unittest.TestCase):

    path = "test/interpreter/assets/"
    ext  = ".txt"

    def test_SimplePrint(self):
        instruction = FileController.read(TestInterpreter.path+"SimplePrint"+TestInterpreter.ext)
        res = Interpreter.execute(instruction)
        self.assertEqual(res, "Blabla")

    def test_SimpleOperationPrint(self):
        instruction = FileController.read(TestInterpreter.path+"SimpleOperationPrint"+TestInterpreter.ext)
        res = Interpreter.execute(instruction)
        self.assertEqual(res, "3")

    def test_EmptyStringInput(self):
        instruction = FileController.read(TestInterpreter.path+"EmptyFile"+TestInterpreter.ext)
        res = Interpreter.execute(instruction)
        self.assertEqual(res, "")

    def test_LineReturnStringInput(self):
        instruction = FileController.read(TestInterpreter.path+"LineReturnString"+TestInterpreter.ext)
        res = Interpreter.execute(instruction)
        self.assertEqual(res, "a\n")

    def test_ErrorReporting(self):
        instruction = FileController.read(TestInterpreter.path+"ErrorReporting"+TestInterpreter.ext)
        res = Interpreter.execute(instruction)
        self.assertEqual(res, "division by zero")

    def test_MultilineEnvironment(self):
        instruction = FileController.read(TestInterpreter.path+"MultilineEnvironment"+TestInterpreter.ext)
        res = Interpreter.execute(instruction)
        self.assertEqual(res, "17")

    def test_EnvironmentWithDoubleBackSlash(self):
        instruction = FileController.read(TestInterpreter.path+"EnvironmentWithDoubleBackSlash"+TestInterpreter.ext)
        res = Interpreter.execute(instruction)
        self.assertEqual(res, "0 & 1 & 2 \\\\ \n")

    def test_EscapeCharactersDoubleBackSlash(self):
        instruction = FileController.read(TestInterpreter.path+"EnvironmentWithDoubleBackSlash"+TestInterpreter.ext)
        res = Interpreter.escapeCharactersManagement(instruction)
        self.assertEqual(res, 'out(str(0)+" & "+str(1)+" & "+str(2)+" \\\\\\\\ \\n")')

if __name__ == '__main__':
    unittest.main()
