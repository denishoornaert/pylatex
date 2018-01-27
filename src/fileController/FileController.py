class FileController():

    """docstring for FileController."""

    @staticmethod
    def read(filename):
        """
        (public) Method that simply returns the content of the file given in
        parameter.
        """
        f = open(filename)
        res = f.read().strip()
        f.close()
        return res

    @staticmethod
    def write(filename, data):
        """
        (public) Method that simply writes the data given in parameter into the
        file given in parameter.
        """
        f = open(filename)
        f.write(data)
        f.close()
