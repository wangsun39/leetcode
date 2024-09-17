# 给你一个字符串数组 words 和一个字符串 target。
#
# 如果字符串 x 是 words 中 任意 字符串的
# 前缀
# ，则认为 x 是一个 有效 字符串。
#
# 现计划通过 连接 有效字符串形成 target ，请你计算并返回需要连接的 最少 字符串数量。如果无法通过这种方式形成 target，则返回 -1。
#
#
#
# 示例 1：
#
# 输入： words = ["abc","aaaaa","bcdef"], target = "aabcdabc"
#
# 输出： 3
#
# 解释：
#
# target 字符串可以通过连接以下有效字符串形成：
#
# words[1] 的长度为 2 的前缀，即 "aa"。
# words[2] 的长度为 3 的前缀，即 "bcd"。
# words[0] 的长度为 3 的前缀，即 "abc"。
# 示例 2：
#
# 输入： words = ["abababab","ab"], target = "ababaababa"
#
# 输出： 2
#
# 解释：
#
# target 字符串可以通过连接以下有效字符串形成：
#
# words[0] 的长度为 5 的前缀，即 "ababa"。
# words[0] 的长度为 5 的前缀，即 "ababa"。
# 示例 3：
#
# 输入： words = ["abcdef"], target = "xyz"
#
# 输出： -1
#
#
#
# 提示：
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 5 * 103
# 输入确保 sum(words[i].length) <= 105。
# words[i] 只包含小写英文字母。
# 1 <= target.length <= 5 * 103
# target 只包含小写英文字母。

from leetcode.allcode.competition.mypackage import *

class Trie:

    def __init__(self, target):
        self.root = {}
        self.target = target
        self.n = len(target)

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



    def longest_match(self, start: str) -> bool:
        cur = self.root
        res = 0
        for i in range(start, self.n):
            e = self.target[i]
            if e in cur:
                cur = cur[e]
                res += 1
            else:
                break
        return res

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        tr = Trie(target)
        n = len(target)
        for w in words:
            tr.insert(w)

        @cache
        def dfs(start):
            if start == n: return 0
            length = tr.longest_match(start)
            if length == 0:
                return inf
            res = inf
            for i in range(length):
                v = dfs(start + i + 1)
                if v + 1 < res:
                    res = v + 1
            return res

        ans = dfs(0)
        if ans == inf:
            return -1
        return ans


so = Solution()
print(so.minValidStrings(words = ["abc","aaaaa","bcdef"], target = "aabcdabc"))
print(so.minValidStrings(words = ["abababab","ab"], target = "ababaababa"))
print(so.minValidStrings( words = ["abcdef"], target = "xyz"))




