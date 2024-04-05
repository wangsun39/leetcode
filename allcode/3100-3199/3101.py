

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        v = 1
        ans = 1
        for i, x in enumerate(nums[1:], 1):
            if x != nums[i - 1]:
                v += 1
            else:
                v = 1
            ans += v
        return ans


so = Solution()
print(so.countAlternatingSubarrays(nums = [0,1,1,1]))
print(so.countAlternatingSubarrays(nums = [1,0,1,0]))




