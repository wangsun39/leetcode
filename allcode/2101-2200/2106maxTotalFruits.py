# 一个括号字符串是只由 '(' 和 ')' 组成的 非空 字符串。如果一个字符串满足下面 任意 一个条件，那么它就是有效的：
#
# 字符串为 ().
# 它可以表示为 AB（A 与 B 连接），其中A 和 B 都是有效括号字符串。
# 它可以表示为 (A) ，其中 A 是一个有效括号字符串。
# 给你一个括号字符串 s 和一个字符串 locked ，两者长度都为 n 。locked 是一个二进制字符串，只包含 '0' 和 '1' 。对于 locked 中 每一个 下标 i ：
#
# 如果 locked[i] 是 '1' ，你 不能 改变 s[i] 。
# 如果 locked[i] 是 '0' ，你 可以 将 s[i] 变为 '(' 或者 ')' 。
# 如果你可以将 s 变为有效括号字符串，请你返回 true ，否则返回 false 。
#
#
#
# 示例 1：
#
#
#
# 输入：s = "))()))", locked = "010100"
# 输出：true
# 解释：locked[1] == '1' 和 locked[3] == '1' ，所以我们无法改变 s[1] 或者 s[3] 。
# 我们可以将 s[0] 和 s[4] 变为 '(' ，不改变 s[2] 和 s[5] ，使 s 变为有效字符串。
# 示例 2：
#
# 输入：s = "()()", locked = "0000"
# 输出：true
# 解释：我们不需要做任何改变，因为 s 已经是有效字符串了。
# 示例 3：
#
# 输入：s = ")", locked = "0"
# 输出：false
# 解释：locked 允许改变 s[0] 。
# 但无论将 s[0] 变为 '(' 或者 ')' 都无法使 s 变为有效字符串。
#
#
# 提示：
#
# n == s.length == locked.length
# 1 <= n <= 105
# s[i] 要么是 '(' 要么是 ')' 。
# locked[i] 要么是 '0' 要么是 '1' 。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n & 1:
            return False
        s1 = []  # 存放左括号位置的栈
        s2 = []  # 存放任意括号位置的栈
        for i in range(n):
            if locked[i] == '1':
                if s[i] == '(':
                    s1.append(i)
                else:
                    if s1:
                        s1.pop()
                    elif s2:
                        s2.pop()
                    else:
                        return False
            else:
                s2.append(i)
        while s1:
            if not s2 or s2[-1] < s1[-1]:
                return False
            s1.pop()
            s2.pop()
        return True



so = Solution()
print(so.canBeValid(s = "))()))", locked = "010100"))
print(so.canBeValid(s = "()()", locked = "0000"))
print(so.canBeValid(s = ")", locked = "0"))




