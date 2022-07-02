class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = (numerator * denominator) < 0
        numerator, denominator = abs(numerator), abs(denominator)
        integer, remain = numerator // denominator, numerator % denominator  # 整数部分
        if 0 == remain:
            return ('-' if sign else '') + str(integer)
        dividends = {remain: 0}  # 被除数序列
        decimal = '' # 小数部分
        loop = 0
        while True:
            remain *= 10
            loop += 1
            # remain == c1 * denominator + c2
            c1, c2 = remain // denominator, remain % denominator
            decimal += str(c1)
            if 0 == c2:
                break
            if c2 in dividends:
                idx = dividends[c2]
                decimal = decimal[:idx] + '(' + decimal[idx:] + ')'
                break
            dividends[c2] = loop
            remain = c2
        return ('-' if sign else '') + str(integer) + '.' + decimal

so = Solution()
print(so.fractionToDecimal(-2147483648, 1))
print(so.fractionToDecimal(-50, 8))
print(so.fractionToDecimal(22, 7))
print(so.fractionToDecimal(1, 2))
print(so.fractionToDecimal(2, 1))
print(so.fractionToDecimal(2, 3))
