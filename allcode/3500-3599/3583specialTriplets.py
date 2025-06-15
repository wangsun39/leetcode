

from leetcode.allcode.competition.mypackage import *

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        counter = Counter()
        left = [0] * n
        right = [0] * n
        for i, x in enumerate(nums):
            left[i] = counter[x * 2]
            counter[x] += 1
        counter = Counter()
        for i in range(n - 1, -1, -1):
            x = nums[i]
            right[i] = counter[x * 2]
            counter[x] += 1
        ans = 0
        for i in range(n):
            ans += (left[i] * right[i] % MOD)
        return ans


so = Solution()
print(so.specialTriplets([6,3,6]))




