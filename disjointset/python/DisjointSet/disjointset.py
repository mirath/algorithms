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
        return self.__find(de, [])

    def __find(self, de, path):
        if de.parent != de:
            path.append(de)
            return self.__find(de.parent, path)

        for e in path:
            e.parent = de

        return de.element

    def union(self, e1, e2):
        de1 = self.lookup[e1]
        de2 = self.lookup[e2]

        # Missing union by rank
        de1.parent = de2
