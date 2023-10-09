class Solution:
    def addStrings(self, num1: str, num2: str):
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        short, long = len(num1), len(num2)
        for i in range(long-short):
            num1 = '0' + num1
        res = ''
        carry = 0
        for i in range(long-1, -1, -1):
            cur = int(num1[i]) + int(num2[i]) + carry
            if cur < 10:
                res = str(cur) + res
                carry = 0
            else:
                res = str(cur-10) + res
                carry = 1
        if 1 == carry:
            res = '1' + res
        return res




so = Solution()
print(so.addStrings('1','9'))
print(so.addStrings('123','1234'))
print(so.addStrings('1123','1234'))
#print(so.diffWaysToCompute("2*3-4*5"))

