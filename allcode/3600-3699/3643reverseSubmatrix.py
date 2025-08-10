

from leetcode.allcode.competition.mypackage import *

min = lambda a, b: b if b < a else a
max = lambda a, b: b if b > a else a

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        r, c = len(grid), len(grid[0])
        for i in range(x, x + k // 2):
            for j in range(y, y + k):
                grid[i][j], grid[i + k - 1][j] = grid[i + k - 1][j], grid[i][j]
        return grid



so = Solution()
print(so.reverseSubmatrix(grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], x = 1, y = 0, k = 3))
print(so.reverseSubmatrix(grid = [[3,4,2,3],[2,3,4,2]], x = 0, y = 2, k = 2))




