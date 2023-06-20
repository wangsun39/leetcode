# 给你两组点，其中第一组中有 size1 个点，第二组中有 size2 个点，且 size1 >= size2 。
#
# 任意两点间的连接成本 cost 由大小为 size1 x size2 矩阵给出，其中 cost[i][j] 是第一组中的点 i 和第二组中的点 j 的连接成本。如果两个组中的每个点都与另一组中的一个或多个点连接，则称这两组点是连通的。换言之，第一组中的每个点必须至少与第二组中的一个点连接，且第二组中的每个点必须至少与第一组中的一个点连接。
#
# 返回连通两组点所需的最小成本。
#
#
#
# 示例 1：
#
#
#
# 输入：cost = [[15, 96], [36, 2]]
# 输出：17
# 解释：连通两组点的最佳方法是：
# 1--A
# 2--B
# 总成本为 17 。
# 示例 2：
#
#
#
# 输入：cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
# 输出：4
# 解释：连通两组点的最佳方法是：
# 1--A
# 2--B
# 2--C
# 3--A
# 最小成本为 4 。
# 请注意，虽然有多个点连接到第一组中的点 2 和第二组中的点 A ，但由于题目并不限制连接点的数目，所以只需要关心最低总成本。
# 示例 3：
#
# 输入：cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
# 输出：10
#
#
# 提示：
#
# size1 == cost.length
# size2 == cost[i].length
# 1 <= size1, size2 <= 12
# size1 >= size2
# 0 <= cost[i][j] <= 100
from functools import cache
from math import inf
from typing import Optional
from collections import deque
# Definition for a binary tree node.
from typing import List

class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        n1, n2 = len(cost), len(cost[0])
        min_cost = [min(x) for x in zip(*cost)]  # min_cost[i] 表示第 2 组中第i个点与左边各点中最小的花费

        @cache
        def dfs(i_l, mask_r):  # 左边前 i_l + 1 个，右两边未连过的点集合
            # 这里左边的点并不需要像右边的点一样用一个掩码记录所有可能，开始只需要枚举左边的点i与右边的某一个点j相连的情况
            # 然后dfs，再最后一步中，如果右边还有点没有被覆盖，可以把未覆盖的点依次找到一个左边的最小花费点连上就可以了
            if i_l == -1:
                return sum([min_cost[i] for i in range(n2) if mask_r & (1 << i)])
            res = inf
            for i in range(n2):
                res = min(res, dfs(i_l - 1, mask_r & ~(1 << i)) + cost[i_l][i])
            return res

        return dfs(n1 - 1, 2 ** n2 - 1)




so = Solution()
print(so.connectTwoGroups([[1, 3, 5], [4, 1, 1], [1, 5, 3]]))
print(so.connectTwoGroups([[15, 96], [36, 2]]))


