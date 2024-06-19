# 给定两条线段（表示为起点start = {X1, Y1}和终点end = {X2, Y2}），如果它们有交点，请计算其交点，没有交点则返回空值。
#
# 要求浮点型误差不超过10^-6。若有多个交点（线段重叠）则返回 X 值最小的点，X 坐标相同则返回 Y 值最小的点。
#
#
#
# 示例 1：
#
# 输入：
# line1 = {0, 0}, {1, 0}
# line2 = {1, 1}, {0, -1}
# 输出： {0.5, 0}
# 示例 2：
#
# 输入：
# line1 = {0, 0}, {3, 3}
# line2 = {1, 1}, {2, 2}
# 输出： {1, 1}
# 示例 3：
#
# 输入：
# line1 = {0, 0}, {1, 1}
# line2 = {1, 0}, {2, 1}
# 输出： {}，两条线段没有交点
#
#
# 提示：
#
# 坐标绝对值不会超过 2^7
# 输入的坐标均是有效的二维坐标

from leetcode.allcode.competition.mypackage import *


class Solution:
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        if start1[0] > end1[0]:
            start1, end1 = end1, start1
        if start2[0] > end2[0]:
            start2, end2 = end2, start2
        if start1[0] == end1[0] and start2[0] == end2[0]:
            if start1[0] != start2[0]:
                return []
            if start1[1] > end1[1]:
                start1, end1 = end1, start1
            if start2[1] > end2[1]:
                start2, end2 = end2, start2
            if start2[1] <= start1[1] <= end2[1]:
                return start1
            if start1[1] <= start2[1] <= end1[1]:
                return start2
            return []
        if start2[0] == end2[0]:
            start1, end1, start2, end2 = start2, end2, start1, end1
        if start1[0] == end1[0]:
            if start2[0] > start1[0] or end2[0] < start1[0]:
                return []
            k2 = (end2[1] - start2[1]) / (end2[0] - start2[0])
            midx = start1[0]
            midy = k2 * (midx - start2[0]) + start2[1]
            return [midx, midy] if start1[1] <= midy <= end1[1] or end1[1] <= midy <= start1[1] else []
        if (end1[1] - start1[1]) * (end2[0] - start2[0]) == (end1[0] - start1[0]) * (end2[1] - start2[1]):
            # 斜率相同
            if (end1[1] - start1[1]) * (end2[0] - start1[0]) == (end1[0] - start1[0]) * (end2[1] - start1[1]):
                # 四点共线
                if start1[0] <= start2[0] <= end1[0]:
                    return start2
                if start2[0] <= start1[0] <= end2[0]:
                    return start1
                return []
            return []
        k1 = (end1[1] - start1[1]) / (end1[0] - start1[0])
        k2 = (end2[1] - start2[1]) / (end2[0] - start2[0])
        # y=k1(x-x0)+y0=k2(x-x2)+y2
        # (k1-k2)x=k1x0-k2x2+y2-y0
        midx = ((k1 * start1[0] - k2 * start2[0]) + start2[1] - start1[1]) / (k1 - k2)
        midy = k1 * (midx - start1[0]) + start1[1]
        if start1[0] <= midx <= end1[0] and start2[0] <= midx <= end2[0]:
            return [midx, midy]
        return []







so = Solution()
print(so.intersection([-10,48], [-43,46], [-16,59], [-1,85]))
print(so.intersection([1,1], [-1,1], [1,0], [-3,2]))
print(so.intersection([0, 1], [0, 2], [0, 2], [0, 3]))
print(so.intersection([0, 1], [0, 2], [0, 2], [0, 3]))
print(so.intersection([0, 1], [0, -1], [1, 1], [-1, -1]))





