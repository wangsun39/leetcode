
from leetcode.allcode.competition.mypackage import *

class Solution:
    def minDays1(self, n: int) -> int:
        dq1, dq2 = deque([n]), deque()
        vis = {n}
        t = 0
        while dq1:
            while dq1:
                x = dq1.pop()
                if x == 1:
                    return t + 1
                if x - 1 not in vis:
                    dq2.append(x - 1)
                    vis.add(x - 1)
                if x % 2 == 0 and x // 2 not in vis:
                    dq2.append(x // 2)
                    vis.add(x // 2)
                if x % 3 == 0 and x // 3 not in vis:
                    dq2.append(x // 3)
                    vis.add(x // 3)
            dq1, dq2 = dq2, deque()
            t += 1

    def minDays(self, n: int) -> int:
        # 2024/5/12 记忆化搜索
        @cache
        def dfs(x):
            if x <= 1:
                return x
            return min(dfs(x // 2) + x % 2, dfs(x // 3) + x % 3) + 1
        return dfs(n)

so = Solution()
print(so.minDays(10))
print(so.minDays(6))
print(so.minDays(1))
print(so.minDays(56))




