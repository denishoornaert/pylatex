import sys
from io import StringIO
import contextlib
import traceback

# Set up the pylatex specific functions
from src.session import SetUp
for function in SetUp.functions:
    exec(function)

class Interpreter():

    """docstring for Interpreter."""

    @staticmethod
    def execute(instructions):
        """
        (static public) Evaluates the python code given in parameter and return
        everything the code is supposed to print (Error messages included).
        """
        res = ""
        if(instructions != ""):
            with Interpreter.setUpIO() as s:
                try:
                    exec(instructions)
                    res = s.getvalue()
                except Exception as e:
                    res = str(e)
        return res

    @staticmethod
    @contextlib.contextmanager
    def setUpIO():
        """
        (static private) Captures the data output on the stdout.
        """
        old = sys.stdout
        stdout = StringIO()
        sys.stdout = stdout
        yield stdout
        sys.stdout = old
