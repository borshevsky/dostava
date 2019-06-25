import random
from enum import Enum, auto

class PointType(Enum):
    ROAD = auto(),
    FOREST = auto(),
    STOCK = auto()

    def __str__(self):
        if self == PointType.ROAD:
           return '🛣 '

        if self == PointType.FOREST:
            return '🌳'


class Point(object):
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

    def __str__(self):
        return '{}'.format(self.type)

    def __repr__(self):
        return str(self)


class World(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.ground = [
            [Point(i, j, random.choice([PointType.ROAD] * 4 + [PointType.FOREST])) for i in range(width)]
            for j in range(height)
        ]

        self._cars = set()
        self._stocks = set()

    @property
    def cars(self):
        return self._cars

    @property
    def stocks(self):
        return self._stocks

    def add_stock(self, stock):
        self.stocks.add(stock)

    def add_car(self, car):
        self.cars.add(car)

    def tick(self):
        for car in self.cars:
            car.tick()

    def graph(self):
        return [
            [0 if p.type == PointType.FOREST else 1 for p in self.ground[i]]
            for i in range(self.height)
        ]

    def __str__(self):
        chars = [
            [str(p) for p in self.ground[i]]
            for i in range(self.height)
        ]

        for car in self.cars:
            chars[car.location[0]][car.location[1]] = '🚛'

        for stock in self.stocks:
            chars[stock.location[0]][stock.location[1]] = '🏪 '

        return '\n'.join([
            ''.join(chars[i][j] for j in range(self.width))
           for i in range(self.height)
        ])
