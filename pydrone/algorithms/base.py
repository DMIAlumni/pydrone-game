"""
Algorithm interface
"""
class BaseAlgorithm(object):

    def evaluate(self):
        raise NotImplementedError()
