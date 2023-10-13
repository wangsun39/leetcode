

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        n = len(s1)
        idx = [i for i in range(n) if s1[i] != s2[i]]
        if len(idx) & 1:
            return -1
        if x == 1:
            return len(idx) // 2
        m = len(idx)
        if m == 0:
            return 0
        def cost(i, j):
            return min(j - i, x)
        @cache
        def dfs(i):   # idx[i:] 之后的最少代价
            if i >= m - 1:
                return 0
            if i & 1:
                c1 = cost(idx[i], idx[i + 1]) + dfs(i + 2)
                c2 = dfs(i + 1)
                return min(c1, c2)
            else:
                c1 = cost(idx[i], idx[i + 1]) + dfs(i + 2)
                c2 = dfs(i + 1) + x
                return min(c1, c2)
        return dfs(0)


so = Solution()
print(so.minOperations(s1 = "1100011000", s2 = "0101001010", x = 2))
print(so.minOperations(s1 = "10110", s2 = "00011", x = 4))




