# 给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
# #
# # 说明：
# #
# # 拆分时可以重复使用字典中的单词。
# # 你可以假设字典中没有重复的单词。
# # 示例 1：
# #
# # 输入: s = "leetcode", wordDict = ["leet", "code"]
# # 输出: true
# # 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
# # 示例 2：
# #
# # 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# # 输出: true
# # 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
# #      注意你可以重复使用字典中的单词。
# # 示例 3：
# #
# # 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# # 输出: false


from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cannotBreak = set()
        Dict = set(wordDict)
        Dict.add('')
        def helper(s):
            N = len(s)
            for i in range(1, N + 1):
                if s[:i] not in Dict:
                    continue
                if s[i:] in Dict:
                    return True
                if s[i:] in cannotBreak:
                    continue
                if helper(s[i:]):
                    return True
                else:
                    cannotBreak.add(s[i:])
            return False
        return helper(s)


so = Solution()
print(so.wordBreak(s = "a", wordDict = ["a"]))
print(so.wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]))
print(so.wordBreak(s = "leetcode", wordDict = ["leet", "code"]))
print(so.wordBreak(s = "applepenapple", wordDict = ["apple", "pen"]))



