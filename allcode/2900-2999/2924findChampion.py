

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        fa = [-1] * n
        for x, y in edges:
            fa[y] = x
        cham = [i for i in range(n) if fa[i] == -1]
        if len(cham) == 1:
            return cham[0]
        return -1


so = Solution()
print(so.findChampion(n = 3, edges = [[0,1],[1,2]]))
print(so.findChampion(n = 4, edges = [[0,2],[1,3],[1,2]]))




