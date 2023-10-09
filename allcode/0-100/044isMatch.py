# 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
#
# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）。
# 两个字符串完全匹配才算匹配成功。
#
# 说明:
#
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
# 示例 1:
#
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 示例 2:
#
# 输入:
# s = "aa"
# p = "*"
# 输出: true
# 解释: '*' 可以匹配任意字符串。
# 示例 3:
#
# 输入:
# s = "cb"
# p = "?a"
# 输出: false
# 解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
# 示例 4:
#
# 输入:
# s = "adceb"
# p = "*a*b"
# 输出: true
# 解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
# 示例 5:
#
# 输入:
# s = "acdcb"
# p = "a*c?b"
# 输出: false


class Solution:
    def __init__(self):
        self.count = 0

    def isMatch(self, s: str, p: str) -> bool:
        def simplify(p):
            N = len(p)
            if 0 == N:
                return p
            res = p[0]
            for i in range(1, N):
                if res[-1] == p[i] == '*':
                    continue
                res += p[i]
            return res
        def findAllStrInp():
            res = []
            N = len(p)
            start = 0
            while start < N:
                if p[start] in ('?', '*'):
                    start += 1
                    continue
                end = start + 1
                while True:
                    if end >= N or p[end] in ('?', '*'):
                        res.append(p[start:end])
                        break
                    end += 1
                start = end
            return res, len(p) > 0 and p[-1] not in ('?', '*')
        def isHaveAllSub(s, sub):
            for x in sub:
                pos = s.find(x)
                if pos == -1:
                    return False
                s = s[pos + len(x):]
            return True
        def isEqual(s, p):  # p 中只包含 * 和 ？
            if p.count('?') > len(s):
                return False
            if 0 == p.count('*') and p.count('?') < len(s):
                return False
            return True
        def helper(s, p, sub):
            self.count += 1
            if p.count('?') > len(s):
                return False
            if 0 == len(sub):  # p 不含字母
                if '*' not in p:
                    return len(s) == p.count('?')
                return True
            if not isHaveAllSub(s, sub):
                return False
            pos = 0
            pos2 = p.find(sub[0])
            while pos < len(s):
                pos1 = s.find(sub[0], pos)
                if -1 == pos1:
                    return False
                s1, p1 = s[:pos1], p[:pos2]  # p第一个字母前的部分必须匹配
                if not isEqual(s1, p1):
                    pos = pos + 1
                    continue
                if helper(s[pos1 + len(sub[0]):], p[pos2 + len(sub[0]):], sub[1:]):
                    return True
                pos = pos + 1
            return False

        p = simplify(p)
        allSubStr, isEnd = findAllStrInp()
        if isEnd:  # p 以字母结尾时，sub[-1]必须与s末尾相同
            if allSubStr[-1] != s[-len(allSubStr[-1]):]:
                return False
        return helper(s, p, allSubStr)


so = Solution()
print(so.isMatch("", ""))  # True
print(so.isMatch("adceb", "*a*b"))  # True
print(so.isMatch("bbbbbbbabbaabbabbbbaaabbabbabaaabbababbbabbbabaaabaab", "b*b*ab**ba*b**b***bba"))  # False
print(so.count)
print(so.isMatch("abaa", "*?*a"))  # True
print(so.isMatch("abc", "*abc?*"))  # False
print(so.isMatch("b", "?"))  # True
print(so.isMatch("ab", "?*"))  # True
print(so.isMatch("acdcb", "a*c?b"))  # False
print(so.isMatch("aa", "a"))  # False
print(so.isMatch("adceb", "a*b"))  # True
print(so.isMatch("bbaaaabaaaaabbabbabbabbababaabababaabbabaaabbaababababbabaabbabbbbbbaaaaaabaabbbbbabbbbabbabababaaaaa", "******aa*bbb*aa*a*bb*ab***bbba*a*babaab*b*aa*a****"))  # False
print(so.isMatch("babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb", "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"))  # False

print(so.isMatch("aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba", "a*******b"))  # False
print(so.isMatch("aa", "*"))  # True
print(so.isMatch("cb", "?a"))  # False
