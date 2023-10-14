# 给你两个数字字符串 num1 和 num2 ，以及两个整数 max_sum 和 min_sum 。如果一个整数 x 满足以下条件，我们称它是一个好整数：
#
# num1 <= x <= num2
# min_sum <= digit_sum(x) <= max_sum.
# 请你返回好整数的数目。答案可能很大，请返回答案对 109 + 7 取余后的结果。
#
# 注意，digit_sum(x) 表示 x 各位数字之和。
# 
#
#
# 示例 1：
#
# 输入：num1 = "1", num2 = "12", min_num = 1, max_num = 8
# 输出：11
# 解释：总共有 11 个整数的数位和在 1 到 8 之间，分别是 1,2,3,4,5,6,7,8,10,11 和 12 。所以我们返回 11 。
# 示例 2：
#
# 输入：num1 = "1", num2 = "5", min_num = 1, max_num = 5
# 输出：5
# 解释：数位和在 1 到 5 之间的 5 个整数分别为 1,2,3,4 和 5 。所以我们返回 5 。
#
#
# 提示：
#
# 1 <= num1 <= num2 <= 1022
# 1 <= min_sum <= max_sum <= 400
from leetcode.allcode.competition.mypackage import *

class Solution:
    def count1(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        # 赛后继续写的 solution
        MOD = 10 ** 9 + 7
        @cache
        def helper(upper, limit):  # 字符串 upper
            if len(upper) == 0:
                return 0 == limit
            first = int(upper[0])
            if first <= limit:
                res = 0
                for i in range(first):
                    res += helper('9' * (len(upper) - 1), limit - i)
                    res %= MOD
                res += helper(upper[1:], limit - first)
                res %= MOD
                return res
            res = 0
            for i in range(limit + 1):
                res += helper('9' * (len(upper) - 1), limit - i)
                res %= MOD
            return res

        def f(upper):
            ans = 0
            for lim in range(min_sum, min(22 * 9 + 1, max_sum + 1)):
                ans += helper(upper, lim)
                ans %= MOD
            # print(upper, ans)
            return ans
        num1 = str(int(num1) - 1)
        return (f(num2) + MOD - f(num1)) % MOD

    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        # 改造用数位DP的模板
        MOD = 10 ** 9 + 7

        def f(num: str):  # 数字 <= num 满足条件的所有数字
            @cache
            def digitDp(i: int, is_limit: bool, s: int) -> int:
                if s > max_sum: return 0
                if i == len(num):
                    return min_sum <= s <= max_sum
                ans = 0
                upper = int(num[i]) if is_limit else 9  # 判断当前位是否受约束
                for j in range(upper + 1):
                    ans += digitDp(i + 1, is_limit and j == upper, s + j)
                return ans
            return digitDp(0, True, 0)

        num1 = str(int(num1) - 1)
        return (f(num2) + MOD - f(num1)) % MOD



so = Solution()
print(so.count("1000000007","2000000014",1,400))  # 1
print(so.count("1", "12", 1, 8))  # 11
print(so.count(num1 = "1", num2 = "5", min_sum = 1, max_sum = 5))




