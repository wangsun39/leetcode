# 给你一个下标从 0 开始的字符串 expression ，格式为 "<num1>+<num2>" ，其中 <num1> 和 <num2> 表示正整数。
#
# 请你向 expression 中添加一对括号，使得在添加之后， expression 仍然是一个有效的数学表达式，并且计算后可以得到 最小 可能值。左括号 必须 添加在 '+' 的左侧，而右括号必须添加在 '+' 的右侧。
#
# 返回添加一对括号后形成的表达式 expression ，且满足 expression 计算得到 最小 可能值。如果存在多个答案都能产生相同结果，返回任意一个答案。
#
# 生成的输入满足：expression 的原始值和添加满足要求的任一对括号之后 expression 的值，都符合 32-bit 带符号整数范围。
#
#  
#
# 示例 1：
#
# 输入：expression = "247+38"
# 输出："2(47+38)"
# 解释：表达式计算得到 2 * (47 + 38) = 2 * 85 = 170 。
# 注意 "2(4)7+38" 不是有效的结果，因为右括号必须添加在 '+' 的右侧。
# 可以证明 170 是最小可能值。
# 示例 2：
#
# 输入：expression = "12+34"
# 输出："1(2+3)4"
# 解释：表达式计算得到 1 * (2 + 3) * 4 = 1 * 5 * 4 = 20 。
# 示例 3：
#
# 输入：expression = "999+999"
# 输出："(999+999)"
# 解释：表达式计算得到 999 + 999 = 1998 。
#  
#
# 提示：
#
# 3 <= expression.length <= 10
# expression 仅由数字 '1' 到 '9' 和 '+' 组成
# expression 由数字开始和结束
# expression 恰好仅含有一个 '+'.
# expression 的原始值和添加满足要求的任一对括号之后 expression 的值，都符合 32-bit 带符号整数范围





from typing import List
from collections import deque
# Definition for a binary tree node.
from collections import Counter
class Solution:
    def minimizeResult(self, expression: str) -> str:
        l = expression.split('+')
        left, right = l[0], l[1]
        n1, n2 = len(left), len(right)
        print(l)
        minE, minV = '', 9999999999999
        for i in range(n1):
            for j in range(n2):
                newS = left[:i] + '(' + left[i:] + '+' + right[:j + 1] + ')' + right[j + 1:]
                if i == 0 and j == n2 - 1:
                    newE = '1' + left[:i] + '*(' + left[i:] + '+' + right[:j + 1] + ')*1' + right[j + 1:]
                elif i == 0:
                    newE = '(' + left[i:] + '+' + right[:j + 1] + ')*' + right[j + 1:]
                elif j == n2 - 1:
                    newE = left[:i] + '*(' + left[i:] + '+' + right[:j + 1] + ')'
                else:
                    newE = left[:i] + '*(' + left[i:] + '+' + right[:j + 1] + ')*' + right[j + 1:]
                #
                # print(newE)
                # print(eval(newE))
                v = eval(newE)
                if v < minV:
                    minV = v
                    minE = newS
        return minE

so = Solution()
# print(so.kthPalindrome([2,9,7,6], intLength = 1))
# print(so.kthPalindrome([2,201429812,8,520498110,492711727,339882032,462074369,9,7,6], intLength = 1))
# print(so.kthPalindrome([1,100,3,4,5,90], intLength = 3))
# print(so.kthPalindrome([1,2,3,4,5,90], intLength = 3))
# print(so.kthPalindrome([2,4,6], intLength = 4))

