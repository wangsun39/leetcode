# 给你一个字符串 word，请你使用以下算法进行压缩：
#
# 从空字符串 comp 开始。当 word 不为空 时，执行以下操作：
# 移除 word 的最长单字符前缀，该前缀由单一字符 c 重复多次组成，且该前缀长度 最多 为 9 。
# 将前缀的长度和字符 c 追加到 comp 。
# 返回字符串 comp 。
#
#
#
#
#
# 示例 1：
#
# 输入：word = "abcde"
#
# 输出："1a1b1c1d1e"
#
# 解释：
#
# 初始时，comp = "" 。进行 5 次操作，每次操作分别选择 "a"、"b"、"c"、"d" 和 "e" 作为前缀。
#
# 对每个前缀，将 "1" 和对应的字符追加到 comp。
#
# 示例 2：
#
# 输入：word = "aaaaaaaaaaaaaabb"
#
# 输出："9a5a2b"
#
# 解释：
#
# 初始时，comp = ""。进行 3 次操作，每次操作分别选择 "aaaaaaaaa"、"aaaaa" 和 "bb" 作为前缀。
#
# 对于前缀 "aaaaaaaaa"，将 "9" 和 "a" 追加到 comp。
# 对于前缀 "aaaaa"，将 "5" 和 "a" 追加到 comp。
# 对于前缀 "bb"，将 "2" 和 "b" 追加到 comp。
#
#
# 提示：
#
# 1 <= word.length <= 2 * 105
# word 仅由小写英文字母组成。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def compressedString(self, word: str) -> str:
        n = len(word)
        prei = 0
        ans = []
        for i in range(1, n):
            x = word[i]
            if x == word[prei]:
                if i - prei == 9:
                    ans.append('9' + x)
                    prei = i
            else:
                ans.append(str(i - prei) + word[i - 1])
                prei = i
        ans.append(str(n - prei) + word[-1])
        return ''.join(ans)


so = Solution()
print(so.compressedString(word = "abcde"))
print(so.compressedString(word = "aaaaaaaaaaaaaabb"))




