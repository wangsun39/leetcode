# 设计一个函数把两个数字相加。不得使用 + 或者其他算术运算符。
#
# 示例：
#
# 输入：a = 1, b = 1
# 输出：2
#
#
# 提示：
#
# a, b 均可能是负数或 0
# 结果不会溢出 32 位整数

from typing import List

class Solution:
    def add(self, a: int, b: int) -> int:

        def add1(a, b):
            c = 0
            carry = 0
            for i in range(32):
                x = a & 1
                y = b & 1
                a >>= 1
                b >>= 1
                if x == 0 and y == 0:
                    c |= carry << i
                    carry = 0
                elif (x == 0 and y == 1) or (x == 1 and y == 0):
                    if carry == 0:
                        c |= 1 << i
                else:
                    if carry == 0:
                        carry = 1
                    else:
                        c |= 1 << i
                if a == 0 == b:
                    if carry:
                        c |= 1 << (i + 1)
                    return c
        def sub(a, b):
            if abs(a) < abs(b):
                if a < 0:
                    sign = 1
                else:
                    sign = -1
                a, b = b, a
            else:
                if a < 0:
                    sign = -1
                else:
                    sign = 1
            a, b = abs(a), abs(b)
            c = 0
            carry = 0
            for i in range(32):
                x = a & 1
                y = b & 1
                a >>= 1
                b >>= 1
                if (x == 0 and y == 0) or (x == 1 and y == 1):
                    if carry:
                        c |= (1 << i)
                elif x == 1 and y == 0:
                    if carry == 0:
                        c |= (1 << i)
                    else:
                        carry = 0
                else:
                    if carry == 0:
                        c |= (1 << i)
                        carry = 1
                if a == 0 == b:
                    return c if sign == 1 else -c

        if a >= 0 and b >= 0:
            return add1(a, b)
        if a <= 0 and b <= 0:
            return -add1(-a, -b)
        return sub(a, b)



so = Solution()
print(so.add(a = 79, b = -734))
print(so.add(a = 111, b = 899))
print(so.add(a = 1, b = 1))
print(so.add(a = 5, b = -3))
print(so.add(a = -5, b = 3))

