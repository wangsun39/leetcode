# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
#
# 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
#
# 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
#
#  
#
# 示例 1：
#
# 输入：numCourses = 2, prerequisites = [[1,0]]
# 输出：true
# 解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
# 示例 2：
#
# 输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
# 输出：false
# 解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
#  
#
# 提示：
#
# 1 <= numCourses <= 105
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# prerequisites[i] 中的所有课程对 互不相同



from typing import List

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


    def canFinish1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def topo():
            ans = []
            graph = defaultdict(list)
            preNum = [0] * numCourses
            queue = []
            for x, y in prerequisites:
                graph[y].append(x)
                preNum[x] += 1
            for i in range(numCourses):
                if preNum[i] == 0:
                    queue.append(i)
            while len(queue):
                x = queue.pop(0)
                ans.append(x)
                for y in graph[x]:
                    preNum[y] -= 1
                    if preNum[y] == 0:
                        queue.append(y)
            return ans
        ans = topo()
        return len(ans) == numCourses

so = Solution()
#print(so.findKthLargest([3,2,1,5,6,4], 2))
#print(so.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
#print(so.findKthLargest([7,6,5,4,3,2,1], 5))
print(so.canFinish(2, [[1,0]]))
print(so.canFinish(2, [[1,0],[0,1]]))

