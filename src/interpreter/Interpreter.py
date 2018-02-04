import sys
from io import StringIO
import contextlib
import traceback
import re

# Set up the pylatex specific functions
from src.session.Functions import *

class Interpreter():

    """docstring for Interpreter."""

    local = {}
    local.setdefault('out', out)

    @staticmethod
    def escapeCharactersManagement(string):
        # Replaces '\\' by '\\\\'
        string = re.sub(r'"(.*)\\\\(.*)"', r'"\1\\\\\\\\\2"', string)
        return string

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
                    instructions = Interpreter.escapeCharactersManagement(instructions)
                    exec(instructions, {}, Interpreter.local)
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
