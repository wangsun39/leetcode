

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        hp = []
        r, c = len(values), len(values[0])
        p = [c - 1] * r
        for i in range(r):
            heappush(hp, [values[i][p[i]], i])
            p[i] -= 1
        ans = 0
        for d in range(1, c * r + 1):
            v, row = heappop(hp)
            ans += v * d
            if p[row] >= 0:
                heappush(hp, [values[row][p[row]], row])
                p[row] -= 1

        return ans



so = Solution()
print(so.maxSpending(values = [[8,5,2],[6,4,1],[9,7,3]]))
print(so.maxSpending(values = [[10,8,6,4,2],[9,7,5,3,2]]))




