# Alice 和 Bob 共有一个无向图，其中包含 n 个节点和 3  种类型的边：
#
# 类型 1：只能由 Alice 遍历。
# 类型 2：只能由 Bob 遍历。
# 类型 3：Alice 和 Bob 都可以遍历。
# 给你一个数组 edges ，其中 edges[i] = [typei, ui, vi] 表示节点 ui 和 vi 之间存在类型为 typei 的双向边。请你在保证图仍能够被 Alice和 Bob 完全遍历的前提下，找出可以删除的最大边数。如果从任何节点开始，Alice 和 Bob 都可以到达所有其他节点，则认为图是可以完全遍历的。
#
# 返回可以删除的最大边数，如果 Alice 和 Bob 无法完全遍历图，则返回 -1 。
#
#
#
# 示例 1：
#
#
#
# 输入：n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
# 输出：2
# 解释：如果删除 [1,1,2] 和 [1,1,3] 这两条边，Alice 和 Bob 仍然可以完全遍历这个图。再删除任何其他的边都无法保证图可以完全遍历。所以可以删除的最大边数是 2 。
# 示例 2：
#
#
#
# 输入：n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
# 输出：0
# 解释：注意，删除任何一条边都会使 Alice 和 Bob 无法完全遍历这个图。
# 示例 3：
#
#
#
# 输入：n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
# 输出：-1
# 解释：在当前图中，Alice 无法从其他节点到达节点 4 。类似地，Bob 也不能达到节点 1 。因此，图无法完全遍历。
#
#
# 提示：
#
# 1 <= n <= 10^5
# 1 <= edges.length <= min(10^5, 3 * n * (n-1) / 2)
# edges[i].length == 3
# 1 <= edges[i][0] <= 3
# 1 <= edges[i][1] < edges[i][2] <= n
# 所有元组 (typei, ui, vi) 互不相同

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        fa = list(range(n))
        # fa = {x: x for x in nums}  # 另一种写法，x不连续
        def find(x):
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]
        def union(x, y):
            fa[find(y)] = find(x)

        alice = []
        bob = []
        both = []
        for type, x, y in edges:
            if type == 1:
                alice.append([x - 1, y - 1])
            elif type == 2:
                bob.append([x - 1, y - 1])
            elif type == 3:
                both.append([x - 1, y - 1])
        nr_both = nr_alice = nr_bob = 0
        for x, y in both:
            if find(x) != find(y):
                union(x, y)
                nr_both += 1
        fa2 = fa[:]  # 备份一份给bob用
        for x, y in alice:
            if find(x) != find(y):
                union(x, y)
                nr_alice += 1
        if any(find(x) != find(0) for x in range(n)):
            return -1
        fa = fa2[:]  # 恢复
        for x, y in bob:
            if find(x) != find(y):
                union(x, y)
                nr_bob += 1
        if any(find(x) != find(0) for x in range(n)):
            return -1
        return len(edges) - nr_both - nr_alice - nr_bob




so = Solution()
print(so.maxNumEdgesToRemove(n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]))
print(so.maxNumEdgesToRemove(n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]))
print(so.maxNumEdgesToRemove(n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]))




