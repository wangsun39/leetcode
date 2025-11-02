

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = sorted(abs(x) for x in nums)
        a, b = nums[-1], nums[-2]
        p = a * b
        c = 10 ** 5
        return p * c


so = Solution()
print(so.maxProduct())




