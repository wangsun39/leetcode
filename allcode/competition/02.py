

from leetcode.allcode.competition.mypackage import *

class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:  # O(log(len(word)))
        cur = self.root
        for e in word:
            if e not in cur:
                cur[e] = {}
            cur = cur[e]
        cur['end'] = True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        cnt = 0
        for e in prefix:
            if e in cur:
                cur = cur[e]
                cnt += 1
            else:
                break
        return cnt

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1 = sorted(str(x) for x in arr1)
        arr2 = sorted(str(x) for x in arr2)
        tr = Trie()
        for w in arr1:
            tr.insert(w)
        ans = 0
        for w in arr2:
            ans = max(ans, tr.startsWith(w))
        return ans


so = Solution()
print(so.longestCommonPrefix(arr1 = [1,10,100], arr2 = [1000]))
print(so.longestCommonPrefix(arr1 = [1,2,3], arr2 = [4,4,4]))




