

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        q = (k + 1 + (n - 2)) // (n - 1)
        r = (k + 1) % (n - 1)
        if q & 1 == 1:
            if r:
                return r - 1
            return n - 2
        return n - r



so = Solution()
print(so.numberOfChild(n = 3, k = 5))
print(so.numberOfChild(n = 5, k = 6))
print(so.numberOfChild(n = 4, k = 2))




