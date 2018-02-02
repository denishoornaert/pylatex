import unittest

from src.lexer.Parser import Parser
from src.lexer.struct import Environment
from src.lexer.error import UnclosedEnvironmentError

from test import TestConfiguration as config

class TestParser(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        self.parser = None

    def getCompletePath(self, filename):
        return config.latexTestFilePath + filename + config.pylatexExtension

    def test_CorrectParserInitalisation(self):
        filepath = self.getCompletePath("NoPythonEnvironment")
        self.parser = Parser(filepath)
        self.assertNotEqual(self.parser.content, "")
        self.assertEqual(self.parser.currentEnvironment, Environment.latex)
        self.assertEqual(self.parser.cursor, 0)

    def test_isStateLatex(self):
        filepath = self.getCompletePath("NoPythonEnvironment")
        self.parser = Parser(filepath)
        self.parser.currentEnvironment = Environment.latex
        self.assertTrue(self.parser.isStateLatex())

    def test_UncorrectIsStateLatex(self):
        filepath = self.getCompletePath("NoPythonEnvironment")
        self.parser = Parser(filepath)
        self.parser.currentEnvironment = Environment.python
        self.assertFalse(self.parser.isStateLatex())

    def test_NoPythonEnvironment(self):
        filepath = self.getCompletePath("NoPythonEnvironment")
        self.parser = Parser(filepath)
        res = self.parser.lex()
        self.assertEqual(res, (Environment.latex, self.parser.content))

    def test_NothingElseToRead(self):
        filepath = self.getCompletePath("NoPythonEnvironment")
        self.parser = Parser(filepath)
        res = self.parser.lex()
        with self.assertRaises(EOFError):
            res = self.parser.lex()

    def test_OnePythonEnvironment(self):
        filepath = self.getCompletePath("OnePythonEnvironment")
        self.parser = Parser(filepath)
        res = self.parser.lex()
        self.assertEqual(res, (Environment.latex, "\documentclass[a4paper,11pt]{article}\n\\begin{document}\n\section{test}\n"))
        res = self.parser.lex()
        self.assertEqual(res, (Environment.python, 'print("Blablablablabla...")'))
        res = self.parser.lex()
        self.assertEqual(res, (Environment.latex, "\n\end{document}"))

    def test_UnclosedPythonEnvironment(self):
        filepath = self.getCompletePath("UnclosedPythonEnvironment")
        self.parser = Parser(filepath)
        res = self.parser.lex()
        with self.assertRaises(UnclosedEnvironmentError):
            res = self.parser.lex()

    def test_MultiplePythonEnvironments(self):
        filepath = self.getCompletePath("MultiplePythonEnvironments")
        self.parser = Parser(filepath)
        res = self.parser.lex()
        self.assertEqual(res, (Environment.latex, "\documentclass[a4paper,11pt]{article}\n\\begin{document}\n\section{test}\n"))
        res = self.parser.lex()
        self.assertEqual(res, (Environment.python, 'print("Blablablablabla...")'))
        res = self.parser.lex()
        self.assertEqual(res, (Environment.latex, '\nSome meaningful text\n'))
        res = self.parser.lex()
        self.assertEqual(res, (Environment.python, 'print("Almost the end...")'))
        res = self.parser.lex()
        self.assertEqual(res, (Environment.latex, "\n\end{document}"))

    def test_TwoConsecutivePythonEnvironments(self):
        filepath = self.getCompletePath("TwoConsecutivePythonEnvironments")
        self.parser = Parser(filepath)
        res = self.parser.lex()
        self.assertEqual(res, (Environment.latex, "\documentclass[a4paper,11pt]{article}\n\\begin{document}\n\section{test}\n"))
        res = self.parser.lex()
        self.assertEqual(res, (Environment.python, 'print("Bla")'))
        res = self.parser.lex()
        self.assertEqual(res, (Environment.latex, ''))
        res = self.parser.lex()
        self.assertEqual(res, (Environment.python, 'print("Bla")'))
        res = self.parser.lex()
        self.assertEqual(res, (Environment.latex, "\n\end{document}"))

if __name__ == '__main__':
    unittest.main()
