
from leetcode.allcode.competition.mypackage import *

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        nums3 = [nums1[i] - nums2[i] for i in range(n)]
        hp = []
        ans = 0
        for x in nums3:
            p1 = bisect_right(hp, x + diff)
            ans += p1
            insort_left(hp, x)
        return ans




so = Solution()
print(so.numberOfPairs(nums1 = [3,2,5], nums2 = [2,2,1], diff = 1))
print(so.numberOfPairs(nums1 = [3,-1], nums2 = [-2,2], diff = -1))




