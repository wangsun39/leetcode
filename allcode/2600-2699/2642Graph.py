

from leetcode.allcode.competition.mypackage import *

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.g = defaultdict(list)
        for x, y, c in edges:
            self.g[x].append([y, c])


    def addEdge(self, edge: List[int]) -> None:
        x, y, c = edge
        self.g[x].append([y, c])


    def shortestPath(self, node1: int, node2: int) -> int:
        vis = [0] * self.n
        dq = deque([[node1, 0]])
        vis[node1] = 1
        dis = [inf] * self.n
        dis[node1] = 0
        while dq:
            x, d = dq.popleft()
            for y, c in self.g[x]:
                if dis[y] > d + c:
                    dis[y] = d + c
                    dq.append([y, d + c])
        if dis[node2] < inf:
            return dis[node2]
        return -1



so = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])
print(so.shortestPath(3, 2))
print(so.shortestPath(0, 3))




