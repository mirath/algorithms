class DisjointElement(object):
    def __init__(self, elem):
        self.element = elem
        self.parent = self
        self.rank = 0


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
        return self.__find(de, []).element

    def __find(self, de, path):
        if de.parent != de:
            path.append(de)
            return self.__find(de.parent, path)

        for e in path:
            e.parent = de

        return de

    def union(self, e1, e2):
        de1 = self.__find(self.lookup[e1], [])
        de2 = self.__find(self.lookup[e2], [])

        if de1.rank > de2.rank:
            de2.parent = de1
        elif de1.rank < de2.rank:
            de1.parent = de2
        else:
            de2.parent = de1
            de1.rank += 1
