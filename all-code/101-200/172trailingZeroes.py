import math
class Solution:
    def trailingZeroes(self, n: int):
        if 0 == n:
            return 0
        N = int(math.log(n, 5))
        sum = 0
        for i in range(N, 0, -1):
            x = n // pow(5, i)
            sum += x
        return sum

so = Solution();
print(so.trailingZeroes(5))
print(so.trailingZeroes(11))

