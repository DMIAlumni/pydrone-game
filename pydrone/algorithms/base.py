class BaseAlgorithm(object):
    """
    Algorithm interface
    """

    def evaluate(self, drone):
        raise NotImplementedError()
