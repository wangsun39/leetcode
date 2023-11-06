

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        w = [0] * n  # 按 bit 位表示每个单词
        for i, x in enumerate(words):
            cur = 0
            for y in x:
                cur |= 1 << (ord(y) - ord('a'))
            w[i] = cur
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if w[i] & w[j] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans



so = Solution()
print(so.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
print(so.maxProduct(["a","ab","abc","d","cd","bcd","abcd"]))
print(so.maxProduct(["a","aa","aaa","aaaa"]))




