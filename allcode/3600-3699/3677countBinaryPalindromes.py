

from leetcode.allcode.competition.mypackage import *

min = lambda a, b: b if b < a else a
max = lambda a, b: b if b > a else a

class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        if n <= 1: return n + 1
        if n == 2: return 2
        if n == 3: return 3
        s = str(bin(n)[2:])
        print(s)
        m = len(s)
        ans = 3
        for i in range(3, m):  # 长度小于m的数的回文数统计
            ha = (i + 1) // 2 - 1
            ans += (1 << ha)
        half1 = s[1: (m + 1) // 2]
        half2 = s[(m + 1) // 2: -1][::-1]
        print(half1, half2)
        half = min(half1, half2)
        ans += int(half, 2) + 1
        print("expect", self.countBinaryPalindromes3(n))
        return ans

    def countBinaryPalindromes3(self, n: int) -> int:
        ans = 0
        for i in range(n + 1):
            bi = bin(i)[2:]
            rbi = bi[::-1]
            if bi == rbi:
                ans += 1
        return ans




so = Solution()
print(so.countBinaryPalindromes(675))
print(so.countBinaryPalindromes(9))




