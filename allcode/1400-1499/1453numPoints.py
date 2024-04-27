# 给你两个整数数组 startTime（开始时间）和 endTime（结束时间），并指定一个整数 queryTime 作为查询时间。
#
# 已知，第 i 名学生在 startTime[i] 时开始写作业并于 endTime[i] 时完成作业。
#
# 请返回在查询时间 queryTime 时正在做作业的学生人数。形式上，返回能够使 queryTime 处于区间 [startTime[i], endTime[i]]（含）的学生人数。
#
#
#
# 示例 1：
#
# 输入：startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
# 输出：1
# 解释：一共有 3 名学生。
# 第一名学生在时间 1 开始写作业，并于时间 3 完成作业，在时间 4 没有处于做作业的状态。
# 第二名学生在时间 2 开始写作业，并于时间 2 完成作业，在时间 4 没有处于做作业的状态。
# 第三名学生在时间 3 开始写作业，预计于时间 7 完成作业，这是是唯一一名在时间 4 时正在做作业的学生。
# 示例 2：
#
# 输入：startTime = [4], endTime = [4], queryTime = 4
# 输出：1
# 解释：在查询时间只有一名学生在做作业。
# 示例 3：
#
# 输入：startTime = [4], endTime = [4], queryTime = 5
# 输出：0
# 示例 4：
#
# 输入：startTime = [1,1,1,1], endTime = [1,3,2,4], queryTime = 7
# 输出：0
# 示例 5：
#
# 输入：startTime = [9,8,7,6,5,4,3,2,1], endTime = [10,10,10,10,10,10,10,10,10], queryTime = 5
# 输出：5
#
#
# 提示：
#
# startTime.length == endTime.length
# 1 <= startTime.length <= 100
# 1 <= startTime[i] <= endTime[i] <= 1000
# 1 <= queryTime <= 1000

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        n = len(darts)
        eps = 10 ** -6
        def get_num(u, v): # 中心在(u,v)时，覆盖的点数
            # for x, y in darts:
            #     print((x - u) * (x - u) + (y - v) * (y - v), x, y, r*r)
            return sum((x - u) * (x - u) + (y - v) * (y - v) <= r * r + eps for x, y in darts)

        ans = 1
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = darts[i]
                x2, y2 = darts[j]
                if (x1 - x2) ** 2 + (y1 - y2) ** 2 > (r * 2) ** 2:  # 两点距离超过直径
                    continue
                if (x1 - x2) ** 2 + (y1 - y2) ** 2 == (r * 2) ** 2:  # 两点距离等于直径，一个圆心在中点
                    ans = max(ans, get_num((x1 + x2)/2, (y1+y2)/2))
                    continue
                if x1 == x2:
                    d12 = y1 - y2
                    dmc = (r ** 2 - (d12 / 2) ** 2) ** 0.5  # 圆心到x1 x2 的中点的距离
                    c1x = (x1 + x2) / 2 + dmc
                    c2x = (x1 + x2) / 2 + dmc
                    ans = max(ans, get_num(c1x, (y1+y2)/2))
                    ans = max(ans, get_num(c2x, (y1+y2)/2))
                    continue
                d12 = ((y1 - y2) ** 2 + (x1-x2) ** 2) ** 0.5 / 2  # x1,x2的距离一半
                x0,y0 = (x1+x2)/2,(y1+y2)/2  # x1 x2 的中点
                k12 = (y1-y2)/(x1-x2)   # x1,x2点斜率
                # 以下是用解方程组得到两组圆心坐标
                c1y = y0 + ((r*r - d12*d12)/(k12*k12+1)) ** 0.5
                c1x = x0+k12*(y0-c1y)
                ans = max(ans, get_num(c1x, c1y))
                c2y = y0 - ((r*r - d12*d12)/(k12*k12+1)) ** 0.5
                c2x = x0+k12*(y0-c2y)
                ans = max(ans, get_num(c2x, c2y))

        return ans


so = Solution()
print(so.numPoints([[4,5],[-4,0],[-4,1],[-3,2],[0,2]], 5))
print(so.numPoints([[-2,0],[2,0],[0,2],[0,-2]], 1))
print(so.numPoints([[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]], 2))
print(so.numPoints(darts = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5))
print(so.numPoints(darts = [[-2,0],[2,0],[0,2],[0,-2]], r = 2))




