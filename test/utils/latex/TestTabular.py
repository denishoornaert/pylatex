import unittest

from utils.latex import Tabular

class TestTabular(unittest.TestCase):

    def test_completeTabular(self):
        matrix = [[i*j for j in range(3)] for i in range(3)]
        tabular = Tabular(matrix)
        res = tabular.__latex__()
        answer = "\\begin{tabular}{|c|c|c|}\n\t\\hline\n\t 0 & 0 & 0 \\\\ \n\t\\hline\n\t 0 & 1 & 2 \\\\ \n\t\\hline\n\t 0 & 2 & 4 \\\\ \n\t\\hline\n\\end{tabular}\n"
        self.assertEqual(res, answer)

    def test_incompleteTabular(self):
        matrix = [[i*j for j in range(i, 3, 1)] for i in range(3)]
        tabular = Tabular(matrix)
        res = tabular.__latex__()
        answer = "\\begin{tabular}{|c|c|c|}\n\t\\hline\n\t 0 & 0 & 0 \\\\ \n\t\\hline\n\t 1 & 2 &   \\\\ \n\t\\hline\n\t 4 &   &   \\\\ \n\t\\hline\n\\end{tabular}\n"
        self.assertEqual(res, answer)

    def test_notAnArrayTabularConstruction(self):
        matrix = 42
        with self.assertRaises(TypeError):
            tabular = Tabular(matrix)

    def test_arrayTabularConstruction(self):
        matrix = [0, 1, 2]
        tabular = Tabular(matrix)
        res = tabular.__latex__()
        answer = "\\begin{tabular}{|c|}\n\t\\hline\n\t 0 \\\\ \n\t\\hline\n\t 1 \\\\ \n\t\\hline\n\t 2 \\\\ \n\t\\hline\n\\end{tabular}\n"
        self.assertEqual(res, answer)

    def test_completeRectangularMatrix(self):
        matrix = [[i*j for j in range(2)] for i in range(3)]
        tabular = Tabular(matrix)
        res = tabular.__latex__()
        answer = "\\begin{tabular}{|c|c|}\n\t\\hline\n\t 0 & 0 \\\\ \n\t\\hline\n\t 0 & 1 \\\\ \n\t\\hline\n\t 0 & 2 \\\\ \n\t\\hline\n\\end{tabular}\n"
        self.assertEqual(res, answer)

    def test_notAllElementAreArrays(self):
        matrix = [1, [1, 1], [1, 2, 1]]
        tabular = Tabular(matrix)
        res = tabular.__latex__()
        answer = "\\begin{tabular}{|c|}\n\t\\hline\n\t 1 \\\\ \n\t\\hline\n\t [1, 1] \\\\ \n\t\\hline\n\t [1, 2, 1] \\\\ \n\t\\hline\n\\end{tabular}\n"
        self.assertEqual(res, answer)

    def test_tabularWithHeader(self):
        matrix = [[i*j for j in range(3)] for i in range(3)]
        tabular = Tabular(matrix)
        tabular.setHeader(["a", "b", "c"])
        res = tabular.__latex__()
        answer = "\\begin{tabular}{|c|c|c|}\n\t\\hline\n\t a & b & c \\\\ \n\t\\hline\n\t 0 & 0 & 0 \\\\ \n\t\\hline\n\t 0 & 1 & 2 \\\\ \n\t\\hline\n\t 0 & 2 & 4 \\\\ \n\t\\hline\n\\end{tabular}\n"
        self.assertEqual(res, answer)

    def test_tabularWithHeaderLargerThanMatrix(self):
        matrix = [[i*j for j in range(2)] for i in range(3)]
        tabular = Tabular(matrix)
        tabular.setHeader(["a", "b", "c"])
        res = tabular.__latex__()
        answer = "\\begin{tabular}{|c|c|c|}\n\t\\hline\n\t a & b & c \\\\ \n\t\\hline\n\t 0 & 0 &   \\\\ \n\t\\hline\n\t 0 & 1 &   \\\\ \n\t\\hline\n\t 0 & 2 &   \\\\ \n\t\\hline\n\\end{tabular}\n"
        self.assertEqual(res, answer)

    def test_tabularWithHeaderSmallerThanMatrix(self):
        matrix = [[i*j for j in range(3)] for i in range(2)]
        tabular = Tabular(matrix)
        tabular.setHeader(["a", "b"])
        res = tabular.__latex__()
        answer = "\\begin{tabular}{|c|c|c|}\n\t\\hline\n\t a & b &   \\\\ \n\t\\hline\n\t 0 & 0 & 0 \\\\ \n\t\\hline\n\t 0 & 1 & 2 \\\\ \n\t\\hline\n\\end{tabular}\n"
        self.assertEqual(res, answer)

    def test_tabularWithSideColumn(self):
        matrix = [[i*j for j in range(2)] for i in range(2)]
        tabular = Tabular(matrix)
        tabular.setSideColumn(["a", "b"])
        res = tabular.__latex__()
        answer = "\\begin{tabular}{|c|c|c|}\n\t\\hline\n\t a & 0 & 0 \\\\ \n\t\\hline\n\t b & 0 & 1 \\\\ \n\t\\hline\n\\end{tabular}\n"
        self.assertEqual(res, answer)

    def test_tabularWithSideColumnLargerThanMatrix(self):
        matrix = [[i*j for j in range(2)] for i in range(2)]
        tabular = Tabular(matrix)
        tabular.setSideColumn(["a", "b", "c"])
        res = tabular.__latex__()
        answer = "\\begin{tabular}{|c|c|c|}\n\t\\hline\n\t a & 0 & 0 \\\\ \n\t\\hline\n\t b & 0 & 1 \\\\ \n\t\\hline\n\t c &   &   \\\\ \n\t\\hline\n\\end{tabular}\n"
        self.assertEqual(res, answer)

    def test_tabularWithHeaderAndSideColumn(self):
        matrix = [[i*j for j in range(3)] for i in range(3)]
        tabular = Tabular(matrix)
        tabular.setHeader(["a", "b", "c"])
        tabular.setSideColumn(["a", "b", "c"])
        res = tabular.__latex__()
        answer = "\\begin{tabular}{|c|c|c|c|}\n\t\\hline\n\t   & a & b & c \\\\ \n\t\\hline\n\t a & 0 & 0 & 0 \\\\ \n\t\\hline\n\t b & 0 & 1 & 2 \\\\ \n\t\\hline\n\t c & 0 & 2 & 4 \\\\ \n\t\\hline\n\\end{tabular}\n"
        self.assertEqual(res, answer)
