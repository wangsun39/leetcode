# 有一条由 n 个点连接而成的折线图。给定一个 下标从 1 开始 的整数数组 y，第 k 个点的坐标是 (k, y[k])。图中没有水平线，即没有两个相邻的点有相同的 y 坐标。
#
# 假设在图中任意画一条无限长的水平线。请返回这条水平线与折线相交的最多交点数。
#
#
#
# 示例 1：
#
#
# 输入：y = [1,2,1,2,1,3,2]
# 输出：5
# 解释：如上图所示，水平线 y = 1.5 与折线相交了 5 次（用红叉表示）。水平线 y = 2 与折线相交了 4 次（用红叉表示）。可以证明没有其他水平线可以与折线有超过 5 个点相交。因此，答案是 5。
# 示例 2：
#
#
# 输入：y = [2,1,3,4,5]
# 输出：2
# 解释：如上图所示，水平线 y=1.5 与折线相交了 2 次（用红叉表示）。水平线 y=2 与折线相交了 2 次（用红叉表示）。可以证明没有其他水平线可以与折线有超过 2 个点相交。因此，答案是 2。
#
#
# 提示：
#
# 2 <= y.length <= 105
# 1 <= y[i] <= 109
# 对于范围 [1, n - 1] 内的所有 i，都有 y[i] != y[i + 1]

from leetcode.allcode.competition.mypackage import *


class Solution:
    def maxIntersectionCount(self, y: List[int]) -> int:
        diff = defaultdict(int)  # 最优值落在某个折线的端点
        n = len(y)
        if y[0] < y[1]:
            diff[y[0]] += 1
            diff[y[1] + 1] -= 1
        else:
            diff[y[1]] += 1
            diff[y[0] + 1] -= 1
        for i in range(1, n - 1):
            y1, y2 = y[i], y[i + 1]
            if y1 > y2:
                y1, y2 = y2, y1
            if y1 == y[i]:
                diff[y1 + 1] += 1
                diff[y2 + 1] -= 1
            else:
                diff[y1] += 1
                diff[y2] -= 1
        # diff = sorted([k, v] for k, v in diff.items())

        diff1 = defaultdict(int)  # 最优值落在某个折线的端点下方
        for i in range(n - 1):
            y1, y2 = y[i], y[i + 1]
            if y1 > y2:
                y1, y2 = y2, y1
            diff1[y1 + 1] += 1
            diff1[y2 + 1] -= 1

        diff2 = defaultdict(int)  # 最优值落在某个折线的端点上方
        for i in range(n - 1):
            y1, y2 = y[i], y[i + 1]
            if y1 > y2:
                y1, y2 = y2, y1
            diff2[y1] += 1
            diff2[y2] -= 1


        def calc(Diff):
            Diff = sorted([k, v] for k, v in Diff.items())
            ans = 0
            cur = 0
            for k, v in Diff:
                cur += v
                ans = max(ans, cur)
            return ans
        return max(calc(diff), calc(diff1), calc(diff2))


so = Solution()
print(so.maxIntersectionCount([1,2,1,2,1,3,2]))
print(so.maxIntersectionCount([2,1,3,4,5]))
print(so.maxIntersectionCount([1,2,3]))
print(so.maxIntersectionCount([3,2,1]))
print(so.maxIntersectionCount([2,1]))







