# 有效数字（按顺序）可以分成以下几个部分：
#
# 一个 小数 或者 整数
# （可选）一个 'e' 或 'E' ，后面跟着一个 整数
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
# 部分有效数字列举如下：
#
# ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
# 部分无效数字列举如下：
#
# ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
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
# 示例 4：
#
# 输入：s = ".1"
# 输出：true
#  
#
# 提示：
#
# 1 <= s.length <= 20
# s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，或者点 '.' 。


class Solution:
    def isNumber(self, s: str) -> bool:
        def isPureNum(s, isInt=False):
            N = len(s)
            if s[-1] in '-+':
                return False
            dotNum, digitNum = 0, 0
            for i, e in enumerate(s):
                if e in '0123456789':
                    digitNum += 1
                elif e == '.':
                    if 1 == dotNum or N - 1 == i == 0 or isInt:
                        return False
                    dotNum = 1
                elif e in '+-':
                    if 0 != i:
                        return False
                else:
                    return False
            return digitNum > 0
        if s[-1] in 'eE-+' or s[0] in 'eE':
            return False
        eNum = 0
        ePos = -1
        for i, e in enumerate(s):
            if e in 'eE':
                if 1 == eNum:
                    return False
                eNum += 1
                ePos = i
        if -1 == ePos:
            return isPureNum(s)
        return isPureNum(s[:ePos]) and isPureNum(s[ePos+1:], True)

    def isNumber1(self, s: str) -> bool:  # other solution
        s = s.strip()
        numbers = [str(i) for i in range(10)]
        n = len(s)

        e_show_up, dot_show_up, num_show_up, num_after_e = False, False, False, False

        for i in range(n):
            c = s[i]
            if c in numbers:
                num_show_up = True
                num_after_e = True
            elif c in ('+', '-'):
                if i > 0 and s[i-1] != 'e':
                    return False
            elif c == '.':
                if dot_show_up or e_show_up:
                    return False
                dot_show_up = True
            elif c == 'e':
                if e_show_up or not num_show_up:
                    return False
                e_show_up = True
                num_show_up = False
            else:
                return False

        return num_show_up and num_after_e





so = Solution()
print(so.isNumber("6e6.5"))  # False
print(so.isNumber("+."))  # False
print(so.isNumber("2e0"))  # True
print(so.isNumber("1e."))  # False
print(so.isNumber(".e1"))  # False
print(so.isNumber("3."))  # True
print(so.isNumber("."))  # False
print(so.isNumber("0"))  # True
print(so.isNumber("."))  # False

print(so.isNumber(".1"))  # True

print(so.isNumber1("1e+"))  # True