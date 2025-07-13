# 给定一份单词的清单，设计一个算法，创建由字母组成的面积最大的矩形，其中每一行组成一个单词(自左向右)，每一列也组成一个单词(自上而下)。不要求这些单词在清单里连续出现，但要求所有行等长，所有列等高。
#
# 如果有多个面积最大的矩形，输出任意一个均可。一个单词可以重复使用。
#
# 示例 1：
#
# 输入：["this", "real", "hard", "trh", "hea", "iar", "sld"]
# 输出：
# [
#    "this",
#    "real",
#    "hard"
# ]
# 示例 2：
#
# 输入：["aa"]
# 输出：["aa","aa"]
# 说明：
#
# words.length <= 1000
# words[i].length <= 100
# 数据保证单词足够随机


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
    def maxRectangle(self, words: List[str]) -> List[str]:
        tr = Trie()
        for w in words:
            tr.insert(w)




so = Solution()
print(so.getMaxMatrix(["this", "real", "hard", "trh", "hea", "iar", "sld"]))




