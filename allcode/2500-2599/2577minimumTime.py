# 给你一个 m x n 的矩阵 grid ，每个元素都为 非负 整数，其中 grid[row][col] 表示可以访问格子 (row, col) 的 最早 时间。也就是说当你访问格子 (row, col) 时，最少已经经过的时间为 grid[row][col] 。
#
# 你从 最左上角 出发，出发时刻为 0 ，你必须一直移动到上下左右相邻四个格子中的 任意 一个格子（即不能停留在格子上）。每次移动都需要花费 1 单位时间。
#
# 请你返回 最早 到达右下角格子的时间，如果你无法到达右下角的格子，请你返回 -1 。
#
#
#
# 示例 1：
#
#
#
# 输入：grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]
# 输出：7
# 解释：一条可行的路径为：
# - 时刻 t = 0 ，我们在格子 (0,0) 。
# - 时刻 t = 1 ，我们移动到格子 (0,1) ，可以移动的原因是 grid[0][1] <= 1 。
# - 时刻 t = 2 ，我们移动到格子 (1,1) ，可以移动的原因是 grid[1][1] <= 2 。
# - 时刻 t = 3 ，我们移动到格子 (1,2) ，可以移动的原因是 grid[1][2] <= 3 。
# - 时刻 t = 4 ，我们移动到格子 (1,1) ，可以移动的原因是 grid[1][1] <= 4 。
# - 时刻 t = 5 ，我们移动到格子 (1,2) ，可以移动的原因是 grid[1][2] <= 5 。
# - 时刻 t = 6 ，我们移动到格子 (1,3) ，可以移动的原因是 grid[1][3] <= 6 。
# - 时刻 t = 7 ，我们移动到格子 (2,3) ，可以移动的原因是 grid[2][3] <= 7 。
# 最终到达时刻为 7 。这是最早可以到达的时间。
# 示例 2：
#
#
#
# 输入：grid = [[0,2,4],[3,2,1],[1,0,4]]
# 输出：-1
# 解释：没法从左上角按题目规定走到右下角。
#
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 2 <= m, n <= 1000
# 4 <= m * n <= 105
# 0 <= grid[i][j] <= 105
# grid[0][0] == 0

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        if not ((r > 1 and grid[1][0] <= 1) or (c > 1 and grid[0][1] <= 1)):
            return -1
        dp = [[-1] * c for _ in range(r)]
        # dp[0][0] = 0
        dir = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        hp = []
        heapify(hp)
        heappush(hp, [0, (0, 0)])
        while len(hp):
            d, (x, y) = heappop(hp)
            # print(d, x, y)
            if dp[x][y] != -1:
                continue
            if x == r - 1 and y == c - 1:
                return d
            dp[x][y] = d
            for x0, y0 in dir:
                u, v = x + x0, y + y0
                if 0 <= u < r and 0 <= v < c and dp[u][v] == -1:
                    if d + 1 >= grid[u][v]:
                        heappush(hp, [d + 1, (u, v)])
                    elif (grid[u][v] - d) & 1:  # 奇数
                        heappush(hp, [grid[u][v], (u, v)])
                    else:
                        heappush(hp, [grid[u][v] + 1, (u, v)])





so = Solution()
print(so.minimumTime([[0,1,3,2],[5,1,2,5],[4,3,8,6]]))  # 7
print(so.minimumTime([[0,2,4],[3,2,1],[1,0,4]]))  # -1




