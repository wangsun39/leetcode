# 给定两个字符串 s 和 t ，每个字符串代表一个非负有理数，只有当它们表示相同的数字时才返回 true 。字符串中可以使用括号来表示有理数的重复部分。
#
# 有理数 最多可以用三个部分来表示：整数部分 <IntegerPart>、小数非重复部分 <NonRepeatingPart> 和小数重复部分 <(><RepeatingPart><)>。数字可以用以下三种方法之一来表示：
#
# <IntegerPart>
# 例： 0 ,12 和 123
# <IntegerPart><.><NonRepeatingPart>
# 例： 0.5 , 1. , 2.12 和 123.0001
# <IntegerPart><.><NonRepeatingPart><(><RepeatingPart><)>
# 例： 0.1(6) ， 1.(9)， 123.00(1212)
# 十进制展开的重复部分通常在一对圆括号内表示。例如：
#
# 1 / 6 = 0.16666666... = 0.1(6) = 0.1666(6) = 0.166(66)
#
#
# 示例 1：
#
# 输入：s = "0.(52)", t = "0.5(25)"
# 输出：true
# 解释：因为 "0.(52)" 代表 0.52525252...，而 "0.5(25)" 代表 0.52525252525.....，则这两个字符串表示相同的数字。
# 示例 2：
#
# 输入：s = "0.1666(6)", t = "0.166(66)"
# 输出：true
# 示例 3：
#
# 输入：s = "0.9(9)", t = "1."
# 输出：true
# 解释："0.9(9)" 代表 0.999999999... 永远重复，等于 1 。[有关说明，请参阅此链接]
# "1." 表示数字 1，其格式正确：(IntegerPart) = "1" 且 (NonRepeatingPart) = "" 。
#
#
# 提示：
#
# 每个部分仅由数字组成。
# 整数部分 <IntegerPart> 不会以零开头。（零本身除外）
# 1 <= <IntegerPart>.length <= 4
# 0 <= <NonRepeatingPart>.length <= 4
# 1 <= <RepeatingPart>.length <= 4

from leetcode.allcode.competition.mypackage import *

class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:

        def proc(s):
            a1 = b1 = c1 = None
            i = s.find('.')
            if i == -1:
                a1 = s
            elif i == len(s) - 1:
                a1 = s[:-1]
            else:
                a1 = s[:i]
                j = s.find('(')
                if j == -1:
                    b1 = s[i + 1:]
                else:
                    b1 = s[i + 1: j]
                    c1 = s[j + 1: len(s) - 1]
            if c1:
                lc = len(c1)
                if all(c1[i] == c1[0] for i in range(lc)):
                    c1 = c1[0]
                elif lc == 4:
                    if c1[:2] == c1[2:]:
                        c1 = c1[:2]
                lc = len(c1)
                if b1:  # 简化b1，把是循环周期内的去除掉
                    while len(b1) >= len(c1) and b1.endswith(c1):
                        b1 = b1[:len(b1) - lc]
                    while len(b1) and b1[-1] == c1[-1]:
                        b1 = b1[:-1]
                        c1 = c1[-1] + c1[:-1]
                if len(b1) == 0:
                    b1 = None
                if c1 == '0':
                    c1 = None
                elif c1 == '9':
                    if b1:
                        lb = len(b1)
                        b1 = str(int(b1) + 1)
                        if len(b1) < lb:
                            b1 = '0' * (lb - len(b1)) + b1
                    else:
                        a1 = str(int(a1) + 1)
                    c1 = None
            if c1 is None and b1 is not None and int(b1) == 0:
                b1 = None
            # print(a1, b1, c1)
            return a1, b1, c1
        return proc(s) == proc(t)






so = Solution()
print(so.isRationalEqual(s = "0.08(9)", t = "0.09"))
print(so.isRationalEqual(s = "1", t = "1.00"))
print(so.isRationalEqual(s = "1", t = "1.0"))
print(so.isRationalEqual(s = "0.9(9)", t = "1."))
print(so.isRationalEqual(s = "0.(52)", t = "0.5(25)"))
print(so.isRationalEqual(s = "0.1666(6)", t = "0.166(66)"))




