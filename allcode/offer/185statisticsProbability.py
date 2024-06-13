# 你选择掷出 num 个色子，请返回所有点数总和的概率。
#
# 你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 num 个骰子所能掷出的点数集合中第 i 小的那个的概率。
#
#
#
# 示例 1：
#
# 输入：num = 3
# 输出：[0.00463,0.01389,0.02778,0.04630,0.06944,0.09722,0.11574,0.12500,0.12500,0.11574,0.09722,0.06944,0.04630,0.02778,0.01389,0.00463]
# 示例 2：
#
# 输入：num = 5
# 输出:[0.00013,0.00064,0.00193,0.00450,0.00900,0.01620,0.02636,0.03922,0.05401,0.06944,0.08372,0.09452,0.10031,0.10031,0.09452,0.08372,0.06944,0.05401,0.03922,0.02636,0.01620,0.00900,0.00450,0.00193,0.00064,0.00013]
#
#
# 提示：
#
# 1 <= num <= 11


from leetcode.allcode.competition.mypackage import *



class Solution:
    def statisticsProbability(self, num: int) -> List[float]:
        dp1 = [1/6] * 6

        for _ in range(num - 1):
            dp2 = [0] * (len(dp1) + 6)
            for i in range(len(dp1)):
                for j in range(1, 7):
                    dp2[i + j] += dp1[i] / 6
            dp1 = dp2
        return dp1[num - 1:]



so = Solution()
print(so.statisticsProbability(1))
print(so.statisticsProbability(2))




