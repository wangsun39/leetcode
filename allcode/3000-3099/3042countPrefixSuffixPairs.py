

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    ans += 1
        return ans


so = Solution()
print(so.countPrefixSuffixPairs(words = ["a","aba","ababa","aa"]))
print(so.countPrefixSuffixPairs(words = ["pa","papa","ma","mama"]))
print(so.countPrefixSuffixPairs(words = ["abab","ab"]))




