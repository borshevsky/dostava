class Order(object):
    def __init__(self, fr, dest, loading_time, unloading_time, cargo):
        self.fr = fr
        self.destination = dest

        self.loading_time = loading_time
        self.unloading_time = unloading_time

        self.cargo = cargo

    @staticmethod
    def random():
        pass