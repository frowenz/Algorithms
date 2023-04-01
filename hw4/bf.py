
Dict = {
    0: 'a', 
    1: 'b', 
    2: 't', 
    3: 'c', 
    4: 'd', 
    5: 'e', 
    6: 's',
    7: 'f', 
    8: 'g'
}

class Graph:
    def __init__(self, vertices):
        self.V = vertices # No. of vertices
        self.graph = []
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(Dict[i], dist[i]))

    def BellmanFord(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0

        for c in range(self.V):
            print("Step", c)
            self.printArr(dist)
            print(" ")

            dist_temp = dist.copy()
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist_temp[v] = dist[u] + w

            dist = dist_temp.copy()

        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return

# 0: 'a', 
# 1: 'b', 
# 2: 't', 
# 3: 'c', 
# 4: 'd', 
# 5: 'e', 
# 6: 's',
# 7: 'f', 
# 8: 'g',

# Driver's code
if __name__ == '__main__':
    g = Graph(9)
    g.addEdge(0, 1, -12)

    g.addEdge(1, 2, 3)
    g.addEdge(1, 4, 4)

    g.addEdge(3, 1, -4)
    g.addEdge(3, 0, 6)

    g.addEdge(4, 3, 3)
    g.addEdge(4, 7, -3)
    g.addEdge(4, 2, -1)

    g.addEdge(5, 4, 1)
    g.addEdge(5, 2, -2)

    g.addEdge(6, 3, 8)
    g.addEdge(6, 4, 7)
    g.addEdge(6, 7, 5)

    g.addEdge(7, 8, -2)
    g.addEdge(7, 5, 3)

    g.addEdge(8, 5, 8)

    g.BellmanFord(6)
