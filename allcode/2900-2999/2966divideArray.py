

from leetcode.allcode.competition.mypackage import *

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        g = n // 3
        ans = [[0] * 3 for _ in range(g)]
        for i in range(n):
            ans[i // 3][i % 3] = nums[i]
        if any(x[2] - x[0] > k for x in ans):
            return []
        return ans


so = Solution()
print(so.divideArray([15,13,12,13,12,14,12,2,3,13,12,14,14,13,5,12,12,2,13,2,2], 2))
print(so.divideArray(nums = [1,3,4,8,7,9,3,5,1], k = 2))
print(so.divideArray(nums = [1,3,3,2,7,3], k = 3))




