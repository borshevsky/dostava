import random
import curses
import time

from src.lib.car import Car
from src.lib.cargo import Stock
from src.lib.router import Router
from src.lib.world import World, Point, PointType
from src.lib.order import Order
from src.lib.solver import Solver

world_size = (40, 70)

world = World(*world_size)

stocks = [
    Stock(random.randint(0, world_size[0] - 1), random.randint(0, world_size[1] - 1))
    for _ in range(10)
]

for i in (0, world_size[0] - 1):
    for j in (0, world_size[1] - 1):
        stocks.append(Stock(i, j))

cars = [Car() for _ in range(30)]

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
        world.tick()
        solver.tick()
        window.addstr(1, 1, str(world))
        window.refresh()
        time.sleep(0.1)

curses.wrapper(ui)



