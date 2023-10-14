
from leetcode.allcode.competition.mypackage import *

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums2) & 1 == 0:
            s1 = 0
        else:
            s1 = 0
            for x in nums1:
                s1 ^= x
        if len(nums1) & 1 == 0:
            s2 = 0
        else:
            s2 = 0
            for x in nums2:
                s2 ^= x
        return s1 ^ s2



so = Solution()
print(so.xorAllNums(nums1 = [2,1,3], nums2 = [10,2,5,0]))
print(so.xorAllNums(nums1 = [1,2], nums2 = [3,4]))




