

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i in range(n):
            flg = False
            for j in range(n):
                if i == j: continue
                if grid[i][j] == 0:
                    flg = True
                    break
            if not flg:
                return i



so = Solution()
print(so.findChampion([[0,1],[0,0]]))
print(so.findChampion([[0,0,1],[1,0,1],[0,0,0]]))




