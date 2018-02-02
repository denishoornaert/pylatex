class TestConfiguration():

    """docstring for TestConfiguration."""

    latexTestFilePath = "test/assets/"

    pylatexExtension = ".ptex"

    @staticmethod
    def getCompletePath(filepath):
        res  = TestConfiguration.latexTestFilePath
        res += filepath
        return  res + TestConfiguration.pylatexExtension
