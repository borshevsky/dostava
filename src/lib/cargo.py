class Cargo(object):
    @property
    def properties(self):
        return {
            'need_drivers': None,
            'ADR': True,
            'farma': False,
            'deck': 'double',
            'pallete': False,
        }


class Schedule(object):
    pass


class Customer(object):
    pass


class Stock(object):
    def __init__(self, x, y):
        self._location = (x, y)

    @property
    def location(self):
        return self._location
