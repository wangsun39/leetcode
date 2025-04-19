

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = sum(nums)
        return s - s // k * k


so = Solution()
print(so.minOperations())




