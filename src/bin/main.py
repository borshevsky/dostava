import random
import curses
import time

from src.lib.car import Car
from src.lib.cargo import Stock
from src.lib.router import Router
from src.lib.world import World, Point, PointType
from src.lib.order import Order
from src.lib.solver import Solver

world_size = (40, 40)

world = World(*world_size)
router = Router(world.graph())

stocks = [
    Stock(random.randint(0, world_size[0] - 1), random.randint(0, world_size[1] - 1))
    for _ in range(5)
]
cars = [Car() for _ in range(15)]

for car in cars:
    world.add_car(car)

for stock in stocks:
    world.add_stock(stock)

orders = [
    Order(random.choice(stocks), random.choice(stocks))
    for _ in range(1000)
]

solver = Solver(world)

for order in orders:
    solver.add_order(order)


def ui(window):
    while True:
        window.clear()
        world.tick()
        solver.tick()
        window.addstr(0, 0, str(world))
        window.refresh()
        time.sleep(0.1)

curses.wrapper(ui)



