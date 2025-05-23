# 你总共需要上numCourses门课，课程编号依次为 0到numCourses-1。你会得到一个数组prerequisite ，其中prerequisites[i] = [ai, bi]表示如果你想选bi 课程，你 必须 先选ai课程。
#
# 有的课会有直接的先修课程，比如如果想上课程 1，你必须先上课程 0，那么会以 [0,1]数对的形式给出先修课程数对。
# 先决条件也可以是 间接 的。如果课程 a 是课程 b 的先决条件，课程 b 是课程 c 的先决条件，那么课程 a 就是课程 c 的先决条件。
#
# 你也得到一个数组queries，其中queries[j] = [uj, vj]。对于第 j 个查询，您应该回答课程uj是否是课程vj的先决条件。
#
# 返回一个布尔数组 answer ，其中 answer[j] 是第 j 个查询的答案。
#
#
#
# 示例 1：
#
#
#
# 输入：numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
# 输出：[false,true]
# 解释：课程 0 不是课程 1 的先修课程，但课程 1 是课程 0 的先修课程。
# 示例 2：
#
# 输入：numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
# 输出：[false,false]
# 解释：没有先修课程对，所以每门课程之间是独立的。
# 示例 3：
#
#
#
# 输入：numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
# 输出：[true,true]
#
#
# 提示：
#
# 2 <= numCourses <= 100
# 0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)
# prerequisites[i].length == 2
# 0 <= ai, bi<= n - 1
# ai!= bi
# 每一对[ai, bi]都 不同
# 先修课程图中没有环。
# 0 <= ui, vi<= n - 1
# ui!= vi



from leetcode.allcode.competition.mypackage import *

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        preC = defaultdict(set)
        def update(c, p):
            for x in preC:
                if c in preC[x]:
                    preC[x].add(p)
            preC[c].add(p)
        for x, y in prerequisites:
            preC[y] |= preC[x]
            update(y, x)
        ans = []
        for q in queries:
            ans.append(True if q[0] in preC[q[1]] else False)
        return ans

so = Solution()
print(so.checkIfPrerequisite(numCourses = 5, prerequisites = [[0,1],[1,2],[2,3],[3,4]], queries = [[0,4],[4,0],[1,3],[3,0]]))
print(so.checkIfPrerequisite(numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]))
print(so.checkIfPrerequisite(numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]))
print(so.checkIfPrerequisite(numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]))




