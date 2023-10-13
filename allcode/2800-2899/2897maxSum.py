

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        bits = [0] * 32  # bits[i] 表示第i位为1的数的个数
        for x in nums:
            i = 0
            while x:
                if x & 1:
                    bits[i] += 1
                x >>= 1
                i += 1
        ans = 0
        for i in range(k):
            x = 0
            for j in range(32):
                if bits[j]:
                    x |= (1 << j)
                    bits[j] -= 1
            ans += x * x
            ans %= MOD
        return ans


so = Solution()
print(so.maxSum(nums = [2,6,5,8], k = 2))
print(so.maxSum(nums = [4,5,4,7], k = 3))




