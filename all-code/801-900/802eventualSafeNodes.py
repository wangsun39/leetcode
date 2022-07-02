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

    def eventualSafeNodes(self, graph):
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


so = Solution()
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
print(so.eventualSafeNodes(graph))

