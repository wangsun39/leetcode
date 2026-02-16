

from leetcode.allcode.competition.mypackage import *

pa_nums = [0] * 51  # 长度为n的二进制整数个数
pa_nums[1] = 2
pa_nums[2] = 1
for i in range(3, 51):
    l = (i - 2 + 1) // 2  # 剩余可变的半长度
    pa_nums[i] = 1 << l

s_pa_nums = list(accumulate(pa_nums))
# print(pa_nums)

class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        if n <= 1: return n + 1
        if n <= 3: return n

        s = bin(n)[2:]
        m = len(s)
        ans = s_pa_nums[m - 1]  # 比s长度短的二进制回文个数

        s1 = s[:(m + 1) // 2]
        h1 = int(s1[1:], 2)
        if m & 1:
            ss = s1 + s1[::-1][1:]
        else:
            ss = s1 + s1[::-1]
        if ss <= s:
            ans += h1 + 1
        else:
            ans += h1

        return ans


so = Solution()
print(so.countBinaryPalindromes(9))
print(so.countBinaryPalindromes(675))




