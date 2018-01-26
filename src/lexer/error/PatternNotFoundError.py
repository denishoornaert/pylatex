class PatternNotFoundError(Exception):

    """docstring for PatternNotFoundError."""

    def __init__(self, value):
        super(Exception, self).__init__()
        self.value = value

    def __str__(self):
        return repr(self.value)
