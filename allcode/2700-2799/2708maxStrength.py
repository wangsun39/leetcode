

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        neg = sorted(x for x in nums if x < 0)
        pos = [x for x in nums if x > 0]
        if len(pos) == 0 and len(neg) <= 1:
            if len(neg) == 0:
                return 0
            return neg[0] if 0 not in nums else 0
        ans = 1
        for x in pos:
            ans *= x
        if len(neg) & 1:
            for x in neg[:-1]:
                ans *= x
        else:
            for x in neg:
                ans *= x
        return ans


so = Solution()
print(so.maxStrength([0]))
print(so.maxStrength([3,-1,-5,2,5,-9]))
print(so.maxStrength([-4,-5,-4]))




