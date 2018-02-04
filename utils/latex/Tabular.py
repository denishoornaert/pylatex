class Tabular():

    """docstring for Tabular."""

    def __init__(self, array):
        if(type(array) == list)
            self.array = array
            self.rowSize = self.getMaxRowSize()
            self.columnSize = len(self.array)
        else:
            raise TypeError("Tabular only accepts array of arrays as parameter")

    def __str__(self):
        return self.array.__str__()

    def getMaxRowSize(self):
        """
        (private) Returns the highest row size and checks taht every element of
        the given array is also an array.
        """
        rowsSize = []
        for row in self.array:
            if(type(row) == list):
                rowsSize.append(len(row))
            else:
                raise TypeError("Tabular only accepts array of arrays as parameter")
        return max(rowsSize)

    def generateHeader(self):
        return "\\begin{tabular}{|"+("c|"*self.rowSize)+"}\n\t\\hline\n"

    def generateFooter(self):
        return "\\end{tabular}\n"

    def generateBody(self):
        res = ""
        for row in range(self.rowSize):
            for col in range(len(self.array[row])):
                try:
                    res += self.array[row][col]
                except IndexError as e:
                    res += " "
                res += " \\\\ \n" if(col==len(row)-1) else " & "
            res += "\\hline\n"
        return res

    def __latex__(self):
        res  = self.generateHeader()
        res += self.generateBody()
        res += self.generateFooter()
        return res
