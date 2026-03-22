

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if all(x & 1 for x in nums1) or all((x & 1) == 0 for x in nums1):
            return True
        mno = min(x for x in nums1 if x & 1)
        return all(x > mno for x in nums1 if (x & 1) == 0)

so = Solution()
print(so.removeDigit())




