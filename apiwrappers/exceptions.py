__author__ = 'rwdavis513'

class InitializationException(Exception):
    def __init__(self):
        msg = 'Function not initialized correctly.'
        super(InitializationException, self).__init__(msg)

