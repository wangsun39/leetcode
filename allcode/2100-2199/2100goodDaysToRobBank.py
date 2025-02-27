# 你和一群强盗准备打劫银行。给你一个下标从 0开始的整数数组security，其中security[i]是第 i天执勤警卫的数量。日子从 0开始编号。同时给你一个整数time。
#
# 如果第 i天满足以下所有条件，我们称它为一个适合打劫银行的日子：
#
# 第 i天前和后都分别至少有 time天。
# 第 i天前连续 time天警卫数目都是非递增的。
# 第 i天后连续 time天警卫数目都是非递减的。
# 更正式的，第 i 天是一个合适打劫银行的日子当且仅当：security[i - time] >= security[i - time + 1] >= ... >= security[i] <= ... <= security[i + time - 1] <= security[i + time].
#
# 请你返回一个数组，包含 所有 适合打劫银行的日子（下标从 0开始）。返回的日子可以 任意顺序排列。
#
#
#
# 示例 1：
#
# 输入：security = [5,3,3,3,5,6,2], time = 2
# 输出：[2,3]
# 解释：
# 第 2 天，我们有 security[0] >= security[1] >= security[2] <= security[3] <= security[4] 。
# 第 3 天，我们有 security[1] >= security[2] >= security[3] <= security[4] <= security[5] 。
# 没有其他日子符合这个条件，所以日子 2 和 3 是适合打劫银行的日子。
# 示例 2：
#
# 输入：security = [1,1,1,1,1], time = 0
# 输出：[0,1,2,3,4]
# 解释：
# 因为 time 等于 0 ，所以每一天都是适合打劫银行的日子，所以返回每一天。
# 示例 3：
#
# 输入：security = [1,2,3,4,5,6], time = 2
# 输出：[]
# 解释：
# 没有任何一天的前 2 天警卫数目是非递增的。
# 所以没有适合打劫银行的日子，返回空数组。
# 示例 4：
#
# 输入：security = [1], time = 5
# 输出：[]
# 解释：
# 没有日子前面和后面有 5 天时间。
# 所以没有适合打劫银行的日子，返回空数组。
#
#
# 提示：
#
# 1 <= security.length <= 105
# 0 <= security[i], time <= 105




from leetcode.allcode.competition.mypackage import *
# Definition for a binary tree node.
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        left, right = [0] * n, [0] * n
        for i in range(1, n):
            left[i] = left[i - 1] + 1 if security[i - 1] >= security[i] else 0
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] + 1 if security[i] <= security[i + 1] else 0
        ans = []
        # print(left)
        for i in range(n):
            if left[i] >= time and right[i] >= time:
                ans.append(i)
        return ans




so = Solution()
print(so.goodDaysToRobBank([1,2,5,4,1,0,2,4,5,3,1,2,4,3,2,4,8], 2))  # [5,10,14]
print(so.goodDaysToRobBank([5,3,3,3,5,6,2], 2))  # [2,3]
print(so.goodDaysToRobBank([3,0,0,0,1], 2))  # [2]
print(so.goodDaysToRobBank([0,4,3,0,0], 1))  # [3]
print(so.goodDaysToRobBank([1,1,1,1,1], 0))  # [0, 1, 2, 3, 4]
print(so.goodDaysToRobBank([1,2,3,4,5,6], 2))   # []

