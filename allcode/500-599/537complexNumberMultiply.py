# 给定两个表示复数的字符串。
#
# 返回表示它们乘积的字符串。注意，根据定义 i2 = -1 。
#
# 示例 1:
#
# 输入: "1+1i", "1+1i"
# 输出: "0+2i"
# 解释: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i ，你需要将它转换为 0+2i 的形式。
# 示例 2:
#
# 输入: "1+-1i", "1+-1i"
# 输出: "0+-2i"
# 解释: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i ，你需要将它转换为 0+-2i 的形式。
# 注意:
#
# 输入字符串不包含额外的空格。
# 输入字符串将以a+bi 的形式给出，其中整数 a 和 b 的范围均在 [-100, 100] 之间。输出也应当符合这种形式。



from typing import List
from collections import defaultdict

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def getNumFromStr(num1):
            l = num1.split('+')
            return int(l[0]), int(l[1][:-1])
        a1, b1 = getNumFromStr(num1)
        a2, b2 = getNumFromStr(num2)
        a3 = a1 * a2 - b1 * b2
        b3 = a1 * b2 + a2 * b1
        return str(a3) + '+' + str(b3) + 'i'

so = Solution()
print(so.complexNumberMultiply("1+1i", "1+1i"))
print(so.complexNumberMultiply("1+-1i", "1+-1i"))

