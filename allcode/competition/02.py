

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        z1, z2 = nums1.count(0), nums2.count(0)
        s1, s2 = sum(nums1), sum(nums2)
        if z1 > z2:
            z1, z2 = z2, z1
            s1, s2 = s2, s1
        if z1 == z2 == 0:
            return s1 if s1 == s2 else -1
        if z1 == 0:
            return s1 if (s1 >= s2 + z2) else -1
        return max(s1 + z1, s2 + z2)



so = Solution()
print(so.minSum(nums1 = [3,2,0,1,0], nums2 = [6,5,0]))
print(so.minSum(nums1 = [2,0,2,0], nums2 = [1,4]))
print(so.minSum(nums1 = [3,2,0,1,0], nums2 = [6,5,0]))




