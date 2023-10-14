
from leetcode.allcode.competition.mypackage import *

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        ans = 0
        for i, x in enumerate(nums):
            if x % 2 != 0: continue
            if x > threshold: continue
            ans = max(ans, 1)
            for j in range(i + 1, n):
                if nums[j] > threshold: break
                if nums[j] % 2 != nums[j - 1] % 2:
                    ans = max(ans, j - i + 1)
                else:
                    break
        return ans


so = Solution()
print(so.longestAlternatingSubarray(nums = [2,2], threshold = 18))
print(so.longestAlternatingSubarray(nums = [3,2,5,4], threshold = 5))
print(so.longestAlternatingSubarray(nums = [1,2], threshold = 2))
print(so.longestAlternatingSubarray(nums = [2,3,4,5], threshold = 4))
print(so.longestAlternatingSubarray(nums = [1,1], threshold = 4))
print(so.longestAlternatingSubarray(nums = [4], threshold = 1))




