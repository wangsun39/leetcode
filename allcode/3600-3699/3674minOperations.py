

from leetcode.allcode.competition.mypackage import *

min = lambda a, b: b if b < a else a
max = lambda a, b: b if b > a else a

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if all(x = nums[0] for x in nums):
            return 0
        return 1



so = Solution()
print(so.minOperations())




