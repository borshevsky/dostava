class Car(object):
    def __init__(self):
        self._route = None
        self._location = (0, 0)
        self._route_position = None

    @property
    def properties(self):
        return {
            'drivers_count': 1,
            'uk_allowed': True,
            'deck': 'single',
            'ADR': True,  # Опасные грузы,
            'pallete': True,
            'test': False,
            'farma_allowed': False,
        }

    @property
    def free(self):
        return self._route is None

    def tick(self):
        if self._route is None:
            return

        if self._route_position is None:
            self._route_position = 0
            self._location = self._route[0]
            return

        if self._route_position == len(self._route) - 1:
            self._route_position = None
            self._route = None
            return

        self._route_position += 1
        self._location = self._route[self._route_position]

    @property
    def speed(self):
        return 1

    @property
    def location(self):
        return self._location

    @property
    def route(self):
        return self._route

    def schedule_routes(self, route):
        self.scheduled_routes.append(route)

    @route.setter
    def route(self, value):
        self._route = value

        if self._route is None:
            self._route_position = None

    @staticmethod
    def random():
        pass
