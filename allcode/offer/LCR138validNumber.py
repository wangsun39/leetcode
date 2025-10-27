# 有效数字（按顺序）可以分成以下几个部分：
#
# 若干空格
# 一个 小数 或者 整数
# （可选）一个 'e' 或 'E' ，后面跟着一个 整数
# 若干空格
# 小数（按顺序）可以分成以下几个部分：
#
# （可选）一个符号字符（'+' 或 '-'）
# 下述格式之一：
# 至少一位数字，后面跟着一个点 '.'
# 至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
# 一个点 '.' ，后面跟着至少一位数字
# 整数（按顺序）可以分成以下几个部分：
#
# （可选）一个符号字符（'+' 或 '-'）
# 至少一位数字
# 部分有效数字列举如下：["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
#
# 部分无效数字列举如下：["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
#
# 给你一个字符串 s ，如果 s 是一个 有效数字 ，请返回 true 。
#
#
#
# 示例 1：
#
# 输入：s = "0"
# 输出：true
# 示例 2：
#
# 输入：s = "e"
# 输出：false
# 示例 3：
#
# 输入：s = "."
# 输出：false
#
#
# 提示：
#
# 1 <= s.length <= 20
# s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，空格 ' ' 或者点 '.' 。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def validNumber(self, s: str) -> bool:
        s = s.strip()
        s = s.split('e')
        if len(s) > 2 or len(s) == 0: return False
        if len(s) == 1:
            s = s[0]
            s = s.split('E')
            if len(s) > 2 or len(s) == 0: return False
        if len(s) == 2:
            a, b = s
            if len(a) == 0 or len(b) == 0: return False
        else:
            a, b = s[0], ''
            if len(a) == 0: return False

        def isInt(ss: str):
            if ss[0] in '+-':
                ss = ss[1:]
            if len(ss) == 0: return False
            return all('0' <= c <= '9' for c in ss)

        def isNum(ss: str):
            if ss[0] in '+-':
                ss = ss[1:]
            if len(ss) == 0: return False
            if ss == '.': return False
            p = ss.find('.')
            if p == -1:
                return all('0' <= c <= '9' for c in ss)
            a, b = ss[: p], ss[p + 1:]
            return all('0' <= c <= '9' for c in a) and all('0' <= c <= '9' for c in b)

        if b == '': return isNum(a)
        return isNum(a) and isInt(b)


so = Solution()
print(so.validNumber('+e3'))
print(so.validNumber('3.'))
print(so.validNumber('0e'))




