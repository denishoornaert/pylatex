import os
from src.fileController import FileController
from src.lexer import Parser

class Generator():

    """docstring for Generator."""

    @staticmethod
    def generates(pyLaTeXFile):
        # Set data
        parser  = Parser(pyLaTeXFile)
        data = ""
        # Main part of the body
        try:
            while(True):
                res = parser.lex()
                data += res[1]
        except EOFError as e:
            # Do nothing as the end of the file as been reached
            pass
        else:
            raise Exception
        # End of the process : write the generated LaTeX file
        destFile = os.path.splitext(pyLaTeXFile)[0]+".tex"
        FileController.write(data, destFile)
