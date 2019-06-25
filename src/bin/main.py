import random
import curses
import time

from src.lib.car import Car
from src.lib.cargo import Stock
from src.lib.router import Router
from src.lib.world import World, Point, PointType
from src.lib.order import Order
from src.lib.solver import Solver

world_size = (10, 35)

world = World(*world_size)
router = Router(world.graph())

stocks = [Stock() for _ in range(3)]
cars = [Car() for _ in range(5)]

for car in cars:
    world.add_car(car)

for stock in stocks:
    world.add_stock(
        stock,
        random.randint(0, world_size[0] - 1),
        random.randint(0, world_size[1] - 1))


def ui(window):
    for i in range(100):
        window.clear()
        world.tick()
        window.addstr(0, 0, str(world))
        window.refresh()
        time.sleep(1)

route = router.route((0, 0), (world_size[0] - 1, world_size[1] - 1))
cars[0].route = route
print(route)
print(str(world))

curses.wrapper(ui)



