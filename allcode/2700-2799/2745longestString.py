# 给你三个整数 x ，y 和 z 。
#
# 这三个整数表示你有 x 个 "AA" 字符串，y 个 "BB" 字符串，和 z 个 "AB" 字符串。你需要选择这些字符串中的部分字符串（可以全部选择也可以一个都不选择），将它们按顺序连接得到一个新的字符串。新字符串不能包含子字符串 "AAA" 或者 "BBB" 。
#
# 请你返回新字符串的最大可能长度。
#
# 子字符串 是一个字符串中一段连续 非空 的字符序列。
#
#
#
# 示例 1：
#
# 输入：x = 2, y = 5, z = 1
# 输出：12
# 解释： 我们可以按顺序连接 "BB" ，"AA" ，"BB" ，"AA" ，"BB" 和 "AB" ，得到新字符串 "BBAABBAABBAB" 。
# 字符串长度为 12 ，无法得到一个更长的符合题目要求的字符串。
# 示例 2：
#
# 输入：x = 3, y = 2, z = 2
# 输出：14
# 解释：我们可以按顺序连接 "AB" ，"AB" ，"AA" ，"BB" ，"AA" ，"BB" 和 "AA" ，得到新字符串 "ABABAABBAABBAA" 。
# 字符串长度为 14 ，无法得到一个更长的符合题目要求的字符串。
#
#
# 提示：
#
# 1 <= x, y, z <= 50

from leetcode.allcode.competition.mypackage import *

class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:

        @cache
        def dfs(xx, yy, zz, start):
            if xx < 0 or yy < 0 or zz < 0: return -inf
            if start == 0:
                res = max(dfs(xx - 1, yy, zz, 1) + 2, dfs(xx, yy - 1, zz, 2) + 2, dfs(xx, yy, zz - 1, 3) + 2)
            elif start == 1:
                res = dfs(xx, yy - 1, zz, 2) + 2
            elif start == 2:
                res = max(dfs(xx, yy, zz - 1, 3) + 2, dfs(xx - 1, yy, zz, 1) + 2)
            else:
                res = max(dfs(xx - 1, yy, zz, 1) + 2, dfs(xx, yy, zz - 1, 3) + 2)
            # print(xx, yy, zz, start, res)
            return max(res, 0)
        return dfs(x, y, z, 0)



so = Solution()
print(so.longestString(x = 1, y = 3, z = 1))
print(so.longestString(x = 2, y = 5, z = 1))
print(so.longestString(x = 3, y = 2, z = 2))




