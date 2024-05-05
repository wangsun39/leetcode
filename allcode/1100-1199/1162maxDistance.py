

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        n = len(grid)
        vis = [[0] * n for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append([i, j])
                    vis[i][j] = 1
        if len(q) in(n * n, 0): return -1
        d = 0
        while q:
            q2 = deque()
            while q:
                x, y = q.popleft()
                for x0, y0 in dir:
                    u, v = x + x0, y + y0
                    if 0 <= u < n and 0 <= v < n and vis[u][v] == 0:
                        q2.append([u, v])
                        vis[u][v] = 1
            if not q2:
                return d
            q = q2
            d += 1





so = Solution()
print(so.maxDistance(grid = [[1,1],[1,1]]))
print(so.maxDistance(grid = [[1,0,1],[0,0,0],[1,0,1]]))
print(so.maxDistance(grid = [[1,0,0],[0,0,0],[0,0,0]]))




