

from leetcode.allcode.competition.mypackage import *

class Trie:

    def __init__(self):
        self.root = {'cnt': 0}

    def insert(self, idx, word: str) -> None:  # O(log(len(word)))
        cur = self.root
        for e in word:
            if e not in cur:
                cur[e] = {'cnt': 0}
            if 'min' in cur:
                # a, b = cur['min']
                # print(cur['min'], [len(word), idx], cur['min'] > [len(word), idx])
                if cur['min'] > [len(word), idx]:
                    cur['min'] = [len(word), idx]
                # print(cur['min'])
                # cur['min'] = min(cur['min'], [len(word), idx])
            else:
                cur['min'] = [len(word), idx]
            cur = cur[e]
        if 'end' not in cur:
            cur['end'] = idx
        cur['cnt'] += 1


    def search(self, word: str) -> int:
        cur = self.root
        for e in word:
            if e in cur:
                cur = cur[e]
            else:
                return 0
        if 'end' in cur:
            return cur['cnt']
        return 0

    def startsWith(self, prefix: str) -> int:
        cur = self.root
        pre = self.root
        for e in prefix:
            if e in cur:
                pre = cur
                cur = cur[e]
            else:
                # if 'end' in pre:
                #     return pre['end']
                # return pre['min'][1]
                if 'end' in cur:
                    return cur['end']
                return cur['min'][1]
        # return cur['cnt']
        if 'end' in cur:
            return cur['end']
        return cur['min'][1]


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        wordsContainer = [w[::-1] for w in wordsContainer]
        wordsQuery = [w[::-1] for w in wordsQuery]
        tr = Trie()
        for i, w in enumerate(wordsContainer):
            tr.insert(i, w)
        ans = [0] * len(wordsQuery)
        for i, w in enumerate(wordsQuery):
            ans[i] = tr.startsWith(w)
        return ans



so = Solution()
print(so.stringIndices(["abcde","abcde"],
["abcde","bcde","cde","de","e"]))
print(so.stringIndices(wordsContainer = ["a","b","ghghgh"], wordsQuery = ["a","b"]))
print(so.stringIndices(wordsContainer = ["abcdefgh","poiuygh","ghghgh"], wordsQuery = ["gh","acbfgh","acbfegh","ghghgh"]))
print(so.stringIndices(wordsContainer = ["abcd","bcd","xbcd"], wordsQuery = ["cd","bcd","xyz"]))




