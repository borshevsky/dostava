import random
from enum import Enum, auto

from src.lib.car import Car
from src.lib.stock import Stock


class PointType(Enum):
    ROAD = auto(),
    FOREST = auto(),
    STOCK = auto()

    def __str__(self):
        if self == PointType.ROAD:
           return '  '

        if self == PointType.FOREST:
            return '🌳'


class Point(object):
    def __init__(self, x: float, y: float, type: PointType):
        self.x = x
        self.y = y
        self.type = type

    def __str__(self):
        return '{}'.format(self.type)

    def __repr__(self):
        return str(self)


class World(object):
    def __init__(self, height: int, width: int):
        self._height = height
        self._width = width
        self._ground = [
            [random.choice([PointType.ROAD] * 8 + [PointType.ROAD]) for _ in range(width)]
            for _ in range(height)
        ]

        self._cars = list()
        self._stocks = list()

    @property
    def cars(self):
        return self._cars

    @property
    def stocks(self):
        return self._stocks

    def add_stock(self, stock: Stock):
        self._stocks.append(stock)

    def add_car(self, car: Car):
        self._cars.append(car)

    def tick(self, time):
        for car in self._cars:
            car.tick()

    def graph(self):
        return [
            [0 if p == PointType.FOREST else 1 for p in row]
            for row in self._ground
        ]

    def __str__(self):
        chars = [
            [str(p) for p in row]
            for row in self._ground
        ]

        for car in self.cars:
            chars[car.location[0]][car.location[1]] = '🚛'

        for stock in self.stocks:
            chars[stock.location[0]][stock.location[1]] = '🏪'

        return '\n'.join(
            ''.join(c for c in row)
            for row in chars)
