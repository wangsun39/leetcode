
from leetcode.allcode.competition.mypackage import *


class Solution:

    def floyd(self, n: int, edges: List[List[int]]) -> List[int]:
        w = [[inf] * n for _ in range(n)]
        for x, y, wt in edges:
            w[x][y] = w[y][x] = wt

        @cache
        def dfs(k: int, i: int, j: int) -> int:
            if k < 0:  # 递归边界
                return w[i][j]
            return min(dfs(k - 1, i, j), dfs(k - 1, i, k) + dfs(k - 1, k, j))

        f = [[inf] * n for _ in range(n)]  # f[i][j] 表示 i 到 j 的最小距离
        for i in range(n):
            f[i][i] = 0
            for j in range(i + 1, n):
                f[i][j] = f[j][i] = dfs(n - 1, i, j)

        return f






