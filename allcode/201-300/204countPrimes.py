# 给定整数 n ，返回 所有小于非负整数 n 的质数的数量 。
#
#
#
# 示例 1：
#
# 输入：n = 10
# 输出：4
# 解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
# 示例 2：
#
# 输入：n = 0
# 输出：0
# 示例 3：
#
# 输入：n = 1
# 输出：0
#
#
# 提示：
#
# 0 <= n <= 5 * 106

from leetcode.allcode.competition.mypackage import *
class Solution1:
    def countPrimes(self, n: int):
        if n <= 2:
            return 0
        dict_Primes = {}
        dict_Primes[2] = True
        for i in range(3, n):
            dict_Primes[i] = False if i%2 == 0 else True
        upper = int(math.sqrt(n))+1
        for i in range(3, upper):
            #print(dict_Primes)
            if not dict_Primes[i]:
                continue
            j = i
            while i * j < n:
                dict_Primes[i*j] = False
                j += 1
            #print(i, dict_Primes)
        num = 0
        for k in dict_Primes:
            if dict_Primes[k]:
                num += 1
        return num

# 2024/5/2  素数筛
def euler_all_primes(n):
    is_prime = [False, False] + [True] * (n - 1)
    primes = []
    flg = False
    for i in range(2, n + 1):
        if is_prime[i]: primes.append(i)
        if flg: continue
        for j in primes:
            if j * i > n: break
            is_prime[j * i] = False
            if i % j == 0: break

    return primes

primes = euler_all_primes(5 * 10 ** 6)

class Solution:
    def countPrimes(self, n: int) -> int:
        return bisect_left(primes, n)

so = Solution()
print(so.countPrimes(9))
print(so.countPrimes(1500000))
1500000

