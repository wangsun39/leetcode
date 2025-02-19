# 给定 m 个数组，每个数组都已经按照升序排好序了。
#
# 现在你需要从两个不同的数组中选择两个整数（每个数组选一个）并且计算它们的距离。两个整数 a 和 b 之间的距离定义为它们差的绝对值 |a-b| 。
#
# 返回最大距离。
#
# 示例 1：
#
# 输入：[[1,2,3],[4,5],[1,2,3]]
# 输出：4
# 解释：
# 一种得到答案 4 的方法是从第一个数组或者第三个数组中选择 1，同时从第二个数组中选择 5 。
# 示例 2：
#
# 输入：arrays = [[1],[1]]
# 输出：0
#
#
# 提示：
#
# m == arrays.length
# 2 <= m <= 105
# 1 <= arrays[i].length <= 500
# -104 <= arrays[i][j] <= 104
# arrays[i] 以 升序 排序。
# 所有数组中最多有 105 个整数。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mn = mx = arrays[0][0]
        for x in arrays[0]:
            mn = min(mn, x)
            mx = max(mx, x)
        ans = 0
        for l in arrays[1:]:
            for x in l:
                ans = max(abs(mn - x), abs(mx - x), ans)
            for x in l:
                mn = min(mn, x)
                mx = max(mx, x)
        return ans




