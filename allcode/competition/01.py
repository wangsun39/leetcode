

from leetcode.allcode.competition.mypackage import *

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s = sum(nums)
        s1 = s2 = 0
        for x in nums:
            if x < 10:
                s1 += x
            elif x < 100:
                s2 += x
        if s1 * 2 > s or s2 * 2 > s:
            return True
        return False


so = Solution()
print(so.canAliceWin(nums = [5,5,5,25]))
print(so.canAliceWin(nums = [1,2,3,4,10]))




