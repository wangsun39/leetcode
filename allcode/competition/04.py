

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        if x > y:
            x, y = y, x
        ans = [0] * (n + 1)
        if x == y or x + 1 == y:
            for k in range(1, n + 1):
                ans[k] = (n - k) * 2
        else:
            for k in range(1, n + 1):
                p1 = max(0, n - k - x)
                p2 = min(x, n - (y - x + 1) - k)
                p2 = max(0, p2)
                ans[k] = (p1 + p2) * 2

        ans.pop(0)
        return ans


so = Solution()
print(so.countOfPairs(n = 5, x = 1, y = 5))
print(so.countOfPairs(n = 3, x = 1, y = 3))
print(so.countOfPairs(n = 5, x = 2, y = 4))
print(so.countOfPairs(n = 4, x = 1, y = 1))




