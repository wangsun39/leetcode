

from leetcode.allcode.competition.mypackage import *

class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        dist = []
        dic = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                ab = abs(nums[i] - nums[j])
                dist.append(ab)
                dic[ab].append([i, j])
        dist.sort()
        forbid = defaultdict(list)
        ans = 0
        for d in dist:
            for i, pl in forbid.items():



so = Solution()
print(so.sumOfPowers())




