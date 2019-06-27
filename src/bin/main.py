import random
import curses
import time

from src.lib.car import Car
from src.lib.cargo import Stock, Cargo
from src.lib.world import World
from src.lib.order import Order
from src.lib.solver import Solver

world_size = (40, 70)
stocks_count = 10
cars_count = 30


def generate_world():
    world = World(*world_size)
    graph = world.graph()

    def free_cell():
        while True:
            i, j = random.randint(0, world_size[0] - 1), random.randint(0, world_size[1] - 1)
            if graph[i][j] == 1:
                return i, j


    for _ in range(stocks_count):
        world.add_stock(Stock(free_cell()))

    for i in (0, world_size[0] - 1):
        for j in (0, world_size[1] - 1):
            world.add_stock(Stock((i, j)))

    for _ in range(cars_count):
        world.add_car(Car(free_cell()))

    return world


def mutate(world, solver):
    wanna_make_order = random.random() > 0.5
    if wanna_make_order:
        solver.add_order(Order(random.choice(world.stocks), random.choice(world.stocks), Cargo()))


def main():
    world = generate_world()
    solver = Solver(world)

    def ui(window):
        while True:
            mutate(world, solver)

            for t in (world, solver):
                t.tick()

            window.addstr(1, 1, str(world))
            window.refresh()
            time.sleep(0.1)

    curses.wrapper(ui)


if __name__ == '__main__':
    main()
