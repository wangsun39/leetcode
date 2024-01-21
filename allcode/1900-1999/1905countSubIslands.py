# 给你两个 m x n 的二进制矩阵 grid1 和 grid2 ，它们只包含 0 （表示水域）和 1 （表示陆地）。一个 岛屿 是由 四个方向 （水平或者竖直）上相邻的 1 组成的区域。任何矩阵以外的区域都视为水域。
#
# 如果 grid2 的一个岛屿，被 grid1 的一个岛屿 完全 包含，也就是说 grid2 中该岛屿的每一个格子都被 grid1 中同一个岛屿完全包含，那么我们称 grid2 中的这个岛屿为 子岛屿 。
#
# 请你返回 grid2 中 子岛屿 的 数目 。
#
#
#
# 示例 1：
#
#
# 输入：grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
# 输出：3
# 解释：如上图所示，左边为 grid1 ，右边为 grid2 。
# grid2 中标红的 1 区域是子岛屿，总共有 3 个子岛屿。
# 示例 2：
#
#
# 输入：grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
# 输出：2
# 解释：如上图所示，左边为 grid1 ，右边为 grid2 。
# grid2 中标红的 1 区域是子岛屿，总共有 2 个子岛屿。
#
#
# 提示：
#
# m == grid1.length == grid2.length
# n == grid1[i].length == grid2[i].length
# 1 <= m, n <= 500
# grid1[i][j] 和 grid2[i][j] 都要么是 0 要么是 1 。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        r, c = len(grid1), len(grid1[0])
        n = r * c
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def f(grid):
            fa = list(range(n))
            # fa = {x: x for x in nums}  # 另一种写法，x不连续
            def find(x):
                if x != fa[x]:
                    fa[x] = find(fa[x])
                return fa[x]
            def union(x, y):
                fa[find(y)] = find(x)

            for i in range(r):
                for j in range(c):
                    if grid[i][j] == 0:
                        fa[i * c + j] = -1
                        continue
                    for x0, y0 in dir:
                        u, v = i + x0, j + y0
                        if 0 <= u < r and 0 <= v < c:
                            if 1 == grid[u][v]:
                                union(i * c + j, u * c + v)
            for i in range(n):
                if fa[i] != -1:
                    find(i)
            d = defaultdict(set)
            for i in range(n):
                if fa[i] == -1: continue
                d[fa[i]].add(i)
            return fa, d
        fa1, d1 = f(grid1)
        fa2, d2 = f(grid2)
        ans = 0
        for s in d2.values():
            l = list(s)
            if all(fa1[l[0]] == fa1[x] != -1 for x in l):
                ans += 1
        return ans




so = Solution()
print(so.countSubIslands(grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]))
print(so.countSubIslands(grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]))




