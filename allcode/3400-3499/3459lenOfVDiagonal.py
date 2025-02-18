# 给你一个大小为 n x m 的二维整数矩阵 grid，其中每个元素的值为 0、1 或 2。
#
# V 形对角线段 定义如下：
#
# 线段从 1 开始。
# 后续元素按照以下无限序列的模式排列：2, 0, 2, 0, ...。
# 该线段：
# 起始于某个对角方向（左上到右下、右下到左上、右上到左下或左下到右上）。
# 沿着相同的对角方向继续，保持 序列模式 。
# 在保持 序列模式 的前提下，最多允许 一次顺时针 90 度转向 另一个对角方向。
#
#
# 返回最长的 V 形对角线段 的 长度 。如果不存在有效的线段，则返回 0。
#
#
#
# 示例 1：
#
# 输入： grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
#
# 输出： 5
#
# 解释：
#
#
#
# 最长的 V 形对角线段长度为 5，路径如下：(0,2) → (1,3) → (2,4)，在 (2,4) 处进行 顺时针 90 度转向 ，继续路径为 (3,3) → (4,2)。
#
# 示例 2：
#
# 输入： grid = [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
#
# 输出： 4
#
# 解释：
#
#
#
# 最长的 V 形对角线段长度为 4，路径如下：(2,3) → (3,2)，在 (3,2) 处进行 顺时针 90 度转向 ，继续路径为 (2,1) → (1,0)。
#
# 示例 3：
#
# 输入： grid = [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]
#
# 输出： 5
#
# 解释：
#
#
#
# 最长的 V 形对角线段长度为 5，路径如下：(0,0) → (1,1) → (2,2) → (3,3) → (4,4)。
#
# 示例 4：
#
# 输入： grid = [[1]]
#
# 输出： 1
#
# 解释：
#
# 最长的 V 形对角线段长度为 1，路径如下：(0,0)。
#
#
#
# 提示：
#
# n == grid.length
# m == grid[i].length
# 1 <= n, m <= 500
# grid[i][j] 的值为 0、1 或 2。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        dir = [[-1, -1], [1, 1], [1, -1], [-1, 1]]
        t = {0: 3, 1: 2, 2: 0, 3: 1}  # 方向转换
        r, c = len(grid), len(grid[0])

        @cache
        def dfs(x, y, d, turn):  # 沿着d方向到达x行，y列后最长能走的长度，turn表示是否转弯过
            res = 1
            u, v = x + dir[d][0], y + dir[d][1]
            if 0 <= u < r and 0 <= v < c and grid[u][v] + grid[x][y] == 2:
                res = max(res, 1 + dfs(u, v, d, turn))
            if not turn:
                x0, y0 = dir[t[d]]  # d1 为转弯后的方向
                u, v = x + x0, y + y0
                if 0 <= u < r and 0 <= v < c and grid[u][v] + grid[x][y] == 2:
                    res = max(res, 1 + dfs(u, v, t[d], True))
            return res
        ans = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    ans = max(ans, 1)
                    for k, [x0, y0] in enumerate(dir):
                        u, v = i + x0, j + y0
                        if 0 <= u < r and 0 <= v < c and grid[u][v] == 2:
                            ans = max(ans, 1 + dfs(u, v, k, False))
        return ans




so = Solution()
print(so.lenOfVDiagonal(grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]))




