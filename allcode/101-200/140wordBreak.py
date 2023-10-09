# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
#
# 说明：
#
# 分隔时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 示例 1：
#
# 输入:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# 输出:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
# 示例 2：
#
# 输入:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# 输出:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# 解释: 注意你可以重复使用字典中的单词。
# 示例 3：
#
# 输入:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出:
# []



from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        cannotBreak = set()
        canBreak = {}
        Dict = set(wordDict)
        Dict.add('')
        def helper(s):
            N = len(s)
            if 0 == N or s in canBreak:
                return True
            res = False
            allBreak = []
            for i in range(N):
                if s[:i + 1] not in Dict or s[i + 1:] in cannotBreak:
                    continue
                if helper(s[i + 1:]):
                    res = True
                    if i == N - 1:
                        allBreak += [s]
                        break
                    allBreak += [s[:i + 1] + ' ' + x for x in canBreak[s[i + 1:]]]
            canBreak[s] = allBreak
            if not res:
                cannotBreak.add(s)
            return res

        if helper(s):
            return canBreak[s]
        return []


so = Solution()
print(so.wordBreak(s = "pineapplepenapple", wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]))
print(so.wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]))
print(so.wordBreak(s = "a", wordDict = ["a"]))
print(so.wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]))
print(so.wordBreak(s = "leetcode", wordDict = ["leet", "code"]))
print(so.wordBreak(s = "applepenapple", wordDict = ["apple", "pen"]))



