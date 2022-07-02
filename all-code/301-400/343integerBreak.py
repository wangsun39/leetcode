class Solution:
    def integerBreak(self, n: int):
        l = self.integerBreakBy2or3(n)
        product = self.mulByElement(l)
        return product
    def integerBreakBy2or3(self, n):
        #分解成2或3，且3尽量多
        num_3 = n // 3
        remain = n % 3
        if 1 == remain:
            num_2 = 2
            num_3 -= 1
        elif 2 == remain:
            num_2 = 1
        else:
            num_2 = 0
        if 1 == num_2 + num_3:
            l = [1, n-1]
        else:
            l = [3] * num_3 + [2] * num_2
        return l
    def mulByElement(self, l):
        product = 1
        for i in l:
            product *= i
        return product



so = Solution()
print(so.integerBreak(3))




