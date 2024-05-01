# 你有一个包含 n 个节点的图。给定一个整数 n 和一个数组 edges ，其中 edges[i] = [ai, bi] 表示图中 ai 和 bi 之间有一条边。
#
# 返回 图中已连接分量的数目 。
#
#
#
# 示例 1:
#
#
#
# 输入: n = 5, edges = [[0, 1], [1, 2], [3, 4]]
# 输出: 2
# 示例 2:
#
#
#
# 输入: n = 5, edges = [[0,1], [1,2], [2,3], [3,4]]
# 输出:  1
#
#
# 提示：
#
# 1 <= n <= 2000
# 1 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai <= bi < n
# ai != bi
# edges 中不会出现重复的边

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        fa = list(range(n))
        # fa = {x: x for x in nums}  # 另一种写法，x不连续
        def find(x):
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]
        def union(x, y):
            fa[find(y)] = find(x)
        for x, y in edges:
            union(x, y)
        for i in range(n):
            find(i)
        return len(set(fa))


so = Solution()
print(so.countComponents(n = 5, edges = [[0, 1], [1, 2], [3, 4]]))




