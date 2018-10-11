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

    def getSeperator(self, row=None):
        res = "\t\\hline\n"
        if(row != None):
            res += "" if(row==self.columnSize-1) else "\t "
        return res

    def getNextCharacters(self, index):
        return " \\\\ \n" if(index == self.rowSize-1) else " & "

    def getCellFiller(self, data, col, row=None):
        res = ""
        try:
            # TODO replace str() by __out__() ?
            res += str(data[col]) if(row == None) else str(data[row][col])
        except IndexError as e:
            res += " "
        res += self.getNextCharacters(col)
        return res

    def headerConstruction(self):
        res = ""
        if(self.header != None):
            if(self.sideColumn != None):
                res += " "+" & "
            for col in range(self.rowSize):
                res += self.getCellFiller(self.header, col)
            res += self.getSeperator()+"\t "
        return res

    def onelinerConstruction(self):
        res = ""
        for row in range(self.columnSize):
            res += str(self.array[row])
            res += " \\\\ \n"
            res += self.getSeperator(row)
        return res

    def tableConstruction(self):
        res = ""
        for row in range(self.columnSize):
            if(self.sideColumn != None):
                res += self.sideColumn[row]+" & "
            for col in range(self.rowSize):
                res += self.getCellFiller(self.array, col, row)
            res += self.getSeperator(row)
        return res

    def generateBody(self):
        """
        (private) Genrates the middle part of the table.
        """
        res  = self.headerConstruction()
        if(self.oneliner):
            res += self.onelinerConstruction()
        else:
            res += self.tableConstruction()
        return res

    def __out__(self):
        res  = self.generateHeader()
        res += self.generateBody()
        res += self.generateFooter()
        return res
