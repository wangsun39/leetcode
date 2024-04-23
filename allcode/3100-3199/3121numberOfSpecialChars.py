# 给你一个字符串 word。如果 word 中同时出现某个字母 c 的小写形式和大写形式，并且 每个 小写形式的 c 都出现在第一个大写形式的 c 之前，则称字母 c 是一个 特殊字母 。
#
# 返回 word 中 特殊字母 的数量。
#
#
#
# 示例 1:
#
# 输入：word = "aaAbcBC"
#
# 输出：3
#
# 解释：
#
# 特殊字母是 'a'、'b' 和 'c'。
#
# 示例 2:
#
# 输入：word = "abc"
#
# 输出：0
#
# 解释：
#
# word 中不存在特殊字母。
#
# 示例 3:
#
# 输入：word = "AbBCab"
#
# 输出：0
#
# 解释：
#
# word 中不存在特殊字母。
#
#
#
# 提示：
#
# 1 <= word.length <= 2 * 105
# word 仅由小写和大写英文字母组成。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        pos1 = [-1] * 26
        pos2 = [-1] * 26
        c2i = {c: i for i, c in enumerate(ascii_lowercase)}
        C2i = {c: i for i, c in enumerate(ascii_uppercase)}
        for i, x in enumerate(word):
            if x.isupper():
                if pos1[C2i[x]] == -1:
                    pos1[C2i[x]] = i
            else:
                pos2[c2i[x]] = i
        ans = 0
        for i in range(26):
            if pos1[i] > pos2[i] != -1:
                ans += 1
        return ans


so = Solution()
print(so.numberOfSpecialChars("AbBCab"))
print(so.numberOfSpecialChars("aaAbcBC"))
print(so.numberOfSpecialChars("abc"))
print(so.numberOfSpecialChars("AbBCab"))




