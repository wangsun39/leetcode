# 给你一个包含 n 个节点的 无向连通图，节点按从 0 到 n - 1 编号。每个节点 最多 与其他两个节点相连。
#
# 图中包含 m 条边，使用一个二维数组 edges 表示，其中 edges[i] = [ai, bi] 表示节点 ai 和节点 bi 之间有一条边。
#
# 你需要为每个节点分配一个从 1 到 n 的 唯一 值。边的值定义为其两端节点值的 乘积 。
#
# 你的得分是图中所有边值的总和。
#
# 返回你可以获得的 最大 得分。
#
#
#
# 示例 1：
#
#
# 输入： n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6]]
#
# 输出： 130
#
# 解释：
#
# 上图展示了一个最优的节点值分配方式。边值的总和为：(7 * 6) + (7 * 5) + (6 * 5) + (1 * 3) + (3 * 4) + (4 * 2) = 130。
#
# 示例 2：
#
#
# 输入： n = 6, edges = [[0,3],[4,5],[2,0],[1,3],[2,4],[1,5]]
#
# 输出： 82
#
# 解释：
#
# 上图展示了一个最优的节点值分配方式。边值的总和为：(1 * 2) + (2 * 4) + (4 * 6) + (6 * 5) + (5 * 3) + (3 * 1) = 82。
#
#
#
# 提示：
#
# 1 <= n <= 5 * 104
# m == edges.length
# 1 <= m <= n
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# 图中不存在重复边。
# 每个节点最多与其他两个节点相连。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxScore(self, n: int, edges: List[List[int]]) -> int:
        if n == 1: return 0
        ans = n * (n - 1)
        for i in range(2, n + 1, 2):
            ans += i * (i - 2)
        for i in range(3, n + 1, 2):
            ans += i * (i - 2)
        if len(edges) == n:
            ans += 2
        return ans


so = Solution()
print(so.maxScore(n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6]]))
print(so.maxScore(n = 6, edges = [[0,3],[4,5],[2,0],[1,3],[2,4],[1,5]]))




