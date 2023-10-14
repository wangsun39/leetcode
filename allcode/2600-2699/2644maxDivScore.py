
from leetcode.allcode.competition.mypackage import *


class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        ans = divisors[0]
        mx = 0
        for x in divisors:
            cur = 0
            for y in nums:
                if y % x == 0:
                    cur += 1
            if cur > mx:
                ans = x
                mx = cur
            elif cur == mx and ans > x:
                ans = x
        return ans


so = Solution()
print(so.maxDivScore(nums = [4,7,9,3,9], divisors = [5,2,3]))
print(so.maxDivScore(nums = [20,14,21,10], divisors = [5,7,5]))
print(so.maxDivScore(nums = [12], divisors = [10,16]))




