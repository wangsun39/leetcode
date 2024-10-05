# 给你一个数组 maximumHeight ，其中 maximumHeight[i] 表示第 i 座塔可以达到的 最大 高度。
#
# 你的任务是给每一座塔分别设置一个高度，使得：
#
# 第 i 座塔的高度是一个正整数，且不超过 maximumHeight[i] 。
# 所有塔的高度互不相同。
# 请你返回设置完所有塔的高度后，可以达到的 最大 总高度。如果没有合法的设置，返回 -1 。
#
#
#
# 示例 1：
#
# 输入：maximumHeight = [2,3,4,3]
#
# 输出：10
#
# 解释：
#
# 我们可以将塔的高度设置为：[1, 2, 4, 3] 。
#
# 示例 2：
#
# 输入：maximumHeight = [15,10]
#
# 输出：25
#
# 解释：
#
# 我们可以将塔的高度设置为：[15, 10] 。
#
# 示例 3：
#
# 输入：maximumHeight = [2,2,1]
#
# 输出：-1
#
# 解释：
#
# 无法设置塔的高度为正整数且高度互不相同。
#
#
#
# 提示：
#
# 1 <= maximumHeight.length <= 105
# 1 <= maximumHeight[i] <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort()
        vis = set()
        n = len(maximumHeight)
        res = [0] * n
        for i, x in enumerate(maximumHeight):
            if x < i + 1: return -1
            if i == 0:
                res[i] = x
                vis.add(x)
                continue
            if x == maximumHeight[i - 1]:
                v = res[i - 1] - 1
                while v in vis:
                    v -= 1
                res[i] = v
                vis.add(v)
            else:
                res[i] = x
                vis.add(x)
        return sum(res)


so = Solution()
print(so.maximumTotalSum(maximumHeight = [7]))
print(so.maximumTotalSum(maximumHeight = [2,3,4,3]))




