

from leetcode.allcode.competition.mypackage import *

class Graph1:

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


class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        def floyd2() -> List[int]:  # 有向图
            w = [[inf] * n for _ in range(n)]
            for x, y, wt in edges:
                w[x][y] = wt

            @cache
            def dfs(k: int, i: int, j: int) -> int:
                if k < 0:  # 递归边界
                    return w[i][j]
                return min(dfs(k - 1, i, j), dfs(k - 1, i, k) + dfs(k - 1, k, j))

            f = [[inf] * n for _ in range(n)]  # f[i][j] 表示 i 到 j 的最小距离
            for i in range(n):
                f[i][i] = 0
                for j in range(i + 1, n):
                    f[i][j] = dfs(n - 1, i, j)
                    f[j][i] = dfs(n - 1, j, i)

            return f
        self.f = floyd2()
        self.n = n


    def addEdge(self, edge: List[int]) -> None:
        # self.add(edges)
        x, y, w = edge
        for i in range(self.n):
            for j in range(i + 1, self.n):
                self.f[i][j] = min(self.f[i][j], self.f[i][x] + self.f[y][j] + w)
                self.f[i][j] = min(self.f[i][j], self.f[i][y] + self.f[x][j] + w)
                self.f[j][i] = self.f[i][j]


    def shortestPath(self, node1: int, node2: int) -> int:
        return self.f[node1][node2] if self.f[node1][node2] != inf else -1





so = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])
print(so.shortestPath(3, 2))
print(so.shortestPath(0, 3))




