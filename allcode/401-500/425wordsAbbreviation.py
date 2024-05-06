# 给定一个单词集合 words （没有重复），找出并返回其中所有的 单词方块 。 words 中的同一个单词可以被 多次 使用。你可以按 任意顺序 返回答案。
#
# 一个单词序列形成了一个有效的 单词方块 的意思是指从第 k 行和第 k 列  0 <= k < max(numRows, numColumns) 来看都是相同的字符串。
#
# 例如，单词序列 ["ball","area","lead","lady"] 形成了一个单词方块，因为每个单词从水平方向看和从竖直方向看都是相同的。
#
#
# 示例 1：
#
# 输入：words = ["area","lead","wall","lady","ball"]
# 输出: [["ball","area","lead","lady"],
# ["wall","area","lead","lady"]]
# 解释：
# 输出包含两个单词方块，输出的顺序不重要，只需要保证每个单词方块内的单词顺序正确即可。
# 示例 2：
#
# 输入：words = ["abat","baba","atan","atal"]
# 输出：[["baba","abat","baba","atal"],
# ["baba","abat","baba","atan"]]
# 解释：
# 输出包含两个单词方块，输出的顺序不重要，只需要保证每个单词方块内的单词顺序正确即可。
#
#
# 提示:
#
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 4
# words[i] 长度相同
# words[i] 只由小写英文字母组成
# words[i] 都 各不相同

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



    def startsWith(self, prefix: str) -> [str]:
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


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        tr = Trie()
        for w in words:
            tr.insert(w)

        ans = []
        for w1 in words:
            if len(w1) > 1:
                for w2 in tr.startsWith(w1[1]):
                    if len(w2) > 2:
                        for w3 in tr.startsWith(w1[2] + w2[2]):
                            if len(w3) > 3:
                                for w4 in tr.startsWith(w1[3] + w2[3] + w3[3]):
                                    ans.append([w1, w2, w3, w4])
                            else:
                                ans.append([w1, w2, w3])
                    else:
                        ans.append([w1, w2])
            else:
                ans.append([w1])

        return ans



so = Solution()
print(so.wordSquares(["a"]))
print(so.wordSquares(["area","lead","wall","lady","ball"]))




