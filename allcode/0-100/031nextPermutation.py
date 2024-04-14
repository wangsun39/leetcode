from collections import defaultdict
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = -1
        for i in range(n - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                k = i
                break
        if k == -1:
            for i in range(n // 2):
                nums[i], nums[n - 1 - i] = nums[n - 1 - i], nums[i]
            return
        for i in range(k, n):
            if i == n - 1:
                nums[k - 1], nums[i] = nums[i], nums[k - 1]
                break
            if nums[k - 1] >= nums[i + 1]:
                nums[k - 1], nums[i] = nums[i], nums[k - 1]
                break
        for i in range((n - k) // 2):
            nums[k + i], nums[n - 1 - i] = nums[n - 1 - i], nums[k + i]



so = Solution()
#print(so.findSubstring("barfoothefoobarman", ["foo","bar"]))
print(so.nextPermutation([1,2,3]))
print(so.nextPermutation([1,3,3]))
print(so.nextPermutation([3,3,1]))