

from leetcode.allcode.competition.mypackage import *

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        s1 = set()
        for i in range(n):
            for j in range(i, n):
                s1.add(nums[i] ^ nums[j])
        s2 = set(nums)
        ans = set()
        for x in s2:
            for y in s1:
                ans.add(x ^ y)
        return len(ans)


so = Solution()
print(so.uniqueXorTriplets([1,3]))




