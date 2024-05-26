

from leetcode.allcode.competition.mypackage import *

class Solution:
    def waysToReachStair(self, k: int) -> int:
        @cache
        def dfs(p, jmp, canback):
            res = 0
            if p == k:
                res += 1
            if p == 0:
                return res + dfs(p + 2 ** jmp, jmp + 1, 1)
            if p > k:
                if not canback:
                    return res
                if p - k > 1:
                    return res
                return res + dfs(p - 1, jmp, 0)
            r1 = dfs(p + 2 ** jmp, jmp + 1, 1)
            r2 = 0
            if canback:
                r2 = dfs(p - 1, jmp, 0)
            return res + r1 + r2
        return dfs(1, 0, 1)


so = Solution()
print(so.waysToReachStair(k = 2))
print(so.waysToReachStair(k = 1))
print(so.waysToReachStair(k = 0))




