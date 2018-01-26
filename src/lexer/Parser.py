import sys
sys.path.append('struct/')
sys.path.append('error/')

from Environment import Environment
from UnclosedEnvironmentError import UnclosedEnvironmentError

class Parser():

    """docstring for Parser."""

    def __init__(self, filename):
        self.content = ""
        self.readFile(filename)
        self.currentEnvironment = Environment.latex
        self.cursor = 0

    def readFile(self, filename):
        """
        Method that loads the content of the file given in parameter into
        the attribut 'content' of the object Parser.
        """
        f = open(filename)
        self.content = f.read().strip()
        f.close()

    def isStateLatex():
        """
        Returns whether the previous environment was LaTex or Python.
        """
        return self.currentEnvironment == Environment.latex

    def lex(self):
        """
        Returns a tuple contaning the detected environment and its content. Will
        eventually raise an error when reaching the end of the file.
        """
        # TODO differenciate the moment where there is no more '<?' or '?>'
        res = None
        delimiter = "<?" if(self.isStateLatex()) else "?>"
        index = self.content.find(delimiter)
        if(index >= 0):
            res = (self.currentEnvironment, self.content[cursor:index])
            self.cursor = index+len(delimiter)
            self.currentEnvironment = Environment.python if(isStateLatex) else Environment.python
        elif(delimeter == "<?"): # and index == -1 : the remaining of the file only contains latex environment
            res = (Environment.latex, self.content[cursor:])
            self.currentEnvironment = Environment.latex
            self.cursor = len(self.content)-1
        else: # delimeter == "?>" and index == -1 : the python environment is not closed
            raise UnclosedEnvironmentError("The Python environment openned at (x, y) is not closed.")
        return res
