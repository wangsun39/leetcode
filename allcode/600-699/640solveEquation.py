# 求解一个给定的方程，将x以字符串 "x=#value"的形式返回。该方程仅包含 '+' ， '-' 操作，变量x和其对应系数。
#
# 如果方程没有解，请返回"No solution"。如果方程有无限解，则返回 “Infinite solutions” 。
#
# 题目保证，如果方程中只有一个解，则 'x' 的值是一个整数。
#
#
#
# 示例 1：
#
# 输入: equation = "x+5-3+x=6+x-2"
# 输出: "x=2"
# 示例 2:
#
# 输入: equation = "x=x"
# 输出: "Infinite solutions"
# 示例 3:
#
# 输入: equation = "2x=x"
# 输出: "x=0"
#
#
# 提示:
#
# 3 <= equation.length <= 1000
# equation只有一个'='.
# equation方程由整数组成，其绝对值在[0, 100]范围内，不含前导零和变量 'x' 。


from typing import List
class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split('=')
        def helper(s):
            res = []
            pos = 0
            for i, e in enumerate(s):
                if e in '+-' and pos != i:
                    res.append(s[pos:i])
                    pos = i
                if i == len(s) - 1:
                    res.append(s[pos:i + 1])
            first, second = '', ''
            for e in res:
                if e == '+x':
                    first += '+1'
                elif e == '-x':
                    first += '-1'
                elif e[-1] == 'x':
                    first += (e[:-1] if len(e) > 1 else '1')
                else:
                    second += e
            return eval(first) if len(first) else 0, eval(second) if len(second) else 0
        left, right = helper(left), helper(right)
        # print(left, right)
        if left[0] == right[0]:
            if left[1] == right[1]:
                return 'Infinite solutions'
            else:
                return 'No solution'
        else:
            return 'x=' + str((right[1] - left[1]) // (left[0] - right[0]))


so = Solution()
print(so.solveEquation("-x=-1"))
print(so.solveEquation("x+5-3+x=6+x-2"))
print(so.solveEquation("x=x"))
print(so.solveEquation("2x=x"))

