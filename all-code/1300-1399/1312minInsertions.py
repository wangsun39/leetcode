# 给你一个字符串 s ，每一次操作你都可以在字符串的任意位置插入任意字符。
#
# 请你返回让 s 成为回文串的 最少操作次数 。
#
# 「回文串」是正读和反读都相同的字符串。
#
#
#
# 示例 1：
#
# 输入：s = "zzazz"
# 输出：0
# 解释：字符串 "zzazz" 已经是回文串了，所以不需要做任何插入操作。
# 示例 2：
#
# 输入：s = "mbadm"
# 输出：2
# 解释：字符串可变为 "mbdadbm" 或者 "mdbabdm" 。
# 示例 3：
#
# 输入：s = "leetcode"
# 输出：5
# 解释：插入 5 个字符后字符串变为 "leetcodocteel" 。
#
#
# 提示：
#
# 1 <= s.length <= 500
# s 中所有字符都是小写字母。

from functools import cache
from typing import List

class Solution:
    def minInsertions(self, s: str) -> int:

        @cache
        def dfs(i, j):
            if i >= j:
                return 0
            if s[i] == s[j]:
                return dfs(i + 1, j - 1)
            return min(dfs(i + 1, j), dfs(i, j - 1)) + 1

        return dfs(0, len(s) - 1)


so = Solution()
print(so.minInsertions("zzazz"))
print(so.minInsertions("mbadm"))
print(so.minInsertions("leetcode"))




