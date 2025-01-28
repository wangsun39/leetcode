# 假如有一排房子，共 n 个，每个房子可以被粉刷成红色、蓝色或者绿色这三种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。
#
# 当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。每个房子粉刷成不同颜色的花费是以一个n x 3的正整数矩阵 costs 来表示的。
#
# 例如，costs[0][0] 表示第 0 号房子粉刷成红色的成本花费；costs[1][2]表示第 1 号房子粉刷成绿色的花费，以此类推。
#
# 请计算出粉刷完所有房子最少的花费成本。
#
#
#
# 示例 1：
#
# 输入: costs = [[17,2,17],[16,16,5],[14,3,19]]
# 输出: 10
# 解释: 将 0 号房子粉刷成蓝色，1 号房子粉刷成绿色，2 号房子粉刷成蓝色。
#     最少花费: 2 + 5 + 3 = 10。
# 示例 2：
#
# 输入: costs = [[7,6,2]]
# 输出: 2
#
#
# 提示:
#
# costs.length == n
# costs[i].length == 3
# 1 <= n <= 100
# 1 <= costs[i][j] <= 20



from leetcode.allcode.competition.mypackage import *


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        d = [[float("inf") for _ in range(3)] for _ in range(n)]
        d[0] = costs[0]

        for i in range(1, n):
            d[i][0] = min(d[i - 1][1], d[i - 1][2]) + costs[i][0]
            d[i][1] = min(d[i - 1][0], d[i - 1][2]) + costs[i][1]
            d[i][2] = min(d[i - 1][1], d[i - 1][0]) + costs[i][2]
        return min(d[-1])




so = Solution()
print(so.minCost([[17,2,17],[16,16,5],[14,3,19]]))




