

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        mx1 = 0
        for i in range(n):
            mx1 = max(mx1, min(nums1[i], nums2[i]))
        if mx1 > min(nums1[-1], nums2[-1]) or max(max(nums1), max(nums2)) > max(nums1[-1], nums2[-1]):
            return -1
        if nums1[-1] > nums2[-1]:
            nums1, nums2 = nums2, nums1
        mx1, mx2 = nums1[-1], nums2[-1]
        ans1 = 0
        for i in range(n - 1):
            if nums1[i] > mx1:
                ans1 += 1
        nums2[-1], nums1[-1] = nums1[-1], nums2[-1]
        mx1, mx2 = nums1[-1], nums2[-1]
        ans2 = 1
        for i in range(n - 1):
            if nums2[i] > mx2:
                ans2 += 1

        return min(ans1, ans2)


so = Solution()
print(so.minOperations(nums1 = [1],nums2 = [1]))
print(so.minOperations(nums1 = [2,3,4,5,9],nums2 = [8,8,4,4,4]))
print(so.minOperations(nums1 = [1,2,7], nums2 = [4,5,3]))
print(so.minOperations(nums1 = [1,5,4],nums2 = [2,5,3]))




