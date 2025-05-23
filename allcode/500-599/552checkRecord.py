# 可以用字符串表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。记录中只含下面三种字符：
# 'A'：Absent，缺勤
# 'L'：Late，迟到
# 'P'：Present，到场
# 如果学生能够 同时 满足下面两个条件，则可以获得出勤奖励：
#
# 按 总出勤 计，学生缺勤（'A'）严格 少于两天。
# 学生 不会 存在 连续 3 天或 连续 3 天以上的迟到（'L'）记录。
# 给你一个整数 n ，表示出勤记录的长度（次数）。请你返回记录长度为 n 时，可能获得出勤奖励的记录情况 数量 。答案可能很大，所以返回对 109 + 7 取余 的结果。
#
#
#
# 示例 1：
#
# 输入：n = 2
# 输出：8
# 解释：
# 有 8 种长度为 2 的记录将被视为可奖励：
# "PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# 只有"AA"不会被视为可奖励，因为缺勤次数为 2 次（需要少于 2 次）。
# 示例 2：
#
# 输入：n = 1
# 输出：3
# 示例 3：
#
# 输入：n = 10101
# 输出：183236316
#
#
# 提示：
#
# 1 <= n <= 105

from leetcode.allcode.competition.mypackage import *


class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp1 = [1,1,0,1,0,0,0]  # 分别表示以'A',('L','LL','P')未出现过'A',('L','LL','P')出现过'A' 结尾的个数
        dp2 = [0,0,0,0,0,0,0]
        for i in range(1, n):
            dp2[0] = sum(dp1[1:4]) % MOD
            dp2[1] = dp1[3]
            dp2[2] = dp1[1]
            dp2[3] = sum(dp1[1:4]) % MOD
            dp2[4] = (dp1[0] + dp1[6]) % MOD
            dp2[5] = dp1[4]
            dp2[6] = (dp1[0] + sum(dp1[4:])) % MOD
            dp1, dp2 = dp2, [0,0,0,0,0,0,0]
            # print(dp1)
        return sum(dp1) % MOD


so = Solution()
print(so.checkRecord(3))  # 19
print(so.checkRecord(2))  # 8
print(so.checkRecord(1))  # 3
print(so.checkRecord(10101))  # 183236316

