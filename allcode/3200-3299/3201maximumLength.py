

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd = even = 0
        for x in nums:
            if x & 1:
                odd = max(odd, even + 1)
            else:
                even = max(even, odd + 1)
        nodd = sum(1 for x in nums if x & 1)
        return max(odd, even, nodd, len(nums) - nodd, 2)


so = Solution()
print(so.maximumLength([4,2,6]))
print(so.maximumLength([1,2,3,4]))
print(so.maximumLength([1,2,1,1,2,1,2]))
print(so.maximumLength([1,3]))




