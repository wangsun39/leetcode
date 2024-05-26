

from leetcode.allcode.competition.mypackage import *

class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [str(x) for x in nums]
        m = len(nums[0])
        counter = [[0] * 10 for _ in range(m)]  # counter[i][j] 第i个数位是j的个数
        for x in nums:
            for j in range(m):
                counter[j][int(x[j])] += 1
        ans = 0
        for i in range(m):
            s = sum(counter[i])
            for j in range(10):
                ans += counter[i][j] * (s - counter[i][j])
        return ans // 2


so = Solution()
print(so.sumDigitDifferences(nums = [13,23,12]))
print(so.sumDigitDifferences(nums = [10,10,10,10]))




