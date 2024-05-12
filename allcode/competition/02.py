

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        ans = -inf
        n = len(energy)
        @cache
        def dfs(idx):
            nonlocal ans
            if idx >= n: return 0
            res = dfs(idx + k) + energy[idx]
            ans = max(ans, res)
            return res
        for i in range(k):
            max(ans, dfs(i))
        return ans


so = Solution()
print(so.maximumEnergy(energy = [5,2,-10,-5,1], k = 3))
print(so.maximumEnergy(energy = [-2,-3,-1], k = 2))




