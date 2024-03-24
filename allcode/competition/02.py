

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minOperations(self, k: int) -> int:
        ans = inf
        if k == 1: return 0
        for i in range(2, k + 1):
            ans = min(ans, i - 1 + (k - 1) // i)

        return ans



so = Solution()
print(so.minOperations(7))
print(so.minOperations(122))
print(so.minOperations(11))
print(so.minOperations(1))




