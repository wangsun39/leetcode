
from leetcode.allcode.competition.mypackage import *

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = set()
        ans = []
        def helper(words):
            n = len(words)
            if n <= 1:
                return words
            n1, n2 = ''.join(sorted(list(words[-1]))), ''.join(sorted(list(words[-2])))
            if n1 == n2:
                return helper(words[:n - 1])
            return helper(words[:n - 1]) + [words[-1]]
        return helper(words)



so = Solution()
print(so.removeAnagrams(["abba","baba","bbaa","cd","cd"]))
print(so.removeAnagrams(["a","b","a"]))
print(so.removeAnagrams(["a","b","c","d","e"]))




