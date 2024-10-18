

from leetcode.allcode.competition.mypackage import *

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pre1 = {nums1[0]}
        pre2 = {nums2[0]}
        union1 = pre1 & pre2  # 公共前缀
        post1 = set(nums1[2:])
        post2 = set(nums2[2:])
        union2 = post1 & post2  # 公共后缀
        j = 1
        ans = 0
        for i in range(1, n - 1):
            a1, b1, c1 = nums1[i - 1], nums1[i], nums1[i + 1]
            pre1.add(a1)
            if a1 in pre2:
                union1.add(a1)
            if b1 in union2:
                union2.remove(b1)
            while j < n and b1 != nums2[j]:
                a2, b2, c2 = nums2[i - 1], nums2[i], nums2[i + 1]
                pre2.add(a2)
                if a2 in pre1:
                    union1.add(a2)
                if b2 in union2:
                    union2.remove(b2)
                j += 1
            if j == n: break
            ans += len(union1) * len(union2)

        return ans

so = Solution()
print(so.goodTriplets(nums1 = [2,0,1,3], nums2 = [0,1,2,3]))




