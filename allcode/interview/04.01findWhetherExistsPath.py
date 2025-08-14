# 节点间通路。给定有向图，设计一个算法，找出两个节点之间是否存在一条路径。
#
# 示例 1：
#
#  输入：n = 3, graph = [[0, 1], [0, 2], [1, 2], [1, 2]], start = 0, target = 2
#  输出：true
# 示例 2：
#
#  输入：n = 5, graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]], start = 0, target = 4
#  输出：true
# 提示：
#
# 节点数量n在[0, 1e5]范围内。
# 节点编号大于等于 0 小于 n。
# 图中可能存在自环和平行边。


from leetcode.allcode.competition.mypackage import *

class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        g = defaultdict(list)
        if start == target: return True
        vis = {start}
        for x, y in graph:
            g[x].append(y)

        def dfs(x):
            for y in g[x]:
                if y == target: return True
                if y in vis: continue
                if dfs(y): return True
                vis.add(y)
            return False
        return dfs(start)




so = Solution()
print(so.findWhetherExistsPath(n = 3, graph = [[0, 1], [0, 2], [1, 2], [1, 2]], start = 0, target = 2))




