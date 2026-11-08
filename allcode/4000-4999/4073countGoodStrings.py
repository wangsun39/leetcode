# 给你一个整数 n。
#
# 如果一个字符串仅由字符 'a' 和 'b' 组成，且满足以下条件之一，则该字符串被认为是 好的 ：
#
# 它只包含 一种 字符，且其长度为 奇数 。
# 它可以写成 s = s1 + s2 的形式，其中 s1 和 s2 是 非空的好 字符串，且 s1 的最后一个字符与 s2 的第一个字符不同。
# 返回长度为 n 的 好的 字符串的数量，模 109 + 7。
#
# 这里，+ 表示字符串拼接。
#
#
#
# 示例 1：
#
# 输入： n = 4
#
# 输出： 6
#
# 解释：
#
# 好的字符串有 "aaab"、"abbb"、"baaa"、"bbba"、"abab" 和 "baba"。
# 例如，"aaab" = "aaa" + "b"。这两个部分都是好的，因为每个部分都只包含一种字符且长度为奇数，并且它们在边界处的字符不同。
# 同样地，"ab" = "a" + "b" 是好的，所以 "abab" = "ab" + "ab" 也是好的，因为它们的边界字符不同。
# 因此，答案为 6。
# 示例 2：
#
# 输入： n = 3
#
# 输出： 4
#
# 解释：
#
# 好的字符串有 "aaa"、"bbb"、"aba" 和 "bab"。因此，答案为 4。
#
# 示例 3：
#
# 输入： n = 2
#
# 输出： 2
#
# 解释：
#
# 好的字符串有 "ab" 和 "ba"。因此，答案为 2。
#
#
#
# 提示：
#
# 1 <= n <= 1015

from leetcode.allcode.competition.mypackage import *

MOD = 1_000_000_007

# a @ b，其中 @ 是矩阵乘法
# 更快的写法见另一份代码【NumPy】
def mul(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    return [[sum(x * y for x, y in zip(row, col)) % MOD for col in zip(*b)]
            for row in a]

# a^n @ f1  矩阵快速幂
def pow_mul(a: List[List[int]], n: int, f1: List[List[int]]) -> List[List[int]]:
    res = f1
    while n:
        if n & 1:
            res = mul(a, res)
        a = mul(a, a)
        n >>= 1
    return res
# print(pre[:10])

class Solution:
    def countGoodStrings(self, n: int) -> int:
        # f(n) = f(n-1) + f(n-2)
        if n == 1:
            return 2
        if n == 2:
            return 2
        f = pow_mul([[1, 1], [1, 0]], n - 2, [[2], [2]])
        return f[0][0]







so = Solution()
print(so.countGoodStrings(n = 4))



