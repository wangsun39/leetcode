from collections import defaultdict

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


so = Solution()
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
print(so.eventualSafeNodes(graph))

