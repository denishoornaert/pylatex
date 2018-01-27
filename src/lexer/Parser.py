from src.lexer.struct.Environment import Environment
from src.lexer.error.UnclosedEnvironmentError import UnclosedEnvironmentError
from src.lexer.error.PatternNotFoundError import PatternNotFoundError

class Parser():

    """docstring for Parser."""

    def __init__(self, filename):
        self.content = ""
        self.readFile(filename)
        self.currentEnvironment = Environment.latex
        self.cursor = 0

    def readFile(self, filename):
        """
        (private) Method that loads the content of the file given in parameter
        into the attribut 'content' of the object Parser.
        """
        f = open(filename)
        self.content = f.read().strip()
        f.close()

    def isStateLatex(self):
        """
        (public) Returns whether the previous environment was LaTex or Python.
        """
        return self.currentEnvironment == Environment.latex

    def indexOf(self, pattern, start=0):
        """
        (private) Returns the index of 'pattern' in 'self.content' from a
        specific start. If the pattern is not found, an error is raised.
        """
        index = self.content[start:].find(pattern)
        if(index >= 0):
            index += start
        else: # index == -1
            raise PatternNotFoundError("The pattern '"+pattern+"' has not been found")
        return index

    def manageNewEnvironment(self, index, delimiter):
        """
        (private) Returns a tuple of the environment and its associated content.
        In addition, the method manages correctly the object attributs.
        """
        res = None
        if(index >= 0):
            res = (self.currentEnvironment, self.content[self.cursor:index])
            self.cursor = index+len(delimiter)
            self.currentEnvironment = Environment.python if(self.isStateLatex()) else Environment.latex
        return res

    def manageEndEnvironment(self, delimiter):
        """
        (private) Returns a tuple of the environment and its associated content
        or raises an error if it appears that the python environment has not
        been closed (i.e. if no '?>' appears in the remaing input).
        """
        res = None
        if(delimiter == "<?"): # and index == -1 : the remaining of the file only contains latex environment
            res = (Environment.latex, self.content[self.cursor:])
            self.currentEnvironment = Environment.latex
            self.cursor = len(self.content)-1
        else: # delimiter == "?>" and index == -1 : the python environment is not closed
            raise UnclosedEnvironmentError("The Python environment openned at (x, y) is not closed.")
        return res

    def lex(self):
        """
        (public) Returns a tuple contaning the detected environment and its content. Will
        eventually raise an error when reaching the end of the file.
        """
        res = None
        if(self.cursor < len(self.content)-1):
            delimiter = "<?" if(self.isStateLatex()) else "?>"
            try:
                index = self.indexOf(delimiter, self.cursor)
                res = self.manageNewEnvironment(index, delimiter)
            except PatternNotFoundError as e:
                res = self.manageEndEnvironment(delimiter)
        else:
            raise EOFError()
        return res
