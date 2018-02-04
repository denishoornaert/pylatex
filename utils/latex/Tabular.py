class Tabular():

    """docstring for Tabular."""

    def __init__(self, array):
        if(type(array) == list):
            self.array = array
            self.rowSize = self.getMaxRowSize()
            self.columnSize = len(self.array)
        else:
            raise TypeError("Tabular only accepts array as parameter")

    def __str__(self):
        return self.array.__str__()

    def getMaxRowSize(self):
        """
        (private) Returns the highest row size and checks tath every element of
        the given array is also an array. If it is not the case, the result is 1
        """
        res = 1
        if(all([type(elem) == list for elem in self.array])):
            rowsSize = []
            for row in self.array:
                rowsSize.append(len(row))
            res = max(rowsSize)
        return res

    def generateHeader(self):
        return "\\begin{tabular}{|"+("c|"*self.rowSize)+"}\n\t\\hline\n\t "

    def generateFooter(self):
        return "\\end{tabular}\n"

    def generateBody(self):
        res = ""
        for row in range(self.rowSize):
            for col in range(self.columnSize):
                try:
                    res += str(self.array[row][col])
                except IndexError as e:
                    res += " "
                res += " \\\\ \n" if(col==self.rowSize-1) else " & "
            res += "\t\\hline\n"
            res += "" if(row==len(self.array)-1) else "\t "
        return res

    def __latex__(self):
        res  = self.generateHeader()
        res += self.generateBody()
        res += self.generateFooter()
        return res
