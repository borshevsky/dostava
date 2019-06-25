class Order(object):
    def __init__(self, source, dest):
        self._source = source
        self._destination = dest

    @property
    def source(self):
        return self._source

    @property
    def destination(self):
        return self._destination
