class Solution:
    def baseNeg2(self, N: int):
        quotient = N
        strings = ''
        if 0 == N:
            return '0'
        while quotient != 0:
            quotient, remainder = self.division(quotient)
            strings = str(remainder) + strings
        return strings
    def division(self, N):
        # N = (-2) * quotient + remainder (0 <= remainder <= 1)
        # return quotient, remainder
        if N % 2 == 0:
            return N / (-2), 0
        remainder = 1
        quotient = (N - remainder) / (-2)
        return quotient, remainder


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
obj = Solution()
print(obj.baseNeg2(3))
print(obj.baseNeg2(4))

