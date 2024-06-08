# 给你一个字符串 s 。它可能包含任意数量的 '*' 字符。你的任务是删除所有的 '*' 字符。
#
# 当字符串还存在至少一个 '*' 字符时，你可以执行以下操作：
#
# 删除最左边的 '*' 字符，同时删除该星号字符左边一个字典序 最小 的字符。如果有多个字典序最小的字符，你可以删除它们中的任意一个。
# 请你返回删除所有 '*' 字符以后，剩余字符连接而成的
# 字典序最小
#  的字符串。
#
#
#
# 示例 1：
#
# 输入：s = "aaba*"
#
# 输出："aab"
#
# 解释：
#
# 删除 '*' 号和它左边的其中一个 'a' 字符。如果我们选择删除 s[3] ，s 字典序最小。
#
# 示例 2：
#
# 输入：s = "abc"
#
# 输出："abc"
#
# 解释：
#
# 字符串中没有 '*' 字符。
#
#
#
# 提示：
#
# 1 <= s.length <= 105
# s 只含有小写英文字母和 '*' 字符。
# 输入保证操作可以删除所有的 '*' 字符。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)
        c2i = {c: i for i, c in enumerate(ascii_lowercase)}
        # i2c = {i: c for i, c in enumerate(ascii_lowercase)}
        delFlg = [0] * n
        idx = [[] for _ in range(26)]

        for i, x in enumerate(s):
            if x != '*':
                idx[c2i[x]].append(i)
                continue
            for j in range(26):
                if len(idx[j]) > 0:
                    k = idx[j].pop()
                    delFlg[k] = 1
                    break
        ans = []
        for i, x in enumerate(s):
            if x == '*' or delFlg[i]: continue
            ans.append(x)
        return ''.join(ans)




so = Solution()
print(so.clearStars("d*"))
print(so.clearStars("aaba*"))
print(so.clearStars("abc"))




