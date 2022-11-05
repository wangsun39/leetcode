# 给你一个以字符串形式表述的 布尔表达式（boolean） expression，返回该式的运算结果。
#
# 有效的表达式需遵循以下约定：
#
# "t"，运算结果为 True
# "f"，运算结果为 False
# "!(expr)"，运算过程为对内部表达式 expr 进行逻辑 非的运算（NOT）
# "&(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 与的运算（AND）
# "|(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 或的运算（OR）
#
#
# 示例 1：
#
# 输入：expression = "!(f)"
# 输出：true
# 示例 2：
#
# 输入：expression = "|(f,t)"
# 输出：true
# 示例 3：
#
# 输入：expression = "&(t,f)"
# 输出：false
# 示例 4：
#
# 输入：expression = "|(&(t,f,t),!(t))"
# 输出：false
#
#
# 提示：
#
# 1 <= expression.length <= 20000
# expression[i] 由 {'(', ')', '&', '|', '!', 't', 'f', ','} 中的字符组成。
# expression 是以上述形式给出的有效表达式，表示一个布尔值。


import bisect
from functools import reduce
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        def calc(expr):
            if len(expr) == 1:
                return expr
            if expr[0] == '&':
                return reduce(lambda x, y: x & y, expr[1:])
            if expr[0] == '|':
                return reduce(lambda x, y: x | y, expr[1:])
            return not expr[1]
        i, n = 0, len(expression)
        while i < n:
            if expression[i] in 'tf':
                expr = True if expression[i] == 't' else False
                if len(stack) == 0:
                    stack.append(expr)
                else:
                    stack[-1].append(expr)
                i += 1
            elif expression[i] in '&|!':
                stack.append([expression[i]])
                i += 2
            elif expression[i] == ',':
                i += 1
            else:
                val = calc(stack.pop())
                if len(stack):
                    stack[-1].append(val)
                else:
                    stack.append(val)
                i += 1
        return stack[0]


obj = Solution()
print(obj.parseBoolExpr("!(f)"))
print(obj.parseBoolExpr("|(&(t,f,t),!(t))"))
print(obj.parseBoolExpr("|(f,t)"))
print(obj.parseBoolExpr("&(t,f)"))




