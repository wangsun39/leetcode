# 给你正整数 low ，high 和 k 。
#
# 如果一个数满足以下两个条件，那么它是 美丽的 ：
#
# 偶数数位的数目与奇数数位的数目相同。
# 这个整数可以被 k 整除。
# 请你返回范围 [low, high] 中美丽整数的数目。
#
#
#
# 示例 1：
#
# 输入：low = 10, high = 20, k = 3
# 输出：2
# 解释：给定范围中有 2 个美丽数字：[12,18]
# - 12 是美丽整数，因为它有 1 个奇数数位和 1 个偶数数位，而且可以被 k = 3 整除。
# - 18 是美丽整数，因为它有 1 个奇数数位和 1 个偶数数位，而且可以被 k = 3 整除。
# 以下是一些不是美丽整数的例子：
# - 16 不是美丽整数，因为它不能被 k = 3 整除。
# - 15 不是美丽整数，因为它的奇数数位和偶数数位的数目不相等。
# 给定范围内总共有 2 个美丽整数。
# 示例 2：
#
# 输入：low = 1, high = 10, k = 1
# 输出：1
# 解释：给定范围中有 1 个美丽数字：[10]
# - 10 是美丽整数，因为它有 1 个奇数数位和 1 个偶数数位，而且可以被 k = 1 整除。
# 给定范围内总共有 1 个美丽整数。
# 示例 3：
#
# 输入：low = 5, high = 5, k = 2
# 输出：0
# 解释：给定范围中有 0 个美丽数字。
# - 5 不是美丽整数，因为它的奇数数位和偶数数位的数目不相等。
#
#
# 提示：
#
# 0 < low <= high <= 109
# 0 < k <= 20

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:

        def f(num: int):  # 数字 <= num 满足条件的所有数字
            s = str(num)
            @cache
            def digitDp(i: int, remain: int, n_odds, n_even, is_limit: bool, is_num: bool) -> int:
                if i == len(s):
                    return 1 if is_num and remain == 0 and n_even == n_odds else 0
                ans = 0
                if not is_num:
                    ans = digitDp(i + 1, 0, 0, 0, False, False)
                    if (len(s) - i - 1) & 1 == 0:  # 长度为奇数，不进行递归
                        return 0
                upper = int(s[i]) if is_limit else 9  # 判断当前位是否受约束
                lower = 0 if is_num else 1
                for j in range(lower, upper + 1):
                    if j & 1:
                        ans += digitDp(i + 1, (remain * 10 + j) % k, n_odds + 1, n_even, is_limit and j == upper, True)
                    else:
                        ans += digitDp(i + 1, (remain * 10 + j) % k, n_odds, n_even + 1, is_limit and j == upper, True)
                return ans
            return digitDp(0, 0, 0, 0, True, False)

        print(f(47))
        print(f(100))
        return f(high) - f(low - 1)


so = Solution()
print(so.numberOfBeautifulIntegers(low = 47, high = 100, k = 18))  # 2
print(so.numberOfBeautifulIntegers(low = 10, high = 20, k = 3))  # 2
print(so.numberOfBeautifulIntegers(low = 1, high = 10, k = 1))  # 1
print(so.numberOfBeautifulIntegers(low = 5, high = 5, k = 2))  # 0




