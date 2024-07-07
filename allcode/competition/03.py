

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])
        sx = [[] for _ in range(r)]
        sy = [[] for _ in range(r)]
        for i in range(r):
            if grid[i][0] == 'X':
                sx[i].append(1)
                sy[i].append(0)
            elif grid[i][0] == 'Y':
                sx[i].append(0)
                sy[i].append(1)
            else:
                sx[i].append(0)
                sy[i].append(0)
            for j in range(1, c):
                if grid[i][j] == 'X':
                    sx[i].append(sx[i][-1] + 1)
                    sy[i].append(sy[i][-1])
                elif grid[i][j] == 'Y':
                    sx[i].append(sx[i][-1])
                    sy[i].append(sy[i][-1] + 1)
                else:
                    sx[i].append(sx[i][-1])
                    sy[i].append(sy[i][-1])
        ssx = [0] * c
        ssy = [0] * c
        ans = 0
        for i in range(r):
            for j in range(c):
                ssx[j] += sx[i][j]
                ssy[j] += sy[i][j]
                if ssx[j] == ssy[j] != 0:
                    ans += 1
        return ans


so = Solution()
print(so.numberOfSubmatrices(grid = [["X","Y","."],["Y",".","."]]))
print(so.numberOfSubmatrices(grid = [["X","X"],["X","Y"]]))
print(so.numberOfSubmatrices(grid = [[".","."],[".","."]]))




