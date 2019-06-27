class Stock(object):
    def __init__(self, location):
        self._location = location

    @property
    def location(self):
        return self._location