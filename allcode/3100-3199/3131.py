

from leetcode.allcode.competition.mypackage import *

class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return (sum(nums2) - sum(nums1)) // len(nums1)


so = Solution()
print(so.addedInteger(nums1 = [2,6,4], nums2 = [9,7,5]))




