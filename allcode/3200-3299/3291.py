

from leetcode.allcode.competition.mypackage import *

class Trie:

    def __init__(self, target):
        self.root = {}
        self.target = target
        self.n = len(target)

    def insert(self, word: str) -> None:  # O(log(len(word)))
        cur = self.root
        for e in word:
            if e not in cur:
                cur[e] = {}
            cur = cur[e]
        cur['end'] = True


    def search(self, word: str) -> bool:
        cur = self.root
        for e in word:
            if e in cur:
                cur = cur[e]
            else:
                return False
        return 'end' in cur



    def longest_match(self, start: str) -> bool:
        cur = self.root
        res = 0
        for i in range(start, self.n):
            e = self.target[i]
            if e in cur:
                cur = cur[e]
                res += 1
            else:
                break
        return res

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        tr = Trie(target)
        n = len(target)
        for w in words:
            tr.insert(w)

        @cache
        def dfs(start):
            if start == n: return 0
            length = tr.longest_match(start)
            if length == 0:
                return inf
            res = inf
            for i in range(length):
                v = dfs(start + i + 1)
                if v + 1 < res:
                    res = v + 1
            return res

        ans = dfs(0)
        if ans == inf:
            return -1
        return ans


so = Solution()
print(so.minValidStrings(words = ["abc","aaaaa","bcdef"], target = "aabcdabc"))
print(so.minValidStrings(words = ["abababab","ab"], target = "ababaababa"))
print(so.minValidStrings( words = ["abcdef"], target = "xyz"))




