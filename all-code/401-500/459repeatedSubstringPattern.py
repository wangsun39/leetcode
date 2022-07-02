# 给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。
#
# 示例 1:
#
# 输入: "abab"
#
# 输出: True
#
# 解释: 可由子字符串 "ab" 重复两次构成。
# 示例 2:
#
# 输入: "aba"
#
# 输出: False
# 示例 3:
#
# 输入: "abcabcabcabc"
#
# 输出: True
#
# 解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)


from typing import List
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        N = len(s)
        if N <= 1:
            return False
        def isRepeated(len):
            times = N // len
            for i in range(len):
                for j in range(1, times):
                    if s[i] != s[j * len + i]:
                        return False
            return True
        isPrime = True
        for i in range(2, N // 2 + 1):
            if N % i == 0:
                isPrime = False
                if isRepeated(i):
                    return True
        if isPrime:
            return isRepeated(1)
        return False




so = Solution()
print(so.repeatedSubstringPattern("a"))
print(so.repeatedSubstringPattern("abab"))
print(so.repeatedSubstringPattern("aba"))
print(so.repeatedSubstringPattern("aaa"))
print(so.repeatedSubstringPattern("ab"))
print(so.repeatedSubstringPattern("aa"))
print(so.repeatedSubstringPattern("abcabcabcabc"))


