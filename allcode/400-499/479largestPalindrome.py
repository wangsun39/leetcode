# 给定一个整数 n ，返回 可表示为两个 n位整数乘积的 最大回文整数 。因为答案可能非常大，所以返回它对 1337 取余 。
#
#
#
# 示例 1:
#
# 输入：n = 2
# 输出：987
# 解释：99 x 91 = 9009, 9009 % 1337 = 987
# 示例 2:
#
# 输入： n = 1
# 输出： 9
#
#
# 提示:
#
# 1 <= n <= 8



import time


from typing import List
import copy
class Solution:
    def largestPalindrome(self, n: int) -> int:
        def getP(n):
            s1 = str(n)
            s2 = s1[::-1]
            return int(s1 + s2)
        def getP1(n):
            s1 = str(n)
            s2 = s1[:0:-1]
            return int(s1 + s2)
        for i in range(10 ** n - 1, 0, -1):
            p = getP(i)
            for k in range(10 ** n - 1, 0, -1):
                m = p % k
                l = p // k
                if l > k:
                    break
                if m == 0 and l > 10 ** (n - 1):
                    print(l, k)
                    return p % 1337
        for i in range(10 ** n - 1, 0, -1):
            p = getP1(i)
            for k in range(10 ** n - 1, 0, -1):
                m = p % k
                l = p // k
                if l > 10 ** (n - 1):
                    break
                if m == 0:
                    print(l, k)
                    return p % 1337


so = Solution()

print(so.largestPalindrome(2))      #9
print(so.largestPalindrome(8))      #9
print(so.largestPalindrome(1))      #9



