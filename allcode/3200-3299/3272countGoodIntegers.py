# 给你两个 正 整数 n 和 k 。
#
# 如果一个整数 x 满足以下条件，那么它被称为 k 回文 整数 。
#
# x 是一个
# 回文整数 。
# x 能被 k 整除。
# 如果一个整数的数位重新排列后能得到一个 k 回文整数 ，那么我们称这个整数为 好 整数。比方说，k = 2 ，那么 2020 可以重新排列得到 2002 ，2002 是一个 k 回文串，所以 2020 是一个好整数。而 1010 无法重新排列数位得到一个 k 回文整数。
#
# 请你返回 n 个数位的整数中，有多少个 好 整数。
#
# 注意 ，任何整数在重新排列数位之前或者之后 都不能 有前导 0 。比方说 1010 不能重排列得到 101 。
#
#
#
# 示例 1：
#
# 输入：n = 3, k = 5
#
# 输出：27
#
# 解释：
#
# 部分好整数如下：
#
# 551 ，因为它可以重排列得到 515 。
# 525 ，因为它已经是一个 k 回文整数。
# 示例 2：
#
# 输入：n = 1, k = 4
#
# 输出：2
#
# 解释：
#
# 两个好整数分别是 4 和 8 。
#
# 示例 3：
#
# 输入：n = 5, k = 6
#
# 输出：2468
#
#
#
# 提示：
#
# 1 <= n <= 10
# 1 <= k <= 9

import math

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        vis = set()
        half = (n + 1) // 2
        orders = [math.factorial(i) for i in range(n + 1)]
        def trans(ss):
            ss = '0' * (n - len(ss)) + ss
            res = [0] * 10
            counter = Counter(ss)
            for k, v in counter.items():
                res[int(k)] = v
            return tuple(res)

        mx_half = 10 ** half
        if n & 1:
            for x in range(mx_half // 10, mx_half):
                v1 = str(x)[:-1] + str(x)[::-1]  # 奇数长度
                v2 = int(v1)
                if v2 % k == 0:
                    tu = trans(v1)
                    vis.add(tu)
        else:
            for x in range(mx_half // 10, mx_half):
                v1 = str(x) + str(x)[::-1]  # 偶数长度
                v2 = int(v1)
                if v2 % k == 0:
                    tu = trans(v1)
                    vis.add(tu)

        def calc(tu):  # 计算排列组合
            n_zero = tu[0]
            total = orders[n - 1] * (n - n_zero)  # 不考虑0开头的
            res = total
            for i in range(10):
                if tu[i]:
                    res //= orders[tu[i]]
            return res

        ans = 0
        for tu in vis:
            ans += calc(tu)
        return ans

so = Solution()
print(so.countGoodIntegers(n = 4, k = 1))
print(so.countGoodIntegers(n = 3, k = 5))
print(so.countGoodIntegers(n = 1, k = 4))




