class DisjointElement(object):
    def __init__(self, elem):
        self.element = elem
        self.parent = elem


class DisjointSet(object):
    def __init__(self, elements):
        self.lookup = {}
        self.set = []
        for e in elements:
            de = DisjointElement(e)
            self.lookup[e] = de
            self.set.append(de)

    def find(self, e):
        pass

    def union(self, e1, e2):
        pass
