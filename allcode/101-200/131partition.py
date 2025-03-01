# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
#
#
#
# 示例 1：
#
# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
# 示例 2：
#
# 输入：s = "a"
# 输出：[["a"]]
#
#
# 提示：
#
# 1 <= s.length <= 16
# s 仅由小写英文字母组成

from leetcode.allcode.competition.mypackage import *

class Solution:
    def partition1(self, s: str) -> List[List[str]]:
        d = {}
        def isPalindrome(s):
            i, N = 0, len(s)
            while i < N // 2:
                if s[i] != s[N-1-i]:
                    return False
                i += 1
            return True
        def helper(s):
            nonlocal d
            res = []
            i, N = 0, len(s)
            if 1 == N:
                return [[s[0]]]
            while i < N:
                if isPalindrome(s[:i+1]):
                    if s[i+1:] in d:
                        subStrSet = d[s[i+1:]]
                    else:
                        subStrSet = helper(s[i+1:])
                        d[s[i+1:]] = subStrSet
                    if i+1 == N:
                        res.append([s[:i+1]])
                    else:
                        for x in subStrSet:
                            res.append([s[:i+1]] + x)
                i += 1
            return res
        return helper(s)

    def partition(self, s: str) -> List[List[str]]:
        # 2025/3/1 简化写法
        n = len(s)

        @cache
        def check(b, e):
            return s[b: e] == s[b: e][::-1]

        @cache
        def dfs(start):
            if start == n: return [[]]
            res = []
            for end in range(start + 1, n + 1):
                if check(start, end):
                    arr = dfs(end)
                    for l in arr:
                        res.append([s[start: end]] + l)
            return res
        return dfs(0)

so = Solution()
print(so.partition('aa'))
print(so.partition('aab'))


