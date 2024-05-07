# 给出 字符串 text 和 字符串列表 words, 返回所有的索引对 [i, j] 使得在索引对范围内的子字符串 text[i]...text[j]（包括 i 和 j）属于字符串列表 words。
#
#
#
# 示例 1:
#
# 输入: text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]
# 输出: [[3,7],[9,13],[10,17]]
# 示例 2:
#
# 输入: text = "ababa", words = ["aba","ab"]
# 输出: [[0,1],[0,2],[2,3],[2,4]]
# 解释:
# 注意，返回的配对可以有交叉，比如，"aba" 既在 [0,2] 中也在 [2,4] 中
#
#
# 提示:
#
# 所有字符串都只包含小写字母。
# 保证 words 中的字符串无重复。
# 1 <= text.length <= 100
# 1 <= words.length <= 20
# 1 <= words[i].length <= 50
# 按序返回索引对 [i,j]（即，按照索引对的第一个索引进行排序，当第一个索引对相同时按照第二个索引对排序）。

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

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        tr = Trie()
        for w in words:
            tr.insert(w)
        n = len(text)
        ans = []
        for i in range(n):
            for j in range(i + 1, n + 1):
                if tr.search(text[i: j]):
                    ans.append([i, j - 1])
        return ans




so = Solution()


