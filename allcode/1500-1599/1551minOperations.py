
from leetcode.allcode.competition.mypackage import *

class Solution:
    def minOperations(self, n: int) -> int:
        arr = range(1, 2 * (n - 1) + 1, 2)

        ans = 0
        for i in range(n // 2):
            ans += (n - arr[i])
        return ans


so = Solution()
print(so.minOperations(6))
print(so.minOperations(3))




