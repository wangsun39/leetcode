# 给你两个整数 n 和 k。
#
# 如果一个 正 整数 x 同时满足以下两个条件，则称其为 兼容 整数：
#
# abs(n - x) <= k
# (n & x) == 0
# 返回所有 兼容 整数 x 的总和。
#
# 注意：
#
# 这里，& 表示 按位与 运算符。
# 整数 i 和 j 之间的 绝对 差定义为 abs(i - j)。
#
#
# 示例 1：
#
# 输入： n = 2, k = 3
#
# 输出： 10
#
# 解释：
#
# 兼容整数为：
#
# x = 1，因为 abs(2 - 1) = 1 且 2 & 1 = 0。
# x = 4，因为 abs(2 - 4) = 2 且 2 & 4 = 0。
# x = 5，因为 abs(2 - 5) = 3 且 2 & 5 = 0。
# 因此，答案为 1 + 4 + 5 = 10。
#
# 示例 2：
#
# 输入： n = 5, k = 1
#
# 输出： 0
#
# 解释：
#
# 区间 [4, 6] 中没有兼容整数。因此，答案为 0。
#
#
#
# 提示：
#
# 1 <= n <= 100
# 1 <= k <= 100

from leetcode.allcode.competition.mypackage import *

class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        s = set(i for i, x in enumerate(bin(n)[2:][::-1]) if x == '1')
        # print(s)

        def f(num: str):  # 数字 <= num 满足条件的所有数字
            # print(num)
            m = len(num)
            @cache
            def digitDp(i: int, is_limit: bool):
                if i == len(num):
                    return 1, 0  # 返回个数 1 , 和 0
                ri = m - 1 - i  #  从右开始的下标
                ans = [0, 0]
                upper = int(num[i]) if is_limit else 1  # 判断当前位是否受约束
                for j in range(upper + 1):
                    if ri in s and j == 1: continue
                    c, su = digitDp(i + 1, is_limit and j == upper)
                    if j == 1:
                        ans = [ans[0] + c, ans[1] + su + c * (1 << ri)]
                    else:
                        ans = [ans[0] + c, ans[1] + su]
                # print(num, i, is_limit, ans)
                return ans
            ans = digitDp(0, True)
            return ans[1]

        low = max(n - k - 1, 0)
        # print(bin(low), n - k - 1)
        return f(bin(n + k)[2:]) - f(bin(low)[2:])


so = Solution()
print(so.sumOfGoodIntegers(n = 2, k = 3))




