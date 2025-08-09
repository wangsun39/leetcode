# 给你两个正整数 left 和 right ，满足 left <= right 。请你计算 闭区间 [left, right] 中所有整数的 乘积 。
#
# 由于乘积可能非常大，你需要将它按照以下步骤 缩写 ：
#
# 统计乘积中 后缀 0 的数目，并 移除 这些 0 ，将这个数目记为 C 。
# 比方说，1000 中有 3 个后缀 0 ，546 中没有后缀 0 。
# 将乘积中剩余数字的位数记为 d 。如果 d > 10 ，那么将乘积表示为 <pre>...<suf> 的形式，其中 <pre> 表示乘积最 开始 的 5 个数位，<suf> 表示删除后缀 0 之后 结尾的 5 个数位。如果 d <= 10 ，我们不对它做修改。
# 比方说，我们将 1234567654321 表示为 12345...54321 ，但是 1234567 仍然表示为 1234567 。
# 最后，将乘积表示为 字符串 "<pre>...<suf>eC" 。
# 比方说，12345678987600000 被表示为 "12345...89876e5" 。
# 请你返回一个字符串，表示 闭区间 [left, right] 中所有整数 乘积 的 缩写 。
#
#
#
# 示例 1：
#
# 输入：left = 1, right = 4
# 输出："24e0"
# 解释：
# 乘积为 1 × 2 × 3 × 4 = 24 。
# 由于没有后缀 0 ，所以 24 保持不变，缩写的结尾为 "e0" 。
# 因为乘积的结果是 2 位数，小于 10 ，所欲我们不进一步将它缩写。
# 所以，最终将乘积表示为 "24e0" 。
# 示例 2：
#
# 输入：left = 2, right = 11
# 输出："399168e2"
# 解释：乘积为 39916800 。
# 有 2 个后缀 0 ，删除后得到 399168 。缩写的结尾为 "e2" 。
# 删除后缀 0 后是 6 位数，不需要进一步缩写。
# 所以，最终将乘积表示为 "399168e2" 。
# 示例 3：
#
# 输入：left = 371, right = 375
# 输出："7219856259e3"
# 解释：乘积为 7219856259000 。
#
#
# 提示：
#
# 1 <= left <= right <= 104

from leetcode.allcode.competition.mypackage import *

import numpy as np

class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        # 1. 末尾 0 的个数
        # 2. 除末尾 0 之外的最低五位数
        # 3. 最高五位数
        # 这几步同时进行
        @cache
        def get_factor_nums(x, y):
            res = 0
            while x % y == 0:
                res += 1
                x //= y
            return res
        two = five = 0
        lg_p = 0  # 总乘积的对数
        for x in range(left, right + 1):
            # lg_p += log(float(x), 10.0)  # 原生的log函数精度不够
            # lg_p += np.log10(np.float128(x))  # 这个在linux下可以通过，window下没有这个函数
            lg_p += np.log10(x)  # 这个在windowns下精度不够
            two += get_factor_nums(x, 2)
            five += get_factor_nums(x, 5)

        tail_zero = sz = min(two, five)
        print(lg_p, np.longdouble(10.0) ** (lg_p - int(lg_p) + 4.0))
        print(lg_p, np.power(10.0, lg_p - int(lg_p) + 4.0))
        head = int(10 ** (lg_p - int(lg_p) + 4))  # 前5位

        # 4. 判断除去末尾零的剩余数字长度是否超过10位
        low = 1  # 除去末尾0的末尾准确数字数字
        tail = 1  # 末尾的数（只考虑末5位）
        two = five = sz  # 允许不考虑的因子2和5的总数量，因为它们合并之和变成10，其他的数字都会影响到low的长度
        for x in range(left, right + 1):
            while two and x % 2 == 0:
                x //= 2
                two -= 1
            while five and x % 5 == 0:
                x //= 5
                five -= 1
            tail = (tail * x) % 100000
            if low < 10 ** 10:
                low *= x
                continue
            x //= 2
        if low < 10 ** 10:
            return str(low) + 'e' + str(tail_zero)

        tail = str(tail)
        tail = '0' * (5 - len(tail)) + tail
        return f"{str(head)}...{tail}e{str(tail_zero)}"

so = Solution()
print(so.abbreviateProduct(left = 1269, right = 7292))
print(so.abbreviateProduct(left = 4838, right = 6186))  # "36088...36896e337"
print(so.abbreviateProduct(left = 2, right = 11))
print(so.abbreviateProduct(left = 1, right = 4))


