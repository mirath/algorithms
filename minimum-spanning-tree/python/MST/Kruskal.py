from DisjointSet.disjointset import DisjointSet

class Kruskal(object):
    def __init__(self, edges):
        ''' The edges are of the form (a, b, w), where `a` and `b`
        are the nodes, and `w` is the weight'''

        self.edges = edges
        self.mst = [] # Here we will place the MST

    def run(self):
        elements = set()
        for e in self.edges:
            elements.add(e[0])
            elements.add(e[1])

        djs = DisjointSet(elements)

        self.edges = sorted(self.edges, key=lambda e: e[2])
        for e in self.edges:

            # Get the nodes
            a = e[0]
            b = e[1]

            # Find out in which set is each node
            s1 = djs.find(a)
            s2 = djs.find(b)

            # If they are not in the same set, add it to the MST and join the sets
            if s1 != s2:
                self.mst.append(e)
                djs.union(s1, s2)

        return self.mst
