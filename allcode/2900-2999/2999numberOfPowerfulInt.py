# 给你三个整数 start ，finish 和 limit 。同时给你一个下标从 0 开始的字符串 s ，表示一个 正 整数。
#
# 如果一个 正 整数 x 末尾部分是 s （换句话说，s 是 x 的 后缀），且 x 中的每个数位至多是 limit ，那么我们称 x 是 强大的 。
#
# 请你返回区间 [start..finish] 内强大整数的 总数目 。
#
# 如果一个字符串 x 是 y 中某个下标开始（包括 0 ），到下标为 y.length - 1 结束的子字符串，那么我们称 x 是 y 的一个后缀。比方说，25 是 5125 的一个后缀，但不是 512 的后缀。
#
#
#
# 示例 1：
#
# 输入：start = 1, finish = 6000, limit = 4, s = "124"
# 输出：5
# 解释：区间 [1..6000] 内的强大数字为 124 ，1124 ，2124 ，3124 和 4124 。这些整数的各个数位都 <= 4 且 "124" 是它们的后缀。注意 5124 不是强大整数，因为第一个数位 5 大于 4 。
# 这个区间内总共只有这 5 个强大整数。
# 示例 2：
#
# 输入：start = 15, finish = 215, limit = 6, s = "10"
# 输出：2
# 解释：区间 [15..215] 内的强大整数为 110 和 210 。这些整数的各个数位都 <= 6 且 "10" 是它们的后缀。
# 这个区间总共只有这 2 个强大整数。
# 示例 3：
#
# 输入：start = 1000, finish = 2000, limit = 4, s = "3000"
# 输出：0
# 解释：区间 [1000..2000] 内的整数都小于 3000 ，所以 "3000" 不可能是这个区间内任何整数的后缀。
#
#
# 提示：
#
# 1 <= start <= finish <= 1015
# 1 <= limit <= 9
# 1 <= s.length <= floor(log10(finish)) + 1
# s 数位中每个数字都小于等于 limit 。
# s 不包含任何前导 0 。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:

        def f(x):
            ss = str(x)

            @cache
            def helper(i: int, is_limit: bool, is_num: bool) -> int:
                if x < int(s):
                    return 0
                if i == len(ss) - len(s):
                    if is_num and is_limit:
                        return ss[len(ss) - len(s):] >= s
                    return 1
                ans = 0
                if not is_num:
                    ans = helper(i + 1, False, False)
                upper = min(int(ss[i]), limit) if is_limit else limit  # 判断当前位是否受约束
                lower = 0 if is_num else 1
                for j in range(lower, upper + 1):
                    ans += helper(i + 1, is_limit and j == int(ss[i]), True)
                return ans

            return helper(0, True, False)
        # print(f(finish))
        return f(finish) - f(start - 1)


so = Solution()
print(so.numberOfPowerfulInt(start = 1, finish = 6000, limit = 4, s = "124"))
print(so.numberOfPowerfulInt(start = 1, finish = 971, limit = 9, s = "72"))
print(so.numberOfPowerfulInt(start = 15, finish = 215, limit = 6, s = "10"))
print(so.numberOfPowerfulInt(start = 1000, finish = 2000, limit = 4, s = "3000"))




