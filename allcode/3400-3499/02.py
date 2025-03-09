

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        mxl = []
        n = len(nums1)
        ans = [0] * n
        s = 0
        pre_v = -1
        pre_a = 0
        for i, x in sorted(enumerate(nums1), key=lambda y:y[1]):
            if pre_v == x or pre_v == -1:
                ans[i] = pre_a
            else:
                ans[i] = s
            pre_v, pre_a = x, ans[i]
            if len(mxl) < k:
                heappush(mxl, nums2[i])
                s += nums2[i]
            else:
                if mxl[0] < nums2[i]:
                    y = heappop(mxl)
                    s += nums2[i] - y
                    heappush(mxl, nums2[i])
        return ans

so = Solution()
print(so.findMaxSum(nums1 = [4,2,1,5,3], nums2 = [10,20,30,40,50], k = 2))
print(so.findMaxSum(nums1 = [2,2,2,2], nums2 = [3,1,2,3], k = 1))




