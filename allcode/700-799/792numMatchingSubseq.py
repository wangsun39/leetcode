# 给定字符串 s 和字符串数组 words, 返回  words[i] 中是s的子序列的单词个数 。
#
# 字符串的 子序列 是从原始字符串中生成的新字符串，可以从中删去一些字符(可以是none)，而不改变其余字符的相对顺序。
#
# 例如， “ace” 是 “abcde” 的子序列。
#
#
# 示例 1:
#
# 输入: s = "abcde", words = ["a","bb","acd","ace"]
# 输出: 3
# 解释: 有三个是 s 的子序列的单词: "a", "acd", "ace"。
# Example 2:
#
# 输入: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# 输出: 2
#
#
# 提示:
#
# 1 <= s.length <= 5 * 104
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 50
# words[i]和 s 都只由小写字母组成。


from leetcode.allcode.competition.mypackage import *

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ns = len(s)
        pos = [[-1] * 26 for _ in range(ns + 1)]  # 保存在s每个位置向后看，26个字母的每一个下一次出现的位置
        cur = [-1] * 26
        cur[ord(s[-1]) - ord('a')] = ns
        ans = 0
        for i in range(ns - 1, -1, -1):
            for j in range(26):
                pos[i][j] = cur[j]
            cur[ord(s[i - 1]) - ord('a')] = i
        print(pos)
        def judge(word):
            cur = 0
            for w in word:
                cur = pos[cur][ord(w) - ord('a')]
                if cur == -1:
                    return False
            return True

        for w in words:
            if judge(w):
                ans += 1
        return ans



so = Solution()
print(so.numMatchingSubseq(s = "abcde", words = ["a","bb","acd","ace"]))
print(so.numMatchingSubseq(s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]))

