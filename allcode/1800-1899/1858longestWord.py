# 给定一个字符串数组 words，找出 words 中所有的前缀都在 words 中的最长字符串。
#
# 例如，令 words = ["a", "app", "ap"]。字符串 "app" 含前缀 "ap" 和 "a" ，都在 words 中。
# 返回符合上述要求的字符串。如果存在多个（符合条件的）相同长度的字符串，返回字典序中最小的字符串，如果这样的字符串不存在，返回 ""。
#
#
#
# 示例 1:
#
# 输入： words = ["k","ki","kir","kira", "kiran"]
# 输出： "kiran"
# 解释： "kiran" 含前缀 "kira"、 "kir"、 "ki"、 和 "k"，这些前缀都出现在 words 中。
# 示例 2:
#
# 输入： words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# 输出： "apple"
# 解释： "apple" 和 "apply" 都在 words 中含有各自的所有前缀。
# 然而，"apple" 在字典序中更小，所以我们返回之。
# 示例 3:
#
# 输入： words = ["abc", "bc", "ab", "qwe"]
# 输出： ""
#
#
# 提示：
#
# 1 <= words.length <= 105
# 1 <= words[i].length <= 105
# 1 <= sum(words[i].length) <= 105

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
                if 'end' not in cur:
                    return False
            else:
                return False
        return 'end' in cur

class Solution:
    def longestWord(self, words: List[str]) -> str:
        tr = Trie()
        for w in words:
            tr.insert(w)

        ans = ''  # 最长字符串

        for w in words:
            if tr.search(w):
                if len(w) > len(ans) or (len(w) == len(ans) and w < ans):
                    ans = w

        return ans

so = Solution()

print(so.longestWord(words = ["k","ki","kir","kira", "kiran"]))
print(so.longestWord(words = ["k","ki","kir","kira", "kiran"]))
print(so.longestWord(words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]))
print(so.longestWord(words = ["abc", "bc", "ab", "qwe"]))




