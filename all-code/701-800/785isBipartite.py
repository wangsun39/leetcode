
class Solution:
    def isBipartite(self, graph):
        self.graph = graph
        num = len(self.graph)
        list1, list2 = [], []
        for i in range(num):
            if i in list1 or i in list2:
                continue
            ret = self.isBipartiteRecursion(i, list1, list2)
            if not ret:
                return False
        return True
    def isBipartiteRecursion(self, node, list1, list2):
        if node in list1:
            return True
        list1.append(node)
        for i in self.graph[node]:
            if i in list1:
                return False
            ret = self.isBipartiteRecursion(i, list2, list1)
            if not ret:
                return False
        return True


so = Solution()
print(so.isBipartite([[1,3], [0,2], [1,3], [0,2]]))
print(so.isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]]))
print(so.isBipartite([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]))

