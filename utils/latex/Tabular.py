class Tabular():

    """docstring for Tabular."""

    def __init__(self, array):
        if(type(array) == list):
            self.array = array
            self.oneliner = False
            self.header = None
            self.sideColumn = None
            self.rowSize = self.getMaxRowSize()
            self.columnSize = len(self.array)
        else:
            raise TypeError("Tabular only accepts array as parameter")

    def __str__(self):
        return self.array.__str__()

    def setHeader(self, header):
        self.header = header
        self.rowSize = max(self.rowSize, len(self.header))

    def setSideColumn(self, column):
        self.sideColumn = column
        self.columnSize = max(self.columnSize, len(self.sideColumn))

    def getMaxRowSize(self):
        """
        (private) Returns the highest row size and checks tath every element of
        the given array is also an array. If it is not the case, the result is 1
        """
        res = 1
        # all elements of the array are arrays
        self.oneliner = not all([type(elem) == list for elem in self.array])
        if(not self.oneliner):
            rowsSize = []
            if(self.header != None):
                rowsSize.append(len(self.header))
            for row in self.array:
                rowsSize.append(len(row))
            res = max(rowsSize)
        return res

    def generateHeader(self):
        """
        (private) Genrates the first part of the table.
        """
        nbColmun = self.rowSize+(self.sideColumn != None)
        return "\\begin{tabular}{|"+("c|"*nbColmun)+"}\n\t\\hline\n\t "

    def generateFooter(self):
        """
        (private) Genrates the last (and third part) of the table.
        """
        return "\\end{tabular}\n"

    def generateBody(self):
        """
        (private) Genrates the middle part of the table.
        """
        res = ""
        if(self.header != None):
            if(self.sideColumn != None):
                res += " "+" & "
            for col in range(self.rowSize):
                try:
                    res += str(self.header[col])
                except IndexError as e:
                    res += " "
                res += " \\\\ \n" if(col==self.rowSize-1) else " & "
            res += "\t\\hline\n\t "
        for row in range(self.columnSize):
            if(self.oneliner):
                res += str(self.array[row])
                res += " \\\\ \n"
            else:
                if(self.sideColumn != None):
                    res += self.sideColumn[row]+" & "
                for col in range(self.rowSize):
                    try:
                        res += str(self.array[row][col])
                    except IndexError as e:
                        res += " "
                    res += " \\\\ \n" if(col==self.rowSize-1) else " & "
            res += "\t\\hline\n"
            res += "" if(row==self.columnSize-1) else "\t "
        return res

    def __latex__(self):
        res  = self.generateHeader()
        res += self.generateBody()
        res += self.generateFooter()
        return res
