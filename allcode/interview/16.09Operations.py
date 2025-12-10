# 请实现整数数字的乘法、减法和除法运算，运算结果均为整数数字，程序中只允许使用加法运算符和逻辑运算符，允许程序中出现正负常数，不允许使用位运算。
#
# 你的实现应该支持如下操作：
#
# Operations() 构造函数
# minus(a, b) 减法，返回a - b
# multiply(a, b) 乘法，返回a * b
# divide(a, b) 除法，返回a / b
# 示例：
#
# Operations operations = new Operations();
# operations.minus(1, 2); //返回-1
# operations.multiply(3, 4); //返回12
# operations.divide(5, -2); //返回-2
# 提示：
#
# 你可以假设函数输入一定是有效的，例如不会出现除法分母为0的情况
# 单个用例的函数调用次数不会超过1000次

from leetcode.allcode.competition.mypackage import *


class Operations:

    def __init__(self):
        pass

    # 取相反数
    def flip(self, num):
        if num == 0:
            return num
        elif num < 0:
            add = 1
            res = 0
            while 1:
                count = add
                if num + count <= 0:
                    num += count
                    res += count
                else:
                    break
                while 1:
                    count = self.multiply2(count)
                    if num + count <= 0:
                        num += count
                        res += count
                    else:
                        break
            return res
        else:
            add = -1
            res = 0
            while 1:
                count = add
                if num + count >= 0:
                    num += count
                    res += count
                else:
                    break
                while 1:
                    count = self.multiply2(count)
                    if num + count >= 0:
                        num += count
                        res += count
                    else:
                        break
            return res

    def multiply2(self, x):
        return x + x

    def minus(self, a: int, b: int) -> int:
        return a + self.flip(b)

    def multiply(self, a: int, b: int) -> int:
        if a == 0 or b == 0: return 0
        if (a > 0 and b > 0) or (a < 0 and b < 0):
            sign = 1
        else:
            sign = -1
        if a < 0: a = self.flip(a)
        if b < 0: b = self.flip(b)
        if a < b: a, b = b, a
        power = [[1, a]]
        c = 1
        while c < b:
            x, y = power[-1]
            power.append([self.multiply2(x), self.multiply2(y)])  # [n, n*a] 其中n是2^i
            c += power[-1][0]

        res = 0
        cur = 0
        while cur < b:
            for cnt, val in power:
                if cur + cnt > b: break
                cur += cnt
                res += val
        if sign == 1: return res
        return self.flip(res)


    # def divide(self, a: int, b: int) -> int:






so = Operations()
print(so.multiply(5, 6))






