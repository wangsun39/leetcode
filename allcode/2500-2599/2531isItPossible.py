# 给你两个下标从 0 开始的字符串 word1 和 word2 。
#
# 一次 移动 由以下两个步骤组成：
#
# 选中两个下标 i 和 j ，分别满足 0 <= i < word1.length 和 0 <= j < word2.length ，
# 交换 word1[i] 和 word2[j] 。
# 如果可以通过 恰好一次 移动，使 word1 和 word2 中不同字符的数目相等，则返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
# 输入：word1 = "ac", word2 = "b"
# 输出：false
# 解释：交换任何一组下标都会导致第一个字符串中有 2 个不同的字符，而在第二个字符串中只有 1 个不同字符。
# 示例 2：
#
# 输入：word1 = "abcc", word2 = "aab"
# 输出：true
# 解释：交换第一个字符串的下标 2 和第二个字符串的下标 0 。之后得到 word1 = "abac" 和 word2 = "cab" ，各有 3 个不同字符。
# 示例 3：
#
# 输入：word1 = "abcde", word2 = "fghij"
# 输出：true
# 解释：无论交换哪一组下标，两个字符串中都会有 5 个不同字符。
#
#
# 提示：
#
# 1 <= word1.length, word2.length <= 105
# word1 和 word2 仅由小写英文字母组成。

from leetcode.allcode.competition.mypackage import *

class Solution:

    def isItPossible(self, word1: str, word2: str) -> bool:
        c1, c2 = Counter(word1), Counter(word2)
        if len(c1) > len(c2): c1, c2 = c2, c1
        if len(c2) - len(c1) > 2: return False
        if len(c1) == len(c2) and len(c1.keys() & c2.keys()): return True
        n1, n2 = len(c1), len(c2)
        for x in c1:
            for y in c2:
                if x == y and c1[x] > 0 and c2[y] > 0:
                    continue
                d1 = 0 if c1[x] > 1 else -1
                d1 += (0 if y in c1 else 1)
                d2 = 0 if c2[y] > 1 else -1
                d2 += (0 if x in c2 else 1)
                if n1 + d1 == n2 + d2:
                    return True
        return False



so = Solution()
print(so.isItPossible(word1 = "a", word2 = "bb"))
print(so.isItPossible(word1 = "ab", word2 = "abcc"))
print(so.isItPossible(word1 = "ac", word2 = "b"))
print(so.isItPossible(word1 = "abcc", word2 = "aab"))
print(so.isItPossible(word1 = "abcde", word2 = "fghij"))




