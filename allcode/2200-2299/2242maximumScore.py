# 给你一个 n 个节点的 无向图 ，节点编号为 0 到 n - 1 。
#
# 给你一个下标从 0 开始的整数数组 scores ，其中 scores[i] 是第 i 个节点的分数。同时给你一个二维整数数组 edges ，其中 edges[i] = [ai, bi] ，表示节点 ai 和 bi 之间有一条 无向 边。
#
# 一个合法的节点序列如果满足以下条件，我们称它是 合法的 ：
#
# 序列中每 相邻 节点之间有边相连。
# 序列中没有节点出现超过一次。
# 节点序列的分数定义为序列中节点分数之 和 。
#
# 请你返回一个长度为 4 的合法节点序列的最大分数。如果不存在这样的序列，请你返回 -1 。
#
#
#
# 示例 1：
#
#
#
# 输入：scores = [5,2,9,8,4], edges = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
# 输出：24
# 解释：上图为输入的图，节点序列为 [0,1,2,3] 。
# 节点序列的分数为 5 + 2 + 9 + 8 = 24 。
# 观察可知，没有其他节点序列得分和超过 24 。
# 注意节点序列 [3,1,2,0] 和 [1,0,2,3] 也是合法的，且分数为 24 。
# 序列 [0,3,2,4] 不是合法的，因为没有边连接节点 0 和 3 。
# 示例 2：
#
#
#
# 输入：scores = [9,20,6,4,11,12], edges = [[0,3],[5,3],[2,4],[1,3]]
# 输出：-1
# 解释：上图为输入的图。
# 没有长度为 4 的合法序列，所以我们返回 -1 。
#
#
# 提示：
#
# n == scores.length
# 4 <= n <= 5 * 104
# 1 <= scores[i] <= 108
# 0 <= edges.length <= 5 * 104
# edges[i].length == 2
# 0 <= ai, bi <= n - 1
# ai != bi
# 不会有重边。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for x, y in edges:
            g[x].append(y)
            g[x].sort(reverse=True, key=lambda t:scores[t])
            if len(g[x]) > 3:
                g[x].pop()
            g[y].append(x)
            g[y].sort(reverse=True, key=lambda t:scores[t])
            if len(g[y]) > 3:
                g[y].pop()
        ans = -1
        for x, y in edges + [[v, u] for u, v in edges]:
            i = 0
            while i < len(g[x]) and g[x][i] == y:
                i += 1
            if i >= len(g[x]): continue
            j = 0
            while j < len(g[y]) and g[y][j] in (x, g[x][i]):
                j += 1
            if j >= len(g[y]): continue
            ans = max(ans, scores[g[x][i]] + scores[x] + scores[y] + scores[g[y][j]])
        return ans

so = Solution()
print(so.maximumScore(scores = [5,2,9,8,4], edges = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]))
print(so.maximumScore(scores = [9,20,6,4,11,12], edges = [[0,3],[5,3],[2,4],[1,3]]))


