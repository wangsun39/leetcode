
from leetcode.allcode.competition.mypackage import *


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        res = [[r.count(1), -i] for i, r in enumerate(mat)]
        res.sort()
        # print(res)
        return [-res[-1][1], res[-1][0]]



so = Solution()
print(so.rowAndMaximumOnes([[0,1],[1,0]]))
print(so.rowAndMaximumOnes([[0,0,0],[0,1,1]]))
print(so.rowAndMaximumOnes([[0,0],[1,1],[0,0]]))




