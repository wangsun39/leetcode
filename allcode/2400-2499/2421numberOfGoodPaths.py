# 给你一棵 n个节点的树（连通无向无环的图），节点编号从0到n - 1且恰好有n - 1条边。
#
# 给你一个长度为 n下标从 0开始的整数数组vals，分别表示每个节点的值。同时给你一个二维整数数组edges，其中edges[i] = [ai, bi]表示节点ai 和bi之间有一条无向边。
#
# 一条 好路径需要满足以下条件：
#
# 开始节点和结束节点的值 相同。
# 开始节点和结束节点中间的所有节点值都 小于等于开始节点的值（也就是说开始节点的值应该是路径上所有节点的最大值）。
# 请你返回不同好路径的数目。
#
# 注意，一条路径和它反向的路径算作 同一路径。比方说，0 -> 1与1 -> 0视为同一条路径。单个节点也视为一条合法路径。
#
#
#
# 示例1：
#
#
#
# 输入：vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]
# 输出：6
# 解释：总共有 5 条单个节点的好路径。
# 还有 1 条好路径：1 -> 0 -> 2 -> 4 。
# （反方向的路径 4 -> 2 -> 0 -> 1 视为跟 1 -> 0 -> 2 -> 4 一样的路径）
# 注意 0 -> 2 -> 3 不是一条好路径，因为 vals[2] > vals[0] 。
# 示例 2：
#
#
#
# 输入：vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]]
# 输出：7
# 解释：总共有 5 条单个节点的好路径。
# 还有 2 条好路径：0 -> 1 和 2 -> 3 。
# 示例 3：
#
#
#
# 输入：vals = [1], edges = []
# 输出：1
# 解释：这棵树只有一个节点，所以只有一条好路径。
#
#
# 提示：
#
# n == vals.length
# 1 <= n <= 3 * 104
# 0 <= vals[i] <= 105
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# edges表示一棵合法的树。
#
# https://leetcode.cn/problems/number-of-good-paths


from leetcode.allcode.competition.mypackage import *

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        adj = defaultdict(list)
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        fa = list(range(n))  # 存放每个点所在连通块的代表元（未必每个点的fa值都是最新的，调用find获取，不要直接fa[i]获取）
        def find(x):
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]

        size = [1] * n  # 存放每个点所属连通块内，具有最大值的节点个数（一般只有每个连通块的代表元的size值是准确的）
        ans = n
        for vx, x in sorted(zip(vals, range(n))):
            fx = find(x)   # 路径压缩 + 找到代表元
            for y in adj[x]:
                y = find(y)  # x, y 之间不比较，而是用他们的代表元进行比较
                if y == fx or vals[y] > vx:  # y == fx 说明y节点已在x节点之前就处理过了，不能重复统计
                    continue
                # 把 x 和 y 所在的连通块合并
                if vals[y] == vx:  # 具有好路径
                    ans += size[y] * size[fa[x]]
                    size[fx] += size[y]
                fa[y] = fx
        return ans





so = Solution()
print(so.numberOfGoodPaths([2,5,5,1,5,2,3,5,1,5], [[0,1],[2,1],[3,2],[3,4],[3,5],[5,6],[1,7],[8,4],[9,7]]))
print(so.numberOfGoodPaths(vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]]))
print(so.numberOfGoodPaths(vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]))
print(so.numberOfGoodPaths(vals = [1], edges = []))




