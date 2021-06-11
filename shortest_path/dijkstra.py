import numpy as np


class Vertex:
    adj = []
    weight = []
    label = 'default'
    dist = np.inf
    pred = None
    def add(self, v, w):
        adj.append(v)
        weight.append(w)


def relax(u, v):
    if v.dist > u.dist + u.weight[u.adj.index(v)]:
        v.dist = u.dist + u.weight[u.adj.index(v)]
        v.pred = u


def extract_min(t):
    m = t[0]
    for v in t:
        if v.dist < m.dist:
            m = v
    return t.pop(t.index(m))


def dijkstra(v0, graph):
    v0.dist = 0
    q = graph[:]
    while len(q) > 0:
        v = extract_min(q)
        for u in v.adj:
            relax(v, u)


def print_path(v):
    print(v.label, end='<-')
    while v.dist != 0:
        v = v.pred
        print(v.label, end='<-')


def main():
    v0 = Vertex()
    a = Vertex()
    b = Vertex()
    c = Vertex()
    d = Vertex()
    v0.label = 'v0'
    a.label = 'a'
    b.label = 'b'
    c.label = 'c'
    d.label = 'd'
    v0.adj = [a, b, c, d]
    v0.weight = [12, 7, 8, 1]
    a.adj = [v0, b, c, d]
    a.weight = [12, 2, 98, 37]
    b.adj = [v0, a, c]
    b.weight = [7, 2, 2]
    c.adj = [v0, a, b, d]
    c.weight = [8, 98, 2, 4]
    d.adj = [v0, a, c]
    d.weight = [1, 37, 4]
    graph = [v0, a, b, c, d]
    dijkstra(v0, graph)
    for v in graph:
        print(v.label, v.dist)
    for v in graph:
        print_path(v)
        print()


if __name__ == '__main__':
    main()
