from src.lib.router import Router


class Solver(object):
    def __init__(self, ground):
        self.ground = ground
        self.router = Router(ground)

    def add_order(self, order):
        pass

    def add_car(self, car):
        pass

    def update(self):
        pass