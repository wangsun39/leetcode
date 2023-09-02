# 给你 n 个二维平面上的点 points ，其中 points[i] = [xi, yi] ，请你返回两点之间内部不包含任何点的 最宽垂直区域 的宽度。
#
# 垂直区域 的定义是固定宽度，而 y 轴上无限延伸的一块区域（也就是高度为无穷大）。 最宽垂直区域 为宽度最大的一个垂直区域。
#
# 请注意，垂直区域 边上 的点 不在 区域内。
#
#
#
# 示例 1：
#
#
# 输入：points = [[8,7],[9,9],[7,4],[9,7]]
# 输出：1
# 解释：红色区域和蓝色区域都是最优区域。
# 示例 2：
#
# 输入：points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
# 输出：3
#
#
# 提示：
#
# n == points.length
# 2 <= n <= 105
# points[i].length == 2
# 0 <= xi, yi <= 109





from typing import Optional,List
from collections import Counter
import heapq


# Definition for a binary tree node.
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xs = sorted([x for x, _ in points])
        return max(xs[i] - xs[i - 1] for i in range(1, len(xs)))



so = Solution()




