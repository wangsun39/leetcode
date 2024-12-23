# 你的任务是计算 ab 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。
#
#
#
# 示例 1：
#
# 输入：a = 2, b = [3]
# 输出：8
# 示例 2：
#
# 输入：a = 2, b = [1,0]
# 输出：1024
# 示例 3：
#
# 输入：a = 1, b = [4,3,3,8,5,2]
# 输出：1
# 示例 4：
#
# 输入：a = 2147483647, b = [2,0,0]
# 输出：1198
#
#
# 提示：
#
# 1 <= a <= 231 - 1
# 1 <= b.length <= 2000
# 0 <= b[i] <= 9
# b 不含前导 0

from leetcode.allcode.competition.mypackage import *

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        pow = [a % MOD]
        for _ in range(1, 2001):
            pow.append(pow[-1] ** 2 % MOD)
        n = len(b)
        ans = 1
        for i in range(n):
            j = n - i - 1
            x = b[j] * 10 ** i
            for k in range(x.bit_length()):
                if x & (1 << k):
                    ans *= pow[k]
                    ans %= MOD
        return ans



so = Solution()
print(so.superPow(a = 1, b = [4,3,3,8,5,2]))
print(so.superPow(a = 2, b = [1,0]))
print(so.superPow(a = 2, b = [3]))
print(so.superPow(a = 2147483647, b = [2,0,0]))




