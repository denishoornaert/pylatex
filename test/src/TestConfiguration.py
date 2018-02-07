class TestConfiguration():

    """docstring for TestConfiguration."""

    latexTestFilePath = "test/src/assets/"

    pylatexExtension = ".ptex"

    @staticmethod
    def getCompletePath(filepath):
        res  = TestConfiguration.latexTestFilePath
        res += filepath
        return  res + TestConfiguration.pylatexExtension
