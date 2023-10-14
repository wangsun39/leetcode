# 给你一个整数 n 。现有一个包含 n 个顶点的 无向 图，顶点按从 0 到 n - 1 编号。给你一个二维整数数组 edges 其中 edges[i] = [ai, bi] 表示顶点 ai 和 bi 之间存在一条 无向 边。
#
# 返回图中 完全连通分量 的数量。
#
# 如果在子图中任意两个顶点之间都存在路径，并且子图中没有任何一个顶点与子图外部的顶点共享边，则称其为 连通分量 。
#
# 如果连通分量中每对节点之间都存在一条边，则称其为 完全连通分量 。
#
#
#
# 示例 1：
#
#
#
# 输入：n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
# 输出：3
# 解释：如上图所示，可以看到此图所有分量都是完全连通分量。
# 示例 2：
#
#
#
# 输入：n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
# 输出：1
# 解释：包含节点 0、1 和 2 的分量是完全连通分量，因为每对节点之间都存在一条边。
# 包含节点 3 、4 和 5 的分量不是完全连通分量，因为节点 4 和 5 之间不存在边。
# 因此，在图中完全连接分量的数量是 1 。
#
#
# 提示：
#
# 1 <= n <= 50
# 0 <= edges.length <= n * (n - 1) / 2
# edges[i].length == 2
# 0 <= ai, bi <= n - 1
# ai != bi
# 不存在重复的边

from leetcode.allcode.competition.mypackage import *


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        ans = 0
        r, c = len(grid), len(grid[0])
        dp = [[0] * c for _ in range(r)]
        for i in range(r):
            dp[i][0] = 1
        for j in range(1, c):
            nx = 0
            for i in range(r):
                if dp[i][j-1] and grid[i][j - 1] < grid[i][j]:
                    dp[i][j] = 1
                elif i > 0 and dp[i-1][j-1] and grid[i - 1][j - 1] < grid[i][j]:
                    dp[i][j] = 1
                elif i < r - 1 and dp[i+1][j-1] and grid[i + 1][j - 1] < grid[i][j]:
                    dp[i][j] = 1
                if dp[i][j] > 0:
                    ans = j
                    nx = 1
            if nx == 0:
                break

        return ans



so = Solution()
print(so.maxMoves([[187,167,209,251,152,236,263,128,135],
                   [267,249,251,285,73,204,70,207,74],
                   [189,159,235,66,84,89,153,111,189],
                   [120,81,210,7,2,231,92,128,218],
                   [193,131,244,293,284,175,226,205,245]]))
print(so.maxMoves([[3,2,4],[2,1,9],[1,1,7]]))
print(so.maxMoves([[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]))




