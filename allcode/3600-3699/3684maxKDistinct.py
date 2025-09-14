

from leetcode.allcode.competition.mypackage import *

min = lambda a, b: b if b < a else a
max = lambda a, b: b if b > a else a

class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums = list(set(nums))
        nums.sort(reverse=True)
        return nums[:k]


so = Solution()
print(so.maxKDistinct())




