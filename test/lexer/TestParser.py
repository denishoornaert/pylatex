import unittest
import sys

sys.path.append('../../src/lexer/')
sys.path.append('../../src/lexer/struct/')
sys.path.append('../../src/lexer/error/')

from Parser import Parser
from Environment import Environment

class TestParser(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        self.parser = None

    def test_CorrectParserInitalisation(self):
        self.parser = Parser("assets/NoPythonEnvironment.tex")
        self.assertNotEqual(self.parser.content, "")
        self.assertEqual(self.parser.currentEnvironment, Environment.latex)
        self.assertEqual(self.parser.cursor, 0)

    def test_isStateLatex(self):
        self.parser = Parser("assets/NoPythonEnvironment.tex")
        self.parser.currentEnvironment = Environment.latex
        self.assertTrue(self.parser.isStateLatex())

    def test_UncorrectIsStateLatex(self):
        self.parser = Parser("assets/NoPythonEnvironment.tex")
        self.parser.currentEnvironment = Environment.python
        self.assertFalse(self.parser.isStateLatex())

    def test_NoPythonEnvironment(self):
        self.parser = Parser("assets/NoPythonEnvironment.tex")
        res = self.parser.lex()
        self.assertEqual(res, (Environment.latex, self.parser.content))

    def test_NothingElseToRead(self):
        self.parser = Parser("assets/NoPythonEnvironment.tex")
        res = self.parser.lex()
        with self.assertRaises(EOFError):
            res = self.parser.lex()

    def test_OnePythonEnvironment(self):
        self.parser = Parser("assets/OnePythonEnvironment.tex")
        res = self.parser.lex()
        self.assertEqual(res, (Environment.latex, "\documentclass[a4paper,11pt]{article}\n\\begin{document}\n\section{test}\n"))
        res = self.parser.lex()
        self.assertEqual(res, (Environment.python, 'print("Blablablablabla...")'))
        res = self.parser.lex()
        self.assertEqual(res, (Environment.latex, "\n\end{document}"))

    def test_UnclosedPythonEnvironment(self):
        pass

    def test_MultiplePythonEnvironments(self):
        pass

    def test_TwoConsecutivePythonEnvironments(self):
        pass

if __name__ == '__main__':
    unittest.main()
