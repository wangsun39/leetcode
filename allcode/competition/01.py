

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        ans = 0
        bits = defaultdict(int)
        for x in nums:
            i = 0
            while x:
                if x & 1 == 1:
                    bits[i] += 1
                i += 1
                x >>= 1
        for i, v in bits.items():
            if v >= k:
                ans |= (1 << i)
        return ans




so = Solution()
print(so.findKOr(nums = [7,12,9,8,9,15], k = 4))
print(so.findKOr(nums = [2,12,1,11,4,5], k = 6))
print(so.findKOr(nums = [10,8,5,9,11,6,8], k = 1))




