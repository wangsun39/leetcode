from leetcode.allcode.competition.mypackage import *, deque

# 树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，一个任何没有简单环路的连通图都是一棵树。
#
# 给你一棵包含 n 个节点的树，标记为 0 到 n - 1 。给定数字 n 和一个有 n - 1 条无向边的 edges 列表（每一个边都是一对标签），其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条无向边。
#
# 可选择树中任何一个节点作为根。当选择节点 x 作为根节点时，设结果树的高度为 h 。在所有可能的树中，具有最小高度的树（即，min(h)）被称为 最小高度树 。
#
# 请你找到所有的 最小高度树 并按 任意顺序 返回它们的根节点标签列表。
#
# 树的 高度 是指根节点和叶子节点之间最长向下路径上边的数量。
#
#
# 示例 1：
#
#
# 输入：n = 4, edges = [[1,0],[1,2],[1,3]]
# 输出：[1]
# 解释：如图所示，当根是标签为 1 的节点时，树的高度是 1 ，这是唯一的最小高度树。
# 示例 2：
#
#
# 输入：n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
# 输出：[3,4]
#
#
# 提示：
#
# 1 <= n <= 2 * 104
# edges.length == n - 1
# 0 <= ai, bi < n
# ai != bi
# 所有 (ai, bi) 互不相同
# 给定的输入 保证 是一棵树，并且 不会有重复的边


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2: return [x for x in range(n)]
        graph = defaultdict(set)
        for x, y in edges:
            graph[x].add(y)
            graph[y].add(x)
        queue = deque([x for x in graph if len(graph[x]) == 1])
        queue.append('|')
        search_num = 0
        while len(queue) > 1:
            e = queue.popleft()
            if e == '|':
                if n - search_num == len(queue) <= 2:
                    return list(queue)
                queue.append(e)
                continue
            search_num += 1
            for x in graph[e]:
                graph[x].remove(e)
                if len(graph[x]) == 1:
                    queue.append(x)




so = Solution()
print(so.findMinHeightTrees(n = 6, edges = [[0,1],[0,2],[0,3],[3,4],[4,5]]))
print(so.findMinHeightTrees(n = 2, edges = [[0,1]]))
print(so.findMinHeightTrees(n = 1, edges = []))
print(so.findMinHeightTrees(n = 4, edges = [[1,0],[1,2],[1,3]]))
print(so.findMinHeightTrees(n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]))

