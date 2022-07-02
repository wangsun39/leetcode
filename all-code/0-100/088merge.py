from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        print(nums1, nums2)
        p1, p2 = m-1, n-1
        for i in range(m+n-1,-1,-1):
            if p1 < 0:
                nums1[i] = nums2[p2]
                p2 -= 1
            elif p2 < 0:
                nums1[i] = nums1[p1]
                p1 -= 1
            elif nums1[p1] <= nums2[p2]:
                nums1[i] = nums2[p2]
                p2 -= 1
            else:
                nums1[i] = nums1[p1]
                p1 -= 1
        return


so = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
so.merge(nums1,3,nums2,3)
print(nums1)
