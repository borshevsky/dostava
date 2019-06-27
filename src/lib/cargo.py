from dataclasses import dataclass
from enum import Enum, auto


class Deck(Enum):
    SINGLE = auto(),
    DOUBLE = auto()


@dataclass
class Cargo(object):
    def __init__(self):
        self.drivers_count = 1
        self.ADR = False
        self.farma = False
        self.deck = Deck.SINGLE
        self.pallete = False

    drivers_count: int
    ADR: bool
    farma: bool
    deck: Deck
    pallete: bool


class Stock(object):
    def __init__(self, location):
        self._location = location

    @property
    def location(self):
        return self._location
