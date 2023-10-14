# 现有一个有向图，其中包含 n 个节点，节点编号从 0 到 n - 1 。此外，该图还包含了 n 条有向边。
#
# 给你一个下标从 0 开始的数组 edges ，其中 edges[i] 表示存在一条从节点 i 到节点 edges[i] 的边。
#
# 想象在图上发生以下过程：
#
# 你从节点 x 开始，通过边访问其他节点，直到你在 此过程 中再次访问到之前已经访问过的节点。
# 返回数组 answer 作为答案，其中 answer[i] 表示如果从节点 i 开始执行该过程，你可以访问到的不同节点数。
#
#
#
# 示例 1：
#
#
# 输入：edges = [1,2,0,0]
# 输出：[3,3,3,4]
# 解释：从每个节点开始执行该过程，记录如下：
# - 从节点 0 开始，访问节点 0 -> 1 -> 2 -> 0 。访问的不同节点数是 3 。
# - 从节点 1 开始，访问节点 1 -> 2 -> 0 -> 1 。访问的不同节点数是 3 。
# - 从节点 2 开始，访问节点 2 -> 0 -> 1 -> 2 。访问的不同节点数是 3 。
# - 从节点 3 开始，访问节点 3 -> 0 -> 1 -> 2 -> 0 。访问的不同节点数是 4 。
# 示例 2：
#
#
# 输入：edges = [1,2,3,4,0]
# 输出：[5,5,5,5,5]
# 解释：无论从哪个节点开始，在这个过程中，都可以访问到图中的每一个节点。
#
#
# 提示：
#
# n == edges.length
# 2 <= n <= 105
# 0 <= edges[i] <= n - 1
# edges[i] != i

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        ans = [-1] * n
        def f(x):
            i = 0
            vis = {}
            while x not in vis:
                if ans[x] != -1:
                    for y in vis.keys():
                        ans[y] = i - vis[y] + ans[x]
                    return
                vis[x] = i
                i += 1
                x = edges[x]
            for k, v in vis.items():
                if v < vis[x]:
                    ans[k] = i - v
                else:
                    ans[k] = i - vis[x]
        for i in range(n):
            if ans[i] == -1:
                f(i)
        return ans




so = Solution()
print(so.countVisitedNodes([1,2,0,0]))
print(so.countVisitedNodes(edges = [1,2,3,4,0]))




