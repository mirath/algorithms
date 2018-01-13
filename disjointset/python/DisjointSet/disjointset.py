class DisjointElement(object):
    def __init__(self, elem):
        self.element = elem
        self.parent = self


class DisjointSet(object):
    def __init__(self, elements):
        self.lookup = {}
        self.set = []
        for e in elements:
            de = DisjointElement(e)
            self.lookup[e] = de
            self.set.append(de)

    def find(self, e):
        de = self.lookup[e]
        return self.__find(de)

    def __find(self, de):
        # Missing path compression
        if de.parent != de:
            return self.__find(de.parent)
        return de.element

    def union(self, e1, e2):
        de1 = self.lookup[e1]
        de2 = self.lookup[e2]

        # Missing union by rank
        de1.parent = de2
