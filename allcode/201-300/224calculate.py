# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
#
# 注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。
#
#
#
# 示例 1：
#
# 输入：s = "1 + 1"
# 输出：2
# 示例 2：
#
# 输入：s = " 2-1 + 2 "
# 输出：3
# 示例 3：
#
# 输入：s = "(1+(4+5+2)-3)+(6+8)"
# 输出：23
#
#
# 提示：
#
# 1 <= s.length <= 3 * 105
# s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
# s 表示一个有效的表达式
# '+' 不能用作一元运算(例如， "+1" 和 "+(2 + 3)" 无效)
# '-' 可以用作一元运算(即 "-1" 和 "-(2 + 3)" 是有效的)
# 输入中不存在两个连续的操作符
# 每个数字和运行的计算将适合于一个有符号的 32位 整数

from leetcode.allcode.competition.mypackage import *

class Solution:
    def calculate1(self, s: str) -> int:
        stack = [[1, 0]]
        sign = 1
        i = 0
        while i < len(s):
            if '(' == s[i]:
                stack.append([sign, 0])
                sign = 1
            elif ')' == s[i]:
                e = stack.pop()
                stack[-1][1] += (e[0] * e[1])
            elif s[i].isdigit():
                cur = int(s[i])
                while i+1 < len(s) and s[i+1].isdigit():
                    cur = cur * 10 + int(s[i+1])
                    i += 1
                stack[-1][1] += (sign * cur)
            elif '+' == s[i]:
                sign = 1
            elif '-' == s[i]:
                sign = -1
            i += 1
        return stack[0][1]

    def calculate(self, s: str) -> int:
        # 2025/6/21 双栈法
        s = s.replace(' ', '')
        nums = []
        ops = []
        i = 0
        n = len(s)

        def calc():
            y = nums.pop()
            x = nums.pop()
            op = ops.pop()
            if op == '+':
                z = x + y
            else:
                z = x - y
            nums.append(z)
        while i < n:
            x = s[i]
            if x == '(':
                ops.append(x)
            elif x == ')':
                while ops[-1] != '(':
                    calc()
                ops.pop()
                while ops and ops[-1] in '+-':
                    calc()
            elif x in '+-':
                if i == 0 or (i and s[i-1] == '('):
                    # 补0，比如 -1+2 开头的负号前补0
                    nums.append(0)
                ops.append(x)
            else:
                v = int(x)
                while i + 1 < len(s) and s[i + 1].isdigit():
                    v = v * 10 + int(s[i + 1])
                    i += 1
                nums.append(v)
                while ops and ops[-1] in '+-':
                    calc()
            i += 1
        return nums[0]




so = Solution()
print(so.calculate("(1+(4+5+2)-3)+(6+8)"))
print(so.calculate("1 + 1"))
print(so.calculate(" 2-1 + 2 "))

