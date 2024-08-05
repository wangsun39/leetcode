

from leetcode.allcode.competition.mypackage import *

class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid[:]
        self.r, self.c = len(grid), len(grid[0])
        self.d = {}
        for i in range(self.r):
            for j in range(self.c):
                self.d[grid[i][j]] = [i, j]



    def adjacentSum(self, value: int) -> int:
        ans = 0
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        i, j = self.d[value]
        for u, v in dir:
            x, y = i + u, j + v
            if 0 <= x < self.r and 0 <= y < self.c:
                ans += self.grid[x][y]
        return ans


    def diagonalSum(self, value: int) -> int:
        dir = [[-1, -1], [1, 1], [-1, 1], [1, -1]]
        i, j = self.d[value]
        ans = 0
        for u, v in dir:
            x, y = i + u, j + v
            if 0 <= x < self.r and 0 <= y < self.c:
                ans += self.grid[x][y]
        return ans


so = Solution()
print(so.removeDigit())




