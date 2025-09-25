# 有一个有 n 个节点的有向图，节点按 0 到 n - 1 编号。图由一个 索引从 0 开始 的 2D 整数数组 graph表示， graph[i]是与节点 i 相邻的节点的整数数组，这意味着从节点 i 到 graph[i]中的每个节点都有一条边。
#
# 如果一个节点没有连出的有向边，则它是 终端节点 。如果没有出边，则节点为终端节点。如果从该节点开始的所有可能路径都通向 终端节点 ，则该节点为 安全节点 。
#
# 返回一个由图中所有 安全节点 组成的数组作为答案。答案数组中的元素应当按 升序 排列。
#
#
#
# 示例 1：
#
# Illustration of graph
#
# 输入：graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# 输出：[2,4,5,6]
# 解释：示意图如上。
# 节点 5 和节点 6 是终端节点，因为它们都没有出边。
# 从节点 2、4、5 和 6 开始的所有路径都指向节点 5 或 6 。
# 示例 2：
#
# 输入：graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
# 输出：[4]
# 解释:
# 只有节点 4 是终端节点，从节点 4 开始的所有路径都通向节点 4 。
#
#
# 提示：
#
# n == graph.length
# 1 <= n <= 104
# 0 <= graph[i].length <= n
# 0 <= graph[i][j] <= n - 1
# graph[i] 按严格递增顺序排列。
# 图中可能包含自环。
# 图中边的数目在范围 [1, 4 * 104] 内。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def recurseMarkNodes(self, L, node):
        if self.nodeMark[node] == ['check', 'unsafe'] or node in L:
            for i in L:
                self.nodeMark[i] = ['check', 'unsafe']
            return
        if self.nodeMark[node] == ['check', 'safe']:
            return
        for i in self.graph[node]:
            self.recurseMarkNodes(L + [node], i)
            # print(self.nodeMark)
            if self.nodeMark[node] == ['check', 'unsafe']:
                return
        self.nodeMark[node] = ['check', 'safe']
        return

    def eventualSafeNodes1(self, graph):
        self.nodeMark = {}
        self.graph = graph
        for i in range(len(graph)):
            self.nodeMark[i] = ['uncheck', None]
        for key in self.nodeMark:
            self.recurseMarkNodes([], key)
        result = []
        for key in self.nodeMark:
            if self.nodeMark[key] == ['check', 'safe']:
                result.append(key)
        # print(self.nodeMark)
        return result

    def eventualSafeNodes(self, graph):
        # 2023/1/18 拓扑排序 模板
        def buildTopo(conditions, n):
            tree = defaultdict(set)
            pre_num = [0] * n
            for x, y in conditions:
                if y not in tree[x]:
                    tree[x].add(y)
                    pre_num[y] += 1
            queue = deque([i for i in range(n) if pre_num[i] == 0]) # deque 在操作大数组时，性能比 list 好很多
            ans = []
            while len(queue):
                q = queue.popleft()
                ans.append(q)
                for x in tree[q]:
                    pre_num[x] -= 1
                    if pre_num[x] == 0:
                        queue.append(x)
            # if len(ans) != n:
            #     return []  # 存在圈
            return ans
        rev_graph = []
        n = len(graph)
        # 把图把图翻转
        for i, s in enumerate(graph):
            rev_graph += [[x, i] for x in s]
        ans = buildTopo(rev_graph, n)
        return sorted(ans)

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # 2023/3/18 拓扑排序
        g = defaultdict(set)
        n = len(graph)
        pre_num = [0] * n
        for i, adj in enumerate(graph):
            for j in adj:
                g[j].add(i)
                pre_num[i] += 1
        queue = deque([i for i in range(n) if pre_num[i] == 0]) # deque 在操作大数组时，性能比 list 好很多
        ans = []
        while len(queue):
            q = queue.popleft()
            ans.append(q)
            for x in g[q]:
                pre_num[x] -= 1
                if pre_num[x] == 0:
                    queue.append(x)
        return sorted(ans)


so = Solution()
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
print(so.eventualSafeNodes(graph))

