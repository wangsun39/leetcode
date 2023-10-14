# 给你两个正整数 low 和 high ，都用字符串表示，请你统计闭区间 [low, high] 内的 步进数字 数目。
#
# 如果一个整数相邻数位之间差的绝对值都 恰好 是 1 ，那么这个数字被称为 步进数字 。
#
# 请你返回一个整数，表示闭区间 [low, high] 之间步进数字的数目。
#
# 由于答案可能很大，请你将它对 109 + 7 取余 后返回。
#
# 注意：步进数字不能有前导 0 。
#
#
#
# 示例 1：
#
# 输入：low = "1", high = "11"
# 输出：10
# 解释：区间 [1,11] 内的步进数字为 1 ，2 ，3 ，4 ，5 ，6 ，7 ，8 ，9 和 10 。总共有 10 个步进数字。所以输出为 10 。
# 示例 2：
#
# 输入：low = "90", high = "101"
# 输出：2
# 解释：区间 [90,101] 内的步进数字为 98 和 101 。总共有 2 个步进数字。所以输出为 2 。
#
#
# 提示：
#
# 1 <= int(low) <= int(high) < 10100
# 1 <= low.length, high.length <= 100
# low 和 high 只包含数字。
# low 和 high 都不含前导 0 。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countSteppingNumbers1(self, low: str, high: str) -> int:
        MOD = 10 ** 9 + 7

        def f(s: str):  # 数字 <= num 满足条件的所有数字
            n = len(s)
            @cache
            def helper(i: int, is_limit: bool, pre: int) -> int:
                if i == len(s):
                    return 1
                ans = 0
                can = []
                if pre > 0:
                    if not is_limit or int(s[i]) >= pre - 1:
                        can.append(pre - 1)
                if pre < 9 and (not is_limit or int(s[i]) >= pre + 1):
                    can.append(pre + 1)
                for j in can:
                    if not is_limit:
                        ans += helper(i + 1, is_limit, j)
                    else:
                        if j == int(s[i]):
                            ans += helper(i + 1, is_limit, j)
                        else:
                            ans += helper(i + 1, False, j)
                    ans %= MOD
                return ans
            ans = 0
            # 长度为n的数
            for i in range(1, int(s[0]) + 1):
                if i < int(s[0]):
                    ans += helper(1, False, i)
                else:
                    ans += helper(1, True, i)
                ans %= MOD

            @cache
            def helper2(i: int, pre: int, ll) -> int:
                if i == ll:
                    return 1
                ans = 0
                can = []
                if pre > 0:
                    can.append(pre - 1)
                if pre < 9:
                    can.append(pre + 1)
                for j in can:
                    ans += helper2(i + 1, j, ll)
                    ans %= MOD
                return ans
            for length in range(1, n):
                for i in range(1, 10):
                    ans += helper2(1, i, length)
                    ans %= MOD

            return ans

        low = str(int(low) - 1)
        # print(f(high))
        # print(f(low))
        return (f(high) + MOD - f(low)) % MOD
    def countSteppingNumbers(self, low: str, high: str) -> int:
        MOD = 10 ** 9 + 7

        def f(s: str):  # 数字 <= num 满足条件的所有数字
            @cache
            def helper(i: int, is_limit: bool, pre: int, is_num: bool) -> int:
                if i == len(s):
                    return is_num
                ans = 0
                if not is_num:
                    ans = helper(i + 1, False, -1, False)

                if pre == -1:
                    if is_limit:
                        can = list(range(1, int(s[i]) + 1))
                    else:
                        can = list(range(1, 10))
                else:
                    can = []
                    if pre > 0:
                        can.append(pre - 1)
                    if pre < 9:
                        can.append(pre + 1)
                    if is_limit:
                        can = [x for x in can if x <= int(s[i])]

                for j in can:
                    if not is_limit:
                        ans += helper(i + 1, False, j, True)
                    else:
                        if j == int(s[i]):
                            ans += helper(i + 1, True, j, True)
                        else:
                            ans += helper(i + 1, False, j, True)
                    ans %= MOD
                return ans
            return helper(0, True, -1, False)

        low = str(int(low) - 1)
        # print(f(high))
        # print(f(low))
        return (f(high) + MOD - f(low)) % MOD



so = Solution()
print(so.countSteppingNumbers(low = "90", high = "101"))
print(so.countSteppingNumbers(low = "2", high = "40"))
print(so.countSteppingNumbers(low = "1", high = "11"))




