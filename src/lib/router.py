from heapdict import heapdict

class Route(object):
    pass



class Router(object):
    def __init__(self, graph):
        self.graph = graph
        self.h = len(graph)
        self.w = len(graph[0])

    def route(self, a, b):
        preds = dict()
        weights = dict()
        edges = heapdict()
        edges[a] = 0

        while len(edges) > 0:
            edge, w = edges.popitem()
            print(edge, w)
            if edge == b:
                return self.make_path(a, b, preds)

            for n in self.neighbors(edge[0], edge[1]):
                if n not in weights or weights[n] > w + 1:
                    edges[n] = w + 1
                    weights[n] = w + 1
                    preds[n] = edge

        print('no route')

    @staticmethod
    def make_path(a, b, preds):
        ret = []
        print(a, b)
        while b != a:
            print('add ', b)
            ret.append(b)
            b = preds[b]
        ret.append(a)

        return list(reversed(ret))

    def neighbors(self, x, y):
        ret = (
            (x + dx, y + dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1)
            if abs(dx + dy) == 1 and 0 <= x + dx < self.h and 0 <= y + dy < self.w and self.graph[x + dx][y + dy] == 1
        )
        return ret






