# 给你一个m x n的整数网格图grid，你可以从一个格子移动到4个方向相邻的任意一个格子。
#
# 请你返回在网格图中从 任意格子出发，达到 任意格子，且路径中的数字是 严格递增的路径数目。由于答案可能会很大，请将结果对109 + 7取余后返回。
#
# 如果两条路径中访问过的格子不是完全相同的，那么它们视为两条不同的路径。
#
#
#
# 示例 1：
#
#
#
# 输入：grid = [[1,1],[3,4]]
# 输出：8
# 解释：严格递增路径包括：
# - 长度为 1 的路径：[1]，[1]，[3]，[4] 。
# - 长度为 2 的路径：[1 -> 3]，[1 -> 4]，[3 -> 4] 。
# - 长度为 3 的路径：[1 -> 3 -> 4] 。
# 路径数目为 4 + 3 + 1 = 8 。
# 示例 2：
#
# 输入：grid = [[1],[2]]
# 输出：3
# 解释：严格递增路径包括：
# - 长度为 1 的路径：[1]，[2] 。
# - 长度为 2 的路径：[1 -> 2] 。
# 路径数目为 2 + 1 = 3 。
#
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 1000
# 1 <= m * n <= 105
# 1 <= grid[i][j] <= 105
# 通过次数4,412提交次数8,965


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        MAX = int(1e9 + 7)

        @lru_cache(None)
        def dfs(i, j):
            res = 1
            dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for d in dir:
                if 0 <= i + d[0] < m and 0 <= j + d[1] < n and grid[i][j] < grid[i + d[0]][j + d[1]]:
                    res += dfs(i  + d[0], j + d[1])
                    res %= MAX
            return res
        for i in range(m):
            for j in range(n):
                ans += dfs(i, j)
                ans %= MAX
        return ans


so = Solution()
print(so.countPaths([[1],[2]]))
print(so.countPaths([[1,1],[3,4]]))




