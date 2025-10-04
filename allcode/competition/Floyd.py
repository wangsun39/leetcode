
from leetcode.allcode.competition.mypackage import *


class Solution:

    def floyd1(n: int, edges: List[List[int]]) -> List[List[int]]:  # 无向图
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



    def floyd2(n: int, edges: List[List[int]]) -> List[List[int]]:  # 有向图
        w = [[inf] * n for _ in range(n)]
        for x, y, wt in edges:
            w[x][y] = wt

        @cache
        def dfs(k: int, i: int, j: int) -> int:
            if k < 0:  # 递归边界
                return w[i][j]
            return min(dfs(k - 1, i, j), dfs(k - 1, i, k) + dfs(k - 1, k, j))

        f = [[inf] * n for _ in range(n)]  # f[i][j] 表示 i 到 j 的最小距离
        for i in range(n):
            f[i][i] = 0
            for j in range(i + 1, n):
                f[i][j] = dfs(n - 1, i, j)
                f[j][i] = dfs(n - 1, j, i)

        return f


    def floyd3(n: int, edges: List[List[int]]) -> List[List[int]]:  # 无向图，递推
        # f[k][i][j] 表示从 i 到 j 的最短路长度，并且这条最短路的中间节点编号都 ≤k

        w = [[inf] * n for _ in range(n)]
        for x, y, wt in edges:
            w[x][y] = w[y][x] = wt

        f = [[[0] * n for _ in range(n)] for _ in range(n + 1)]
        f[0] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    f[k + 1][i][j] = min(f[k][i][j], f[k][i][k] + f[k][k][j])
        return f[n]



    def floyd4(n: int, edges: List[List[int]]) -> List[List[int]]:  # 有向图，递推
        f = [[inf] * n for _ in range(n)]
        for i in range(n):
            f[i][i] = 0
        for x, y, w in edges:
            f[x][y] = w  # 添加一条边（题目保证没有重边和自环）
        for k in range(n):
            for i in range(n):
                if f[i][k] == inf: continue
                for j in range(n):
                    f[i][j] = min(f[i][j], f[i][k] + f[k][j])
        return f

    def floyd5(edges: List[List]) -> defaultdict:  # 有向图，递推，图表示中点可以是字符串，不一定是 0~n-1
        f = defaultdict(lambda: defaultdict(lambda: inf))
        s = set()
        for x, y, _ in edges:
            s.add(x)
            s.add(y)
            f[x][x] = f[y][y] = 0
        for x, y, w in edges:
            f[x][y] = w  # 添加一条边（题目保证没有重边和自环）
        for k in s:
            for i in s:
                if f[i][k] == inf: continue
                for j in s:
                    f[i][j] = MIN(f[i][j], f[i][k] + f[k][j])
        return f






