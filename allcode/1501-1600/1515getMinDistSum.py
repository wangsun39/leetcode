# 一家快递公司希望在新城市建立新的服务中心。公司统计了该城市所有客户在二维地图上的坐标，并希望能够以此为依据为新的服务中心选址：使服务中心 到所有客户的欧几里得距离的总和最小 。
#
# 给你一个数组 positions ，其中 positions[i] = [xi, yi] 表示第 i 个客户在二维地图上的位置，返回到所有客户的 欧几里得距离的最小总和 。
#
# 换句话说，请你为服务中心选址，该位置的坐标 [xcentre, ycentre] 需要使下面的公式取到最小值：
#
#
#
# 与真实值误差在 10-5之内的答案将被视作正确答案。
#
#
#
# 示例 1：
#
#
#
# 输入：positions = [[0,1],[1,0],[1,2],[2,1]]
# 输出：4.00000
# 解释：如图所示，你可以选 [xcentre, ycentre] = [1, 1] 作为新中心的位置，这样一来到每个客户的距离就都是 1，所有距离之和为 4 ，这也是可以找到的最小值。
# 示例 2：
#
#
#
# 输入：positions = [[1,1],[3,3]]
# 输出：2.82843
# 解释：欧几里得距离可能的最小总和为 sqrt(2) + sqrt(2) = 2.82843
#
#
# 提示：
#
# 1 <= positions.length <= 50
# positions[i].length == 2
# 0 <= xi, yi <= 100

from leetcode.allcode.competition.mypackage import *

class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        n = len(positions)
        def dist(x0, y0):
            return sum(((x - x0) ** 2 + (y - y0) ** 2) ** 0.5 for x, y in positions)
        left, right = min(positions[i][0] for i in range(n)), max(positions[i][0] for i in range(n))
        down, up = min(positions[i][1] for i in range(n)), max(positions[i][1] for i in range(n))
        d1 = d2 = dist(positions[0][0], positions[0][1])

        def calc(x0):  # 在 x = x0上找到最小值对应的y坐标
            hi, lo = up, down
            while hi - lo > 10 ** (-7):
                y1, y2 = (2 * lo + hi) / 3, (lo + 2 * hi) / 3
                d1, d2 = dist(x0, y1), dist(x0, y2)
                if d1 < d2:
                    hi = y2
                else:
                    lo = y1
            return min(d1, d2)

        while right - left > 10 ** (-7):
            x1, x2 = (2 * left + right) / 3, (left + 2 * right) / 3
            d1, d2 = calc(x1), calc(x2)
            if d1 < d2:
                right = x2
            else:
                left = x1
        return min(d1, d2)



so = Solution()
print(so.getMinDistSum([[58,32],[41,21]]))
print(so.getMinDistSum([[1,1],[0,0],[2,0]]))
print(so.getMinDistSum([[0,1],[1,0],[1,2],[2,1]]))
print(so.getMinDistSum([[1,1],[3,3]]))




