

from leetcode.allcode.competition.mypackage import *

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        diag = [[x * x + y * y, x, y] for x, y in dimensions]
        diag.sort(key=lambda x: [x[0], x[1] * x[2]], reverse=True)
        return diag[0][1] * diag[0][2]


so = Solution()
print(so.areaOfMaxDiagonal(dimensions = [[9,3],[8,6]]))
print(so.areaOfMaxDiagonal(dimensions = [[3,4],[4,3]]))
print(so.areaOfMaxDiagonal(dimensions = [[9,3],[8,6]]))




