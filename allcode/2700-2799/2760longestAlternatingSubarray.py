
from leetcode.allcode.competition.mypackage import *

class Solution:
    def longestAlternatingSubarray1(self, nums: List[int], threshold: int) -> int:
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

    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        # 2023/11/16  双指针
        n = len(nums)
        l = 0
        ans = 0
        while l < n:
            if nums[l] > threshold or nums[l] & 1:
                l += 1
                continue
            r = l + 1
            while r < n and nums[r] & 1 != nums[r - 1] & 1 and nums[r] <= threshold:
                r += 1
            ans = max(ans, r - l)
            if r >= n:
                break
            l = r
        return ans

so = Solution()
print(so.longestAlternatingSubarray(nums = [2,2], threshold = 18))
print(so.longestAlternatingSubarray(nums = [3,2,5,4], threshold = 5))
print(so.longestAlternatingSubarray(nums = [1,2], threshold = 2))
print(so.longestAlternatingSubarray(nums = [2,3,4,5], threshold = 4))
print(so.longestAlternatingSubarray(nums = [1,1], threshold = 4))
print(so.longestAlternatingSubarray(nums = [4], threshold = 1))




