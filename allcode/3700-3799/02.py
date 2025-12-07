

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

N = 5 * (10 ** 5) + 1

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

    return is_prime

is_prime = euler_all_primes(N)
cand = []

ss = 0
for i in range(2, N):
    if is_prime[i]:
        ss += i
        if ss > N: break
        cand.append(ss)


class Solution:
    def largestPrime(self, n: int) -> int:
        if n < 2: return 0
        p = bisect_right(cand, n)
        return cand[p - 1]



so = Solution()
print(so.largestPrime(20))




