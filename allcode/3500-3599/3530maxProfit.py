# 给你一个由 n 个节点组成的有向无环图（DAG），节点编号从 0 到 n - 1，通过二维数组 edges 表示，其中 edges[i] = [ui, vi] 表示一条从节点 ui 指向节点 vi 的有向边。每个节点都有一个对应的 得分 ，由数组 score 给出，其中 score[i] 表示节点 i 的得分。
#
# 你需要以 有效的拓扑排序 顺序处理这些节点。每个节点在处理顺序中被分配一个编号从 1 开始的位置。
#
# 将每个节点的得分乘以其在拓扑排序中的位置，然后求和，得到的值称为 利润。
#
# 请返回在所有合法拓扑排序中可获得的 最大利润 。
#
# 拓扑排序 是一个对 DAG 中所有节点的线性排序，使得每条有向边 u → v 中，节点 u 都出现在 v 之前。
#
#
#
# 示例 1：
#
# 输入： n = 2, edges = [[0,1]], score = [2,3]
#
# 输出： 8
#
# 解释：
#
#
#
# 节点 1 依赖于节点 0，因此一个合法顺序是 [0, 1]。
#
# 节点	处理顺序	得分	乘数	利润计算
# 0	第 1 个	2	1	2 × 1 = 2
# 1	第 2 个	3	2	3 × 2 = 6
# 所有合法拓扑排序中可获得的最大总利润是 2 + 6 = 8。
#
# 示例 2：
#
# 输入： n = 3, edges = [[0,1],[0,2]], score = [1,6,3]
#
# 输出： 25
#
# 解释：
#
#
#
# 节点 1 和 2 都依赖于节点 0，因此最优的合法顺序是 [0, 2, 1]。
#
# 节点	处理顺序	得分	乘数	利润计算
# 0	第 1 个	1	1	1 × 1 = 1
# 2	第 2 个	3	2	3 × 2 = 6
# 1	第 3 个	6	3	6 × 3 = 18
# 所有合法拓扑排序中可获得的最大总利润是 1 + 6 + 18 = 25。
#
#
#
# 提示：
#
# 1 <= n == score.length <= 22
# 1 <= score[i] <= 105
# 0 <= edges.length <= n * (n - 1) / 2
# edges[i] == [ui, vi] 表示一条从 ui 到 vi 的有向边。
# 0 <= ui, vi < n
# ui != vi
# 输入图 保证 是一个 DAG。
# 不存在重复的边。

from leetcode.allcode.competition.mypackage import *

MAX = lambda a, b: b if b > a else a

class Solution:
    class Solution:
        def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
            if not edges:
                score.sort()
                return sum(s * i for i, s in enumerate(score, 1))

            g = defaultdict(list)
            pre_num = [0] * n
            for x, y in edges:
                if y not in g[x]:
                    g[x].append(y)
                    pre_num[y] += 1
            queue = deque([i for i in range(n) if pre_num[i] == 0])  # deque 在操作大数组时，性能比 list 好很多

            @cache
            def dfs(vis):
                if vis == (1 << n) - 1:
                    return 0

                start = vis.bit_count() + 1
                res = 0
                m = len(queue)
                for _ in range(m):
                    x = queue.popleft()
                    vis ^= (1 << x)
                    for y in g[x]:
                        pre_num[y] -= 1
                        if pre_num[y] == 0:
                            queue.append(y)
                    res = max(res, dfs(vis) + score[x] * start)
                    # 恢复现场
                    for y in g[x][::-1]:
                        pre_num[y] += 1
                        if queue and queue[-1] == y:
                            queue.pop()
                    vis ^= (1 << x)
                    queue.append(x)

                return res

            return dfs(0)

    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        # 优化后的简洁写法
        if not edges:
            score.sort()
            return sum(s * i for i, s in enumerate(score, 1))

        pre = [0] * n  # 前面元素的状压
        for x, y in edges:
            pre[y] |= (1 << x)

        @cache
        def dfs(vis):
            if vis == (1 << n) - 1:
                return 0

            start = vis.bit_count() + 1
            res = 0
            for i in range(n):
                if vis & (1 << i): continue
                if (pre[i] & vis) == pre[i]:  # 判断前序节点是否都访问过了
                    v = dfs(vis ^ (1 << i)) + start * score[i]
                    res = MAX(res, v)
            return res

        return dfs(0)




so = Solution()
print(so.maxProfit(n = 2, edges = [[0,1]], score = [2,3]))  # 8
print(so.maxProfit(n = 3, edges = [[0,1]], score = [21915,50942,52739]))
print(so.maxProfit(n = 3, edges = [[0,1],[0,2]], score = [1,6,3]))   # 25




