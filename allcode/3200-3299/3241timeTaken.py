# 给你一棵 无向 树，树中节点从 0 到 n - 1 编号。同时给你一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ui, vi] 表示节点 ui 和 vi 在树中有一条边。
#
# 一开始，所有 节点都 未标记 。对于节点 i ：
#
# 当 i 是奇数时，如果时刻 x - 1 该节点有 至少 一个相邻节点已经被标记了，那么节点 i 会在时刻 x 被标记。
# 当 i 是偶数时，如果时刻 x - 2 该节点有 至少 一个相邻节点已经被标记了，那么节点 i 会在时刻 x 被标记。
# 请你返回一个数组 times ，表示如果你在时刻 t = 0 标记节点 i ，那么时刻 times[i] 时，树中所有节点都会被标记。
#
# 请注意，每个 times[i] 的答案都是独立的，即当你标记节点 i 时，所有其他节点都未标记。
#
#
#
# 示例 1：
#
# 输入：edges = [[0,1],[0,2]]
#
# 输出：[2,4,3]
#
# 解释：
#
#
#
# 对于 i = 0 ：
# 节点 1 在时刻 t = 1 被标记，节点 2 在时刻 t = 2 被标记。
# 对于 i = 1 ：
# 节点 0 在时刻 t = 2 被标记，节点 2 在时刻 t = 4 被标记。
# 对于 i = 2 ：
# 节点 0 在时刻 t = 2 被标记，节点 1 在时刻 t = 3 被标记。
# 示例 2：
#
# 输入：edges = [[0,1]]
#
# 输出：[1,2]
#
# 解释：
#
#
#
# 对于 i = 0 ：
# 节点 1 在时刻 t = 1 被标记。
# 对于 i = 1 ：
# 节点 0 在时刻 t = 2 被标记。
# 示例 3：
#
# 输入：edges = [[2,4],[0,1],[2,3],[0,2]]
#
# 输出：[4,6,3,5,5]
#
# 解释：
#
#
#
#
#
# 提示：
#
# 2 <= n <= 105
# edges.length == n - 1
# edges[i].length == 2
# 0 <= edges[i][0], edges[i][1] <= n - 1
# 输入保证 edges 表示一棵合法的树。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        n = len(edges) + 1
        ans = [0] * n
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        t = defaultdict(lambda: defaultdict(lambda: 0))  # x -> y 这条路，走完这个分支需要的总时间，走完整个分支的时间，是相对到达x的时间，x，y是相邻的
        h = defaultdict(list)  # 记录从每个点出发，所有路径的最大总时间，和次大总时间

        def dfs(x, fa):
            res = 0
            a1 = a2 = 0
            for y in g[x]:
                if y == fa: continue
                v = dfs(y, x)
                if y & 1:
                    t[x][y] = v + 1
                    res = max(res, v + 1)
                else:
                    t[x][y] = v + 2
                    res = max(res, v + 2)
                if t[x][y] > a1:
                    a1, a2 = t[x][y], a1
                elif t[x][y] > a2:
                    a2 = t[x][y]
            h[x] = [a1, a2]
            return res

        ans[0] = dfs(0, -1)

        # 计算所有 t[x][fa]
        def dfs2(x, fa):
            for y in g[x]:
                if y == fa: continue
                if t[x][y] == h[x][0]:
                    t[y][x] = h[x][1] + (1 if x & 1 else 2)
                else:
                    t[y][x] = h[x][0] + (1 if x & 1 else 2)
                if t[y][x] > h[y][0]:
                    h[y] = [t[y][x], h[y][0]]
                elif t[y][x] > h[y][1]:
                    h[y][1] = t[y][x]
                dfs2(y, x)

        dfs2(0, -1)

        ans = [h[i][0] for i in range(n)]
        return ans


so = Solution()
print(so.timeTaken([[5,4],[2,1],[4,2],[1,0],[3,1]]))
print(so.timeTaken([[1,0],[2,1],[5,3],[3,1],[6,1],[4,3]]))
print(so.timeTaken([[2,4],[0,1],[2,3],[0,2]]))
print(so.timeTaken([[0,1]]))
print(so.timeTaken([[0,1],[0,2]]))




