# 给出一个单词数组 words ，其中每个单词都由小写英文字母组成。
#
# 如果我们可以 不改变其他字符的顺序 ，在 wordA 的任何地方添加 恰好一个 字母使其变成 wordB ，那么我们认为 wordA 是 wordB 的 前身 。
#
# 例如，"abc" 是 "abac" 的 前身 ，而 "cba" 不是 "bcad" 的 前身
# 词链是单词 [word_1, word_2, ..., word_k] 组成的序列，k >= 1，其中 word1 是 word2 的前身，word2 是 word3 的前身，依此类推。一个单词通常是 k == 1 的 单词链 。
#
# 从给定单词列表 words 中选择单词组成词链，返回 词链的 最长可能长度 。
#
#
# 示例 1：
#
# 输入：words = ["a","b","ba","bca","bda","bdca"]
# 输出：4
# 解释：最长单词链之一为 ["a","ba","bda","bdca"]
# 示例 2:
#
# 输入：words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
# 输出：5
# 解释：所有的单词都可以放入单词链 ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
# 示例 3:
#
# 输入：words = ["abcd","dbqca"]
# 输出：1
# 解释：字链["abcd"]是最长的字链之一。
# ["abcd"，"dbqca"]不是一个有效的单词链，因为字母的顺序被改变了。
#
#
# 提示：
#
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] 仅由小写英文字母组成。

from typing import List
from functools import cache
from math import *
from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        nt = defaultdict(list)  # 记录 i 的后面的节点list
        n = len(words)
        def check(x, y):
            if len(x) != len(y) - 1: return False
            m = len(x)
            i = j = 0
            cnt = 0
            while i < m and j < m + 1:
                if x[i] != y[j]:
                    j += 1
                    cnt += 1
                    if cnt > 1: return False
                else:
                    i += 1
                    j += 1
            return True
        for i in range(n - 1):
            for j in range(i, n):
                if check(words[i], words[j]):
                    nt[j].append(i)

        @cache
        def dfs(i):
            mx = 0
            for x in nt[i]:
                ll = dfs(x)
                mx = max(ll, mx)
            return mx + 1
        ans = 0
        for i in range(n):
            res = dfs(i)
            if res > ans:
                ans = res
        return ans



obj = Solution()
print(obj.longestStrChain(words = ["a","b","ba","bca","bda","bdca"]))
print(obj.longestStrChain(words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]))
print(obj.longestStrChain(words = ["abcd","dbqca"]))

