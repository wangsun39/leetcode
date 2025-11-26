# 给定一个较长字符串big和一个包含较短字符串的数组smalls，设计一个方法，根据smalls中的每一个较短字符串，对big进行搜索。输出smalls中的字符串在big里出现的所有位置positions，其中positions[i]为smalls[i]出现的所有位置。
#
# 示例：
#
# 输入：
# big = "mississippi"
# smalls = ["is","ppi","hi","sis","i","ssippi"]
# 输出： [[1,4],[8],[],[3],[1,4,7,10],[5]]
# 提示：
#
# 0 <= len(big) <= 1000
# 0 <= len(smalls[i]) <= 1000
# smalls的总字符数不会超过 106。
# 你可以认为smalls中没有重复字符串。
# 所有出现的字符均为英文小写字母。

from leetcode.allcode.competition.mypackage import *

class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str, idx: int) -> None:  # O(log(len(word)))
        cur = self.root
        for e in word:
            if e not in cur:
                cur[e] = {'ids': [idx]}
            else:
                cur[e]['ids'].append(idx)
            cur = cur[e]

    def search(self, word: str) -> List[int]:
        cur = self.root
        m = len(word)
        for i, e in enumerate(word):
            if e in cur:
                cur = cur[e]
                if i == m - 1:
                    return cur['ids']
            else:
                return []
        return []


class Solution:
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        n = len(big)
        tr = Trie()
        for i in range(n):
            tr.insert(big[i:], i)
        ans = []
        for w in smalls:
            ans.append(tr.search(w))
        return ans


so = Solution()
print(so.multiSearch("mississippi", ["is","ppi","hi","sis","i","ssippi"]))




