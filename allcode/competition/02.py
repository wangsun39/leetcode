

from leetcode.allcode.competition.mypackage import *

MX = 100 + 1
is_prime = [True] * MX
is_prime[1] = False
for i in range(2, isqrt(MX) + 1):
    if is_prime[i]:
        for j in range(i * i, MX, i):
            is_prime[j] = False

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        flg = [is_prime[x] for x in nums]
        idx = [i for i, x in enumerate(flg) if x]
        return idx[-1] - idx[0]


so = Solution()
print(so.maximumPrimeDifference( [4,2,9,5,3]))
print(so.maximumPrimeDifference(  [4,8,2,8]))




