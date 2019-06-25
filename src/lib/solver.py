from src.lib.router import Router


class Solver(object):
    def __init__(self, world):
        self._world = world
        self._router = Router(world.graph())
        self._scheduled_orders = []

    def add_order(self, order):
        try:
            free_car = next(car for car in self._world.cars if car.free)
            route = self._router.route(free_car.location, order.source.location)
            route += self._router.route(order.source.location, order.destination.location)
            free_car.route = route

        except StopIteration:
            self._scheduled_orders.append(order)


    def tick(self):
        if len(self._scheduled_orders) == 0:
            return

        try:
            free_car = next(car for car in self._world.cars if car.free)
            order = self._scheduled_orders.pop(0)

            route = self._router.route(free_car.location, order.source.location)
            route += self._router.route(order.source.location, order.destination.location)
            free_car.route = route

        except StopIteration:
            pass

    def add_car(self, car):
        pass

    def update(self):
        pass