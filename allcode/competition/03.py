# 给你一个大小为 m x n 的二维矩形 grid 。每次 操作 中，你可以将 任一 格子的值修改为 任意 非负整数。完成所有操作后，你需要确保每个格子 grid[i][j] 的值满足：
#
# 如果下面相邻格子存在的话，它们的值相等，也就是 grid[i][j] == grid[i + 1][j]（如果存在）。
# 如果右边相邻格子存在的话，它们的值不相等，也就是 grid[i][j] != grid[i][j + 1]（如果存在）。
# 请你返回需要的 最少 操作数目。
#
#
#
# 示例 1：
#
# 输入：grid = [[1,0,2],[1,0,2]]
#
# 输出：0
#
# 解释：
#
#
#
# 矩阵中所有格子已经满足要求。
#
# 示例 2：
#
# 输入：grid = [[1,1,1],[0,0,0]]
#
# 输出：3
#
# 解释：
#
#
#
# 将矩阵变成 [[1,0,1],[1,0,1]] ，它满足所有要求，需要 3 次操作：
#
# 将 grid[1][0] 变为 1 。
# 将 grid[0][1] 变为 0 。
# 将 grid[1][2] 变为 1 。
# 示例 3：
#
# 输入：grid = [[1],[2],[3]]
#
# 输出：2
#
# 解释：
#
#
#
# 这个矩阵只有一列，我们可以通过 2 次操作将所有格子里的值变为 1 。
#
#
#
# 提示：
#
# 1 <= n, m <= 1000
# 0 <= grid[i][j] <= 9

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        counter = [[0] * 10 for _ in range(c)]  # counter[i][j] 第i列有几个j
        for i in range(r):
            for j in range(c):
                counter[j][grid[i][j]] += 1
        dp = [[0] * 11 for _ in range(c)] # dp[i][j] 前 i 列变成j，的最小操作数
        for j in range(10):
            dp[0][j] = r - counter[0][j]
        dp[0][10] = r  # 变成其他数字
        for i in range(1, c):
            for j in range(10):
                mn = min(dp[i - 1][k] for k in range(11) if k != j)
                dp[i][j] = mn + (r - counter[i][j])
            dp[i][10] = min(dp[i - 1][k] for k in range(11)) + r
        return min(dp[-1])


so = Solution()
print(so.minimumOperations([[1,1,1],[0,0,0]]))
print(so.minimumOperations([[1,0,2],[1,0,2]]))
print(so.minimumOperations([[1],[2],[3]]))




