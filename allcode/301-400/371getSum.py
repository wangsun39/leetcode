# 给你两个整数 a 和 b ，不使用 运算符 + 和 - ​​​​​​​，计算并返回两整数之和。
#
#
#
# 示例 1：
#
# 输入：a = 1, b = 2
# 输出：3
# 示例 2：
#
# 输入：a = 2, b = 3
# 输出：5
#
#
# 提示：
#
# -1000 <= a, b <= 1000

from leetcode.allcode.competition.mypackage import *

class Solution:
    def getSum(self, a: int, b: int) -> int:
        def add(a, b):
            ans = 0
            carry = 0
            for i in range(11):
                if (a >> i) & 1 and (b >> i) & 1:
                    if carry:
                        ans |= (1 << i)
                    carry = 1
                elif (a >> i) & 1 or (b >> i) & 1:
                    if not carry:
                        ans |= (1 << i)
                else:
                    if carry:
                        ans |= (1 << i)
                        carry = 0
            return ans
        def sub(a, b):
            ans = 0
            carry = 0
            for i in range(11):
                if (a >> i) & 1 and (b >> i) & 1:
                    if carry:
                        ans |= (1 << i)
                elif (a >> i) & 1:
                    if carry:
                        carry = 0
                    else:
                        ans |= (1 << i)
                elif (b >> i) & 1:
                    if not carry:
                        ans |= (1 << i)
                        carry = 1
                else:
                    if carry:
                        ans |= (1 << i)
            return ans
        if a * b >= 0:
            if a >= 0 and b >= 0:
                return add(a, b)
            else:
                return -add(-a, -b)
        else:
            if abs(a) < abs(b):
                a, b = b, a
            if a < 0:
                return -sub(-a, b)
            else:
                return sub(a, -b)




so = Solution()
print(so.getSum(a = -1, b = -2))
print(so.getSum(a = -1, b = 2))
print(so.getSum(a = 1, b = 2))
print(so.getSum(a = 1, b = -2))




