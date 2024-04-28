# 给你一个字符串 s 和一个整数 k 。
#
# 定义函数 distance(s1, s2) ，用于衡量两个长度为 n 的字符串 s1 和 s2 之间的距离，即：
#
# 字符 'a' 到 'z' 按 循环 顺序排列，对于区间 [0, n - 1] 中的 i ，计算所有「 s1[i] 和 s2[i] 之间 最小距离」的 和 。
# 例如，distance("ab", "cd") == 4 ，且 distance("a", "z") == 1 。
#
# 你可以对字符串 s 执行 任意次 操作。在每次操作中，可以将 s 中的一个字母 改变 为 任意 其他小写英文字母。
#
# 返回一个字符串，表示在执行一些操作后你可以得到的 字典序最小 的字符串 t ，且满足 distance(s, t) <= k 。
#
#
#
# 示例 1：
#
# 输入：s = "zbbz", k = 3
# 输出："aaaz"
# 解释：在这个例子中，可以执行以下操作：
# 将 s[0] 改为 'a' ，s 变为 "abbz" 。
# 将 s[1] 改为 'a' ，s 变为 "aabz" 。
# 将 s[2] 改为 'a' ，s 变为 "aaaz" 。
# "zbbz" 和 "aaaz" 之间的距离等于 k = 3 。
# 可以证明 "aaaz" 是在任意次操作后能够得到的字典序最小的字符串。
# 因此，答案是 "aaaz" 。
# 示例 2：
#
# 输入：s = "xaxcd", k = 4
# 输出："aawcd"
# 解释：在这个例子中，可以执行以下操作：
# 将 s[0] 改为 'a' ，s 变为 "aaxcd" 。
# 将 s[2] 改为 'w' ，s 变为 "aawcd" 。
# "xaxcd" 和 "aawcd" 之间的距离等于 k = 4 。
# 可以证明 "aawcd" 是在任意次操作后能够得到的字典序最小的字符串。
# 因此，答案是 "aawcd" 。
# 示例 3：
#
# 输入：s = "lol", k = 0
# 输出："lol"
# 解释：在这个例子中，k = 0，更改任何字符都会使得距离大于 0 。
# 因此，答案是 "lol" 。
#
#
# 提示：
#
# 1 <= s.length <= 100
# 0 <= k <= 2000
# s 只包含小写英文字母。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        c2i = {c: i for i, c in enumerate(ascii_lowercase)}
        ans = list(s)
        n = len(s)
        for i in range(n):
            v = min(c2i[s[i]], 26 - c2i[s[i]])
            if v <= k:
                k -= v
                ans[i] = 'a'
            else:
                ans[i] = chr(ord(s[i]) - k)
                break
        return ''.join(ans)


so = Solution()
print(so.getSmallestString(s = "rn", k = 9))
print(so.getSmallestString(s = "zbbz", k = 3))
print(so.getSmallestString(s = "xaxcd", k = 4))
print(so.getSmallestString(s = "lol", k = 0))



