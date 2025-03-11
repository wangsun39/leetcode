

# 有个内含单词的超大文本文件，给定任意两个不同的单词，找出在这个文件中这两个单词的最短距离(相隔单词数)。如果寻找过程在这个文件中会重复多次，而每次寻找的单词不同，你能对此优化吗?
#
# 示例：
#
# 输入：words = ["I","am","a","student","from","a","university","in","a","city"], word1 = "a", word2 = "student"
# 输出：1
# 提示：
#
# words.length <= 100000

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        d = defaultdict(list)
        for i, w in enumerate(words):
            d[w].append(i)
        def find(l1, l2):
            i, j = 0, 0
            ans = 1e9
            while i < len(l1) and j < len(l2):
                if l1[i] < l2[j]:
                    ans = min(ans, l2[j] - l1[i])
                    i += 1
                else:
                    ans = min(ans, l1[i] - l2[j])
                    j += 1
            return ans
        return find(d[word1], d[word2])




so = Solution()
print(so.findClosest(["I","am","a","student","from","a","university","in","a","city"], word1 = "a", word2 = "student"))




