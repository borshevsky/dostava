import random
import curses
import time

from src.lib.car import Car
from src.lib.cargo import Cargo
from src.lib.stock import Stock
from src.lib.router import Router
from src.lib.world import World, PointType
from src.lib.order import Order
from src.lib.solver import Solver

world_size = (40, 70)
stocks_count = 10
cars_count = 30


def generate_world():
    world = World(*world_size)
    graph = world.graph()
    router = Router(graph)

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
        world.add_car(Car(free_cell(), router))

    return world, router


def mutate(world, solver, t):
    wanna_make_order = random.random() > 0.8
    if wanna_make_order:
        solver.add_order(Order(
            random.choice(world.stocks), random.choice(world.stocks),
            Cargo(),
            t + random.randint(5, 100)))


def draw_orders(window, orders):
    y = world_size[1] * 2 + 2
    window.addstr(1, y, "Orders:")

    row = 2

    def print_order(order):
        nonlocal row
        window.addstr(row, y, f'    {order.source.location} -> {order.destination.location}')
        row += 1

    def print_orders(type, orders):
        nonlocal row
        window.addstr(row, y, f'  {type}:')
        row  += 1

        for o in orders[-10:]:
            print_order(o)

    for t, o in zip(('P', 'S', 'F'), orders):
        print_orders(t, o)

def main():
    world, router = generate_world()
    solver = Solver(world, router)

    def ui(window):
        tm = 0
        while True:
            mutate(world, solver, tm)

            for t in (world, solver):
                t.tick(tm)

            window.addstr(1, 1, str(world))
            draw_orders(window, solver.orders)
            window.refresh()
            time.sleep(0.1)

    curses.wrapper(ui)


if __name__ == '__main__':
    main()
