class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:
        self.adjDict = self.getAdjNode(prerequisites)
        self.haveCheckNode = []
        for node in self.adjDict:
            if node not in self.haveCheckNode:
                self.haveCheckNode.append(node)
                ret = self.isExistCycle(node, [])
                if not ret:
                    return False
        return True

    def getAdjNode(self, graph):
        d = {}
        for edge in graph:
            if edge[0] not in d:
                d[edge[0]] = [edge[1]]
            else:
                if edge[1] not in d[edge[0]]:
                    d[edge[0]].append(edge[1])
        return d
    def isExistCycle(self, node, link_in):
        link = link_in[:]
        link.append(node)
        self.haveCheckNode.append(node)
        if node not in self.adjDict:
            return True
        for adj in self.adjDict[node]:
            if adj not in link:
                ret = self.isExistCycle(adj, link)
                if not ret:
                    return False
            else:
                return False
        return True

so = Solution()
#print(so.findKthLargest([3,2,1,5,6,4], 2))
#print(so.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
#print(so.findKthLargest([7,6,5,4,3,2,1], 5))
print(so.canFinish(2, [[1,0]]))
print(so.canFinish(2, [[1,0],[0,1]]))

