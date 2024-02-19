

from leetcode.allcode.competition.mypackage import *

class Trie:

    def __init__(self):
        self.root = {'cnt': 0}

    def insert(self, word: str) -> None:  # O(log(len(word)))
        cur = self.root
        for e in word:
            if e not in cur:
                cur[e] = {'cnt': 0}
            cur = cur[e]
        cur['end'] = True
        cur['cnt'] += 1


    def search(self, word: str) -> bool:
        cur = self.root
        for e in word:
            if e in cur:
                cur = cur[e]
            else:
                return False
        return 'end' in cur



    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for e in prefix:
            if e in cur:
                cur = cur[e]
            else:
                return 0
        return cur['cnt']


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def z_function(s):
            n = len(s)
            z = [0] * n
            l, r = 0, 0
            for i in range(1, n):
                if i <= r and z[i - l] < r - i + 1:
                    z[i] = z[i - l]
                else:
                    z[i] = max(0, r - i + 1)
                    while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                        z[i] += 1
                if i + z[i] - 1 > r:
                    l = i
                    r = i + z[i] - 1
            return z
        tr = Trie()
        ans = 0
        for word in words[::-1]:
            ans += tr.startsWith(word)
            z = z_function(word)
            n = len(word)
            z[0] = n
            for i, x in enumerate(z):
                if x == n - i:
                    tr.insert(word[i:])
        return ans

so = Solution()
print(so.countPrefixSuffixPairs(words = ["bb","bb"]))
print(so.countPrefixSuffixPairs(words = ["a","aba","ababa","aa"]))
print(so.countPrefixSuffixPairs(words = ["pa","papa","ma","mama"]))
print(so.countPrefixSuffixPairs(words = ["abab","ab"]))




