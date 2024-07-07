

from leetcode.allcode.competition.mypackage import *

class Trie:

    def __init__(self, target):
        self.root = {}
        self.target = target
        self.n = len(target)

    def insert(self, word: str, cost: int) -> None:  # O(log(len(word)))
        cur = self.root
        for e in word:
            if e not in cur:
                cur[e] = {}
            cur = cur[e]
        cur['end'] = cost


    def search(self, word: str) -> bool:
        cur = self.root
        for e in word:
            if e in cur:
                cur = cur[e]
            else:
                return False
        return 'end' in cur



    def startsWith(self, start: int) -> list:
        cur = self.root
        res = []  # 返回 [len, cost] 的数组
        dep = 0
        for i in range(start, self.n):
            e = self.target[i]
            if e in cur:
                cur = cur[e]
                dep += 1
                if 'end' in cur:
                    res.append([dep, cur['end']])
            else:
                break

        return res

class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        tr = Trie(target)
        n = len(target)
        d = {}
        for w, c in zip(words, costs):
            if w not in d:
                d[w] = c
            else:
                d[w] = min(d[w], c)
        for w, c in d.items():
            tr.insert(w, c)

        vis = [inf] * (n + 1)
        vis[-1] = 0

        @cache
        def dfs(start):
            if start == n:
                return 0
            mn = inf
            res = tr.startsWith(start)
            for l, c in res:
                if vis[start + l] < inf:
                    v = vis[start + l] + c
                else:
                    v = dfs(start + l) + c
                if mn > v:
                    mn = v
            vis[start] = mn
            return mn
        ans = dfs(0)
        return -1 if ans == inf else ans


so = Solution()
print(so.minimumCost("r",["r","r","r","r"],[1,6,3,3]))
print(so.minimumCost(target = "abcdef", words = ["abdef","abc","d","def","ef"], costs = [100,1,1,10,5]))
print(so.minimumCost(target = "aaaa", words = ["z","zz","zzz"], costs = [1,10,100]))




