# 考试中有 n 种类型的题目。给你一个整数 target 和一个下标从 0 开始的二维整数数组 types ，其中 types[i] = [counti, marksi] 表示第 i 种类型的题目有 counti 道，每道题目对应 marksi 分。
#
# 返回你在考试中恰好得到 target 分的方法数。由于答案可能很大，结果需要对 109 +7 取余。
#
# 注意，同类型题目无法区分。
#
# 比如说，如果有 3 道同类型题目，那么解答第 1 和第 2 道题目与解答第 1 和第 3 道题目或者第 2 和第 3 道题目是相同的。
#
#
# 示例 1：
#
# 输入：target = 6, types = [[6,1],[3,2],[2,3]]
# 输出：7
# 解释：要获得 6 分，你可以选择以下七种方法之一：
# - 解决 6 道第 0 种类型的题目：1 + 1 + 1 + 1 + 1 + 1 = 6
# - 解决 4 道第 0 种类型的题目和 1 道第 1 种类型的题目：1 + 1 + 1 + 1 + 2 = 6
# - 解决 2 道第 0 种类型的题目和 2 道第 1 种类型的题目：1 + 1 + 2 + 2 = 6
# - 解决 3 道第 0 种类型的题目和 1 道第 2 种类型的题目：1 + 1 + 1 + 3 = 6
# - 解决 1 道第 0 种类型的题目、1 道第 1 种类型的题目和 1 道第 2 种类型的题目：1 + 2 + 3 = 6
# - 解决 3 道第 1 种类型的题目：2 + 2 + 2 = 6
# - 解决 2 道第 2 种类型的题目：3 + 3 = 6
# 示例 2：
#
# 输入：target = 5, types = [[50,1],[50,2],[50,5]]
# 输出：4
# 解释：要获得 5 分，你可以选择以下四种方法之一：
# - 解决 5 道第 0 种类型的题目：1 + 1 + 1 + 1 + 1 = 5
# - 解决 3 道第 0 种类型的题目和 1 道第 1 种类型的题目：1 + 1 + 1 + 2 = 5
# - 解决 1 道第 0 种类型的题目和 2 道第 1 种类型的题目：1 + 2 + 2 = 5
# - 解决 1 道第 2 种类型的题目：5
# 示例 3：
#
# 输入：target = 18, types = [[6,1],[3,2],[2,3]]
# 输出：1
# 解释：只有回答所有题目才能获得 18 分。
#
#
# 提示：
#
# 1 <= target <= 1000
# n == types.length
# 1 <= n <= 50
# types[i].length == 2
# 1 <= counti, marksi <= 50

from leetcode.allcode.competition.mypackage import *


class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        n = len(types)
        dp = [[0] * (target + 1) for _ in range(n)]  # 前 i 种类型的题，得到 j 分的总数
        for i in range(n):
            for j in range(1, types[i][0] + 1):
                if j * types[i][1] <= target:
                    dp[i][j * types[i][1]] = 1
            for j in range(1, target + 1):
                for k in range(types[i][0] + 1):
                    if j - types[i][1] * k >= 0 and i > 0:
                        dp[i][j] += dp[i - 1][j - types[i][1] * k]
                        dp[i][j] %= MOD
        # ans = 0
        # print(dp)
        return dp[-1][target]





so = Solution()




