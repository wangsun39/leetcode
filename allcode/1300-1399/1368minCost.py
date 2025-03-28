# 给你一个 m x n 的网格图 grid 。 grid 中每个格子都有一个数字，对应着从该格子出发下一步走的方向。 grid[i][j] 中的数字可能为以下几种情况：
#
# 1 ，下一步往右走，也就是你会从 grid[i][j] 走到 grid[i][j + 1]
# 2 ，下一步往左走，也就是你会从 grid[i][j] 走到 grid[i][j - 1]
# 3 ，下一步往下走，也就是你会从 grid[i][j] 走到 grid[i + 1][j]
# 4 ，下一步往上走，也就是你会从 grid[i][j] 走到 grid[i - 1][j]
# 注意网格图中可能会有 无效数字 ，因为它们可能指向 grid 以外的区域。
#
# 一开始，你会从最左上角的格子 (0,0) 出发。我们定义一条 有效路径 为从格子 (0,0) 出发，每一步都顺着数字对应方向走，最终在最右下角的格子 (m - 1, n - 1) 结束的路径。有效路径 不需要是最短路径 。
#
# 你可以花费 cost = 1 的代价修改一个格子中的数字，但每个格子中的数字 只能修改一次 。
#
# 请你返回让网格图至少有一条有效路径的最小代价。
#
#
#
# 示例 1：
#
#
#
# 输入：grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
# 输出：3
# 解释：你将从点 (0, 0) 出发。
# 到达 (3, 3) 的路径为： (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) 花费代价 cost = 1 使方向向下 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) 花费代价 cost = 1 使方向向下 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) 花费代价 cost = 1 使方向向下 --> (3, 3)
# 总花费为 cost = 3.
# 示例 2：
#
#
#
# 输入：grid = [[1,1,3],[3,2,2],[1,1,4]]
# 输出：0
# 解释：不修改任何数字你就可以从 (0, 0) 到达 (2, 2) 。
# 示例 3：
#
#
#
# 输入：grid = [[1,2],[4,3]]
# 输出：1
# 示例 4：
#
# 输入：grid = [[2,2,2],[2,2,2]]
# 输出：3
# 示例 5：
#
# 输入：grid = [[4]]
# 输出：0
#
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        dir = [[-1, 0, 3], [1, 0, 4], [0, -1, 1], [0, 1, 2]]
        r, c = len(grid), len(grid[0])
        dq1 = deque([[r - 1, c - 1]])
        dp = [[inf] * c for _ in range(r)]
        dp[r - 1][c - 1] = 0
        dq3, tmp = deque(), set()
        cur = 0
        while dq1:
            dq2 = deque()
            while dq1:
                x, y = dq1.popleft()
                for d1, d2, d in dir:
                    u, v = x + d1, y + d2
                    if 0 <= u < r and 0 <= v < c:
                        if dp[u][v] != inf: continue
                        if d == grid[u][v]:
                            dp[u][v] = cur
                            dq2.append([u, v])  # 不需要修改方向的格子
                        elif (u, v) not in tmp:
                            dq3.append([u, v])  # 需要修改方向的格子
                            tmp.add((u, v))  # 记录已经在dq3中的格子
            if dq2:
                dq1 = dq2
            else:
                cur += 1
                for (x, y) in tmp:
                    dp[x][y] = cur
                dq1, dq3, tmp = dq3, deque(), set()
            if dp[0][0] != inf:
                return dp[0][0]




so = Solution()
print(so.minCost(grid = [[3,4,3],[2,2,2],[2,1,1],[4,3,2],[2,1,4],[2,4,1],[3,3,3],[1,4,2],[2,2,1],[2,1,1],[3,3,1],[4,1,4],[2,1,4],[3,2,2],[3,3,1],[4,4,1],[1,2,2],[1,1,1],[1,3,4],[1,2,1],[2,2,4],[2,1,3],[1,2,1],[4,3,2],[3,3,4],[2,2,1],[3,4,3],[4,2,3],[4,4,4]]))  # 18
print(so.minCost(grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]))
print(so.minCost(grid = [[1,1,3],[3,2,2],[1,1,4]]))
print(so.minCost(grid = [[1,2],[4,3]]))
print(so.minCost(grid = [[2,2,2],[2,2,2]]))
print(so.minCost(grid = [[4]]))




