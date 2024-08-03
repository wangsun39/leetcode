# 给定两个正方形及一个二维平面。请找出将这两个正方形分割成两半的一条直线。假设正方形顶边和底边与 x 轴平行。
#
# 每个正方形的数据square包含3个数值，正方形的左下顶点坐标[X,Y] = [square[0],square[1]]，以及正方形的边长square[2]。所求直线穿过两个正方形会形成4个交点，请返回4个交点形成线段的两端点坐标（两个端点即为4个交点中距离最远的2个点，这2个点所连成的线段一定会穿过另外2个交点）。2个端点坐标[X1,Y1]和[X2,Y2]的返回格式为{X1,Y1,X2,Y2}，要求若X1 != X2，需保证X1 < X2，否则需保证Y1 <= Y2。
#
# 若同时有多条直线满足要求，则选择斜率最大的一条计算并返回（与Y轴平行的直线视为斜率无穷大）。
#
# 示例：
#
# 输入：
# square1 = {-1, -1, 2}
# square2 = {0, -1, 2}
# 输出： {-1,0,2,0}
# 解释： 直线 y = 0 能将两个正方形同时分为等面积的两部分，返回的两线段端点为[-1,0]和[2,0]
# 提示：
#
# square.length == 3
# square[2] > 0

from leetcode.allcode.competition.mypackage import *

class Solution:
    def cutSquares(self, square1: List[int], square2: List[int]) -> List[float]:
        e1, e2 = square1[2], square2[2]
        c1x, c2x = square1[0] + e1 / 2, square2[0] + e2 / 2
        c1y, c2y = square1[1] + e1 / 2, square2[1] + e2 / 2
        if c1x == c2x:
            return [c1x, min(c1y - e1 / 2, c2y - e2 / 2), c1x, max(c1y + e1 / 2, c2y + e2 / 2)]
        if c1y == c2y:
            return [min(c1x - e1 / 2, c2x - e2 / 2), c1y, max(c1x + e1 / 2, c2x + e2 / 2), c1y]
        k = (c2y - c1y) / (c2x - c1x)
        b = c1y - k * c1x
        up1, up2, down1, down2 = square1[1] + e1, square2[1] + e2, square1[1], square2[1]
        left1, left2, right1, right2 = square1[0], square2[0], square1[0] + e1, square2[0] + e2

        def f(x):
            return k * x + b
        def g(y):  # f的反函数
            return (y - b) / k

        if down1 <= f(left1) <= up1:
            x1, y1 = left1, f(left1)
            x2, y2 = right1, f(right1)
        else:
            x1, y1 = g(down1), down1
            x2, y2 = g(up1), up1

        if down2 <= f(left2) <= up2:
            x3, y3 = left2, f(left2)
            x4, y4 = right2, f(right2)
        else:
            x3, y3 = g(down2), down2
            x4, y4 = g(up2), up2

        l = [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
        l.sort()
        return l[0] + l[-1]

so = Solution()
print(so.cutSquares([249,-199,5], [-1,136,76]))
print(so.cutSquares([-1, -1, 2], [0, -1, 2]))
print(so.cutSquares([-1,1,3], [0,0,5]))





