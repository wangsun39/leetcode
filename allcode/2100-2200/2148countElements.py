

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) > 1:
            return len(nums) - 2
        return 0



so = Solution()
print(so.countElements())




