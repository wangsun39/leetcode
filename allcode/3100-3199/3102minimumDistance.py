# 给你一个下标从 0 开始的数组 points ，它表示二维平面上一些点的整数坐标，其中 points[i] = [xi, yi] 。
#
# 两点之间的距离定义为它们的
# 曼哈顿距离
# 。
#
# 请你恰好移除一个点，返回移除后任意两点之间的 最大 距离可能的 最小 值。
#
#
#
# 示例 1：
#
# 输入：points = [[3,10],[5,15],[10,2],[4,4]]
# 输出：12
# 解释：移除每个点后的最大距离如下所示：
# - 移除第 0 个点后，最大距离在点 (5, 15) 和 (10, 2) 之间，为 |5 - 10| + |15 - 2| = 18 。
# - 移除第 1 个点后，最大距离在点 (3, 10) 和 (10, 2) 之间，为 |3 - 10| + |10 - 2| = 15 。
# - 移除第 2 个点后，最大距离在点 (5, 15) 和 (4, 4) 之间，为 |5 - 4| + |15 - 4| = 12 。
# - 移除第 3 个点后，最大距离在点 (5, 15) 和 (10, 2) 之间的，为 |5 - 10| + |15 - 2| = 18 。
# 在恰好移除一个点后，任意两点之间的最大距离可能的最小值是 12 。
# 示例 2：
#
# 输入：points = [[1,1],[1,1],[1,1]]
# 输出：0
# 解释：移除任一点后，任意两点之间的最大距离都是 0 。
#
#
# 提示：
#
# 3 <= points.length <= 105
# points[i].length == 2
# 1 <= points[i][0], points[i][1] <= 108

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        l1, l2 = [], []
        for i, [x, y] in enumerate(points):
            l1.append([x - y, i])
            l2.append([x + y, i])
        l1.sort()
        l2.sort()
        ans = max(l1[-1][0] - l1[0][0], l2[-1][0] - l2[0][0])
        def calc(idx, l):
            # 删除下标idx的点，计算l中的最多差值是多少
            if l[0][1] == idx:
                res = l[-1][0] - l[1][0]
            elif l[-1][1] == idx:
                res = l[-2][0] - l[0][0]
            else:
                res = l[-1][0] - l[0][0]
            return res

        cur = max(l1[-1][0] - l1[1][0], calc(l1[0][1], l2))
        ans = min(ans, cur)

        cur = max(l1[-2][0] - l1[0][0], calc(l1[-1][1], l2))
        ans = min(ans, cur)

        cur = max(l2[-1][0] - l2[1][0], calc(l2[0][1], l1))
        ans = min(ans, cur)

        cur = max(l2[-2][0] - l2[0][0], calc(l2[-1][1], l1))
        ans = min(ans, cur)
        return ans



so = Solution()
print(so.minimumDistance(points = [[3,10],[5,15],[10,2],[4,4]]))
print(so.minimumDistance(points = [[4,1],[10,7],[5,6],[3,2],[10,9],[2,9],[2,8]]))
print(so.minimumDistance(points = [[1,1],[1,1],[1,1]]))




