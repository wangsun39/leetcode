# 给定两个整数 a 和 b ，返回 任意 字符串 s ，要求满足：
#
# s 的长度为 a + b，且正好包含 a 个 'a' 字母与 b 个 'b' 字母；
# 子串 'aaa' 没有出现在 s 中；
# 子串 'bbb' 没有出现在 s 中。
#
#
# 示例 1：
#
# 输入：a = 1, b = 2
# 输出："abb"
# 解释："abb", "bab" 和 "bba" 都是正确答案。
# 示例 2：
#
# 输入：a = 4, b = 1
# 输出："aabaa"
#
#
# 提示：
#
# 0 <= a, b <= 100
# 对于给定的 a 和 b，保证存在满足要求的 s

from leetcode.allcode.competition.mypackage import *

class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        if a == b: return 'ab' * a
        if a > b:
            l = ['aab'] * (a - b - 1) + ['ab'] * (2 * (b + 1) - a)
            return ''.join(l)[:-1]
        else:
            l = ['bba'] * (b - a - 1) + ['ba'] * (2 * (a + 1) - b)
            return ''.join(l)[:-1]


so = Solution()
print(so.strWithout3a3b(a = 1, b = 1))
print(so.strWithout3a3b(a = 4, b = 1))
print(so.strWithout3a3b(a = 1, b = 2))

