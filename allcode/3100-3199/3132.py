

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        nums2.sort()
        for i in range(-1000, 1001, 1):
            nums3 = sorted([x + i for x in nums1])
            k = j = 0
            found = True
            while k < n and j < n - 2:
                if nums3[k] == nums2[j]:
                    k += 1
                    j += 1
                else:
                    k += 1
                    if k - j > 2:
                        found = False
                        break
            if found:
                return i


so = Solution()
print(so.minimumAddedInteger(nums1 = [3,5,5,3], nums2 = [7,7]))
print(so.minimumAddedInteger(nums1 = [4,20,16,12,8], nums2 = [14,18,10]))




