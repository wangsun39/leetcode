# 给你一棵含有 n 个节点的树，节点编号从 0 到 n - 1，用一个二维整数数组 edges 表示。edges[i] = [ui, vi, ci] 表示节点 ui 和 vi 之间的一条边，其开销为 ci。
#
# 同时给你一个长度为 n 的整数数组 values，其中 values[i] 是节点 i 的值。
#
# 如果两个 不同 节点之间的路径上所有节点（包括两个端点）的值的按位异或结果在二进制表示中含有 偶数 个置位，则称该路径为 平衡异或 路径。
#
# 一条路径的 开销 是其所有边开销的总和。
#
# 返回一条平衡异或路径的 最小开销 。如果不存在这样的路径，返回 -1。
#
# 置位 是指一个数字的二进制表示中值为 1 的位。数字 0 含有零个置位。
#
#
#
# 示例 1：
#
#
#
# 输入： edges = [[0,1,4],[0,2,6],[0,3,3],[3,4,5]], values = [3,1,7,1,3]
#
# 输出： 7
#
# 解释：
#
# 平衡异或路径	异或值	总开销
# 1 - 0 - 2	1 XOR 3 XOR 7 = 5	4 + 6 = 10
# 1 - 0 - 3	1 XOR 3 XOR 1 = 3	4 + 3 = 7
# 1 - 0 - 3 - 4	1 XOR 3 XOR 1 XOR 3 = 0	4 + 3 + 5 = 12
# 2 - 0 - 3	7 XOR 3 XOR 1 = 5	6 + 3 = 9
# 2 - 0 - 3 - 4	7 XOR 3 XOR 1 XOR 3 = 6	6 + 3 + 5 = 14
# 最小开销为 7，由路径 1 - 0 - 3 达成。因此，答案为 7。
#
# 示例 2：
#
#
#
# 输入： edges = [[0,1,5],[1,2,10]], values = [1,7,3]
#
# 输出： 5
#
# 解释：
#
# 平衡异或路径	异或值	总开销
# 0 - 1	1 XOR 7 = 6	5
# 0 - 1 - 2	1 XOR 7 XOR 3 = 5	5 + 10 = 15
# 最小开销为 5，由路径 0 - 1 达成。因此，答案为 5。
#
# 示例 3：
#
#
#
# 输入： edges = [[0,1,5],[0,2,7],[0,3,9]], values = [1,3,5,9]
#
# 输出： -1
#
# 解释：
#
# 任意两个不同节点之间的路径异或值在二进制下都含有奇数个置位。
# 因此，不存在平衡异或路径，所以答案为 -1。
#
#
# 提示：
#
# 2 <= n <= 105
# edges.length == n - 1
# edges[i] = [ui, vi, ci]
# 0 <= ui, vi <= n - 1
# 1 <= ci <= 109
# values.length == n
# 1 <= values[i] <= 109
# edges 表示一棵合法的树。

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def minActivationCost(self, edges: list[list[int]], values: list[int]) -> int:
        values = [x.bit_count() % 2 for x in values]  # 将 values的值都变成它们数位为1的数量的奇偶性，具体的值是没有意义的
        g = defaultdict(list)
        for x, y, w in edges:
            g[x].append([y, w])
            g[y].append([x, w])

        ans = inf
        def dfs(x, fa):
            # 以 x 为根节点的子树
            # 返回 以 x 为一端，异或值为奇数的最大开销，和异或值为偶数的最大开销

            nonlocal ans
            even = odds = inf
            if values[x]:  # x 数位位奇数
                odds = 0
                for y, w in g[x]:
                    if y == fa: continue
                    r1, r2 = dfs(y, x)
                    ans = MIN(ans, r2 + w)
                # 这种情况，不存在两个子树拼成一个路径满足异或和为偶数
            else:
                even = 0
                ol = []  # 子树中奇数返回值的最小的两个
                for y, w in g[x]:
                    if y == fa: continue
                    r1, r2 = dfs(y, x)
                    ans = MIN(ans, r1 + w)
                    if r2 < inf:
                        odds = MIN(odds, r2 + w)
                        ol.append(r2 + w)
                        if len(ol) > 2:
                            ol.sort()
                            ol = ol[:2]
                if len(ol) == 2:
                    ans = MIN(ans, sum(ol))


            return even, odds

        dfs(0, -1)
        if ans != inf:
            return ans
        return -1



so = Solution()
print(so.minActivationCost(edges = [[1,0,3],[2,1,6],[3,1,1],[4,0,4],[5,1,8],[6,5,9],[7,3,5]], values = [4,5,10,2,6,6,1,8]))
print(so.minActivationCost(edges = [[0,1,5],[0,2,7],[0,3,9]], values = [1,3,5,9]))
print(so.minActivationCost(edges = [[0,1,4],[0,2,6],[0,3,3],[3,4,5]], values = [3,1,7,1,3]))


