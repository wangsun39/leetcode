# 给你一个由数字组成的字符串 s 。重复执行以下操作，直到字符串恰好包含 两个 数字：
#
# 从第一个数字开始，对于 s 中的每一对连续数字，计算这两个数字的和 模 10。
# 用计算得到的新数字依次替换 s 的每一个字符，并保持原本的顺序。
# 如果 s 最后剩下的两个数字 相同 ，返回 true 。否则，返回 false。
#
#
#
# 示例 1：
#
# 输入： s = "3902"
#
# 输出： true
#
# 解释：
#
# 一开始，s = "3902"
# 第一次操作：
# (s[0] + s[1]) % 10 = (3 + 9) % 10 = 2
# (s[1] + s[2]) % 10 = (9 + 0) % 10 = 9
# (s[2] + s[3]) % 10 = (0 + 2) % 10 = 2
# s 变为 "292"
# 第二次操作：
# (s[0] + s[1]) % 10 = (2 + 9) % 10 = 1
# (s[1] + s[2]) % 10 = (9 + 2) % 10 = 1
# s 变为 "11"
# 由于 "11" 中的数字相同，输出为 true。
# 示例 2：
#
# 输入： s = "34789"
#
# 输出： false
#
# 解释：
#
# 一开始，s = "34789"。
# 第一次操作后，s = "7157"。
# 第二次操作后，s = "862"。
# 第三次操作后，s = "48"。
# 由于 '4' != '8'，输出为 false。
#
#
# 提示：
#
# 3 <= s.length <= 100
# s 仅由数字组成。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = list(s)
        s = [int(x) for x in s]
        s1 = []
        while len(s) > 2:
            for i, x in enumerate(s[1:], 1):
                v = (s[i - 1] + s[i]) % 10
                s1.append(v)
            s, s1 = s1, []
        return s[0] == s[1]


so = Solution()
print(so.hasSameDigits('3902'))




