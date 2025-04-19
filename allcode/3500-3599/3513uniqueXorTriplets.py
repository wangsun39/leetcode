

from leetcode.allcode.competition.mypackage import *

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2: return n
        l = n.bit_length()
        return 1 << l


so = Solution()
print(so.uniqueXorTriplets([1,2]))




