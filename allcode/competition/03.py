

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        s1, s2 = set(nums1), set(nums2)
        s = s1 & s2
        ans1 = set()
        for x in s1:
            if x not in s2:
                ans1.add(x)
            if len(ans1) >= n // 2:
                break
        ans2 = set()
        for x in s2:
            if x not in s1:
                ans2.add(x)
            if len(ans2) >= n // 2:
                break
        ans = ans1 | ans2
        for x in s:
            if len(ans) >= n:
                break
            ans.add(x)
        return len(ans)




so = Solution()
print(so.maximumSetSize(nums1 = [1,1,2,2,3,3], nums2 = [4,4,5,5,6,6]))
print(so.maximumSetSize(nums1 = [1,2,3,4,5,6], nums2 = [2,3,2,3,2,3]))
print(so.maximumSetSize(nums1 = [1,2,1,2], nums2 = [1,1,1,1]))




