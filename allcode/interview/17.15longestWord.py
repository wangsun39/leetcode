# 给定一组单词words，编写一个程序，找出其中的最长单词，且该单词由这组单词中的其他单词组合而成。若有多个长度相同的结果，返回其中字典序最小的一项，若没有符合要求的单词则返回空字符串。
#
# 示例：
#
# 输入： ["cat","banana","dog","nana","walk","walker","dogwalker"]
# 输出： "dogwalker"
# 解释： "dogwalker"可由"dog"和"walker"组成。
# 提示：
#
# 0 <= len(words) <= 200
# 1 <= len(words[i]) <= 100

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

    def search(self, word: str) -> List[int]:
        cur = self.root
        i = 0
        res = []
        for e in word:
            if 'end' in cur:
                res.append(i)
            if e in cur:
                cur = cur[e]
                i += 1
            else:
                break
        if 'end' in cur:
            res.append(i)
        return res




class Solution:
    def longestWord(self, words: List[str]) -> str:
        tr = Trie()
        for w in words:
            tr.insert(w)

        words.sort(key=lambda x: [-len(x), x])

        def check(word, flg):
            m = len(word)
            idx = tr.search(word)
            if flg == 0:
                if len(idx) <= 1:
                    return False
            else:
                if idx and idx[-1] == m: return True
            for i in idx:
                if i == m: continue
                if check(word[i:], 1):
                    return True
            return False


        for w in words:
            if check(w, 0):
                return w

        return ''





so = Solution()
print(so.longestWord(["cat","banana","dog","nana","walk","walker","dogwalker"]))




