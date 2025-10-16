
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
                return False
        return True


# 计数的Trie树
class Trie:

    def __init__(self):
        self.root = {'cnt': 0, 'end': 0}   # cnt 表示以当前节点为前缀的单词有多少个，'end' 表示以当前前缀作为单词的有多少个

    def insert(self, word: str) -> None:  # O(log(len(word)))
        cur = self.root
        for e in word:
            if e not in cur:
                cur[e] = {'cnt': 1}
            else:
                cur[e]['cnt'] += 1
            cur = cur[e]
        if 'end' not in cur:
            cur['end'] = 1
        else:
            cur['end'] += 1
        # cur['cnt'] += 1
        self.root['cnt'] += 1

    def countWordsEqualTo(self, word: str) -> int:
        cur = self.root
        for e in word:
            if e in cur:
                cur = cur[e]
            else:
                return 0
        if 'end' in cur:
            return cur['end']
        return 0

    def countWordsStartingWith(self, prefix: str) -> int:
        cur = self.root
        for e in prefix:
            if e in cur:
                cur = cur[e]
            else:
                return 0
        return cur['cnt']

    def erase(self, word: str) -> None:
        cur = self.root
        for i, e in enumerate(word):
            if cur[e]['cnt'] == 1:
                del(cur[e])
                return
            else:
                cur[e]['cnt'] -= 1
                if i == len(word) - 1:
                    break
            cur = cur[e]
        cur[e]['end'] -= 1
        self.root['cnt'] -= 1

    def startsWith(self, prefix: str) -> [str]:
        # 返回以前缀开头的所有词
        cur = self.root
        for e in prefix:
            if e in cur:
                cur = cur[e]
                if 'end' in cur:
                    return [x for x in cur if x != 'end']
            else:
                return []

        def dfs(node):
            if 'end' in node:
                return ['']
            res = []
            for x in node:
                l = dfs(node[x])
                res += [x + st for st in l]
            return res
        res = dfs(cur)
        return [prefix + x for x in res]


