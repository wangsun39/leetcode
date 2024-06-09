

from leetcode.allcode.competition.mypackage import *

class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        nums = [1] * n
        for i in range(k):
            for j in range(1, n):
                nums[j] += nums[j - 1]
                nums[j] %= MOD
        return nums[-1]


so = Solution()
print(so.valueAfterKSeconds(n = 4, k = 5))
print(so.valueAfterKSeconds(n = 5, k = 3))




