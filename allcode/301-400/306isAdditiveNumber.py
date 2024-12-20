# 累加数 是一个字符串，组成它的数字可以形成累加序列。
#
# 一个有效的 累加序列 必须 至少 包含 3 个数。除了最开始的两个数以外，序列中的每个后续数字必须是它之前两个数字之和。
#
# 给你一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是 累加数 。如果是，返回 true ；否则，返回 false 。
#
# 说明：累加序列里的数，除数字 0 之外，不会 以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。
#
#
#
# 示例 1：
#
# 输入："112358"
# 输出：true
# 解释：累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# 示例 2：
#
# 输入："199100199"
# 输出：true
# 解释：累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199
#
#
# 提示：
#
# 1 <= num.length <= 35
# num 仅由数字（0 - 9）组成
#
#
# 进阶：你计划如何处理由过大的整数输入导致的溢出?

from leetcode.allcode.competition.mypackage import *

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def check(d1, d2):
            # [0, d1], [d1 + 1, d2]
            if (num[d1 + 1] == '0' and d2 - d1 > 1) or (num[0] == '0' and d1 > 0): return False
            a, b = int(num[:d1 + 1]), int(num[d1 + 1: d2 + 1])
            cur = d2 + 1
            while True:
                c = a + b
                lc = len(str(c))
                if cur + lc > n:
                    return False
                if (num[cur] == '0' and lc > 1) or num[cur: cur + lc] != str(c):
                    return False
                cur += lc
                if cur == n: return True
                a, b = b, c

        for i in range(n):
            for j in range(i + 1, n):
                if check(i, j):
                    return True
        return False


so = Solution()
print(so.isAdditiveNumber("000"))
print(so.isAdditiveNumber("112358"))



