

from leetcode.allcode.competition.mypackage import *

min = lambda a, b: b if b < a else a
max = lambda a, b: b if b > a else a

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        for i, x in enumerate(nums):
            if x != i:
                return i
        return 0


so = Solution()
print(so.sortPermutation([0,3,2,1]))




