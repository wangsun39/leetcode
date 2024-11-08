# 你要开发一座金矿，地质勘测学家已经探明了这座金矿中的资源分布，并用大小为 m * n 的网格 grid 进行了标注。每个单元格中的整数就表示这一单元格中的黄金数量；如果该单元格是空的，那么就是 0。
#
# 为了使收益最大化，矿工需要按以下规则来开采黄金：
#
# 每当矿工进入一个单元，就会收集该单元格中的所有黄金。
# 矿工每次可以从当前位置向上下左右四个方向走。
# 每个单元格只能被开采（进入）一次。
# 不得开采（进入）黄金数目为 0 的单元格。
# 矿工可以从网格中 任意一个 有黄金的单元格出发或者是停止。
#
#
# 示例 1：
#
# 输入：grid = [[0,6,0],[5,8,7],[0,9,0]]
# 输出：24
# 解释：
# [[0,6,0],
#  [5,8,7],
#  [0,9,0]]
# 一种收集最多黄金的路线是：9 -> 8 -> 7。
# 示例 2：
#
# 输入：grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
# 输出：28
# 解释：
# [[1,0,7],
#  [2,0,6],
#  [3,4,5],
#  [0,3,0],
#  [9,0,20]]
# 一种收集最多黄金的路线是：1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7。
#
#
# 提示：
#
# 1 <= grid.length, grid[i].length <= 15
# 0 <= grid[i][j] <= 100
# 最多 25 个单元格中有黄金。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        vis = [[0] * c for _ in range(r)]
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def dfs(i, j):
            vis[i][j] = 1
            res = 0
            for u, v in dir:
                x, y = u + i, v + j
                if 0 <= x < r and 0 <= y < c and grid[x][y] and vis[x][y] == 0:
                    tmp = dfs(x, y)
                    if tmp > res:
                        res = tmp
            vis[i][j] = 0
            return res + grid[i][j]
        ans = 0
        for i in range(r):
            for j in range(c):
                if 0 == grid[i][j]: continue
                v = dfs(i, j)
                if v > ans:
                    ans = v
        return ans




so = Solution()
print(so.getMaximumGold(grid = [[0,6,0],[5,8,7],[0,9,0]]))




