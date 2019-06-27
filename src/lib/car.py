from dataclasses import dataclass

from src.lib.cargo import Deck


class Car(object):
    drivers_count: int
    uk_allowed: bool
    deck: Deck
    ADR_alowed: bool
    pallete: bool
    farma_allowed: bool

    def __init__(self, location):
        self._route = None
        self._location = location
        self._route_position = None

        self.drivers_count = 1
        self.uk_allowed = True
        self.deck = Deck.SINGLE
        self.ADR_alowed = True
        self.pallete = True
        self.farma_allowed = True

    @property
    def free(self):
        return self._route is None

    @property
    def location(self):
        return self._location

    @property
    def route(self):
        return self._route

    @route.setter
    def route(self, value):
        assert self._route is None
        assert value[0] == self._location

        self._route = value

        if self._route is None:
            self._route_position = None

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
