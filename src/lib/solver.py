from heapq import heappush, heappop

from src.lib.order import Order
from src.lib.router import Router
from src.lib.world import World


class Solver(object):
    def __init__(self, world: World, router: Router):
        self._world = world
        self._router = router

        self._scheduled_orders = []
        self._performing_orders = []
        self._failed_orders = []

        self._current_time = 0

    @property
    def orders(self):
        return self._performing_orders, self._scheduled_orders, self._failed_orders

    def add_order(self, order: Order):
        heappush(self._scheduled_orders, order)
        self.schedule()

    def tick(self, time):
        self._current_time = time
        self.schedule()

    def find_fastest_car_for_order(self, order):
        need_to_be_free_in = order.loading_time - self._current_time
        fastest_car = (None, None, None)

        for car in self._world.cars:
            if car.busy_duration() > need_to_be_free_in:
                continue

            route_from_finish_point_to_stock = self._router.route(car.finish_point(), order.source.location)
            time_from_finish_point_to_stock = len(route_from_finish_point_to_stock)
            time_from_now_to_stock = car.busy_duration() + time_from_finish_point_to_stock

            if  time_from_now_to_stock > need_to_be_free_in:
                continue

            if fastest_car[1] is None or fastest_car[1] > time_from_now_to_stock:
                fastest_car = (car, time_from_now_to_stock, route_from_finish_point_to_stock)
                continue

        return fastest_car[0], fastest_car[2]

    def schedule(self):
        for _ in range(10):
            if not self._scheduled_orders:
                return

            order = heappop(self._scheduled_orders)

            if order.loading_time < self._current_time:
                self._failed_orders.append(order)
                continue

            fastest_car, proposed_route_to_source = self.find_fastest_car_for_order(order)
            if fastest_car is None:
                self._failed_orders.append(order)
                continue

            fastest_car.add_route(proposed_route_to_source)
            fastest_car.add_route(self._router.route(order.source.location, order.destination.location))

            self._performing_orders.append(order)
