# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
#
# 示例 1:
#
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
# 示例 2:
#
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
# 说明：
#
# num1 和 num2 的长度小于110。
# num1 和 num2 只包含数字 0-9。
# num1 和 num2 均不以零开头，除非是数字 0 本身。
# 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def mulSingle(num1, single): # single表示一位数数字
            carry = 0  # 表示进位的数字
            res = ''
            for x in num1[::-1]:
                c = int(x) * single + carry
                res = str(c % 10) + res
                carry = c // 10
            if carry > 0:
                res = str(carry) + res
            return res
        def add(num1, num2):
            N = max(len(num1), len(num2))
            num1 = '0' * (N - len(num1)) + num1
            num2 = '0' * (N - len(num2)) + num2
            carry = 0
            res = ''
            for i in range(N-1, -1, -1):
                c = int(num1[i]) + int(num2[i]) + carry
                res = str(c % 10) + res
                carry = c // 10
            if carry > 0:
                res = str(carry) + res
            return res

        if '0' == num2[0] or '0' == num1[0]:
            return '0'
        res = ''
        N2 = len(num2)
        for i in range(N2):
            cur = mulSingle(num1, int(num2[N2 - i - 1]))
            cur += ('0' * i)
            print(cur)
            res = add(res, cur)
        return res


so = Solution()
print(so.multiply("723", "459"))
