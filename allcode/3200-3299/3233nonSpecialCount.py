

from leetcode.allcode.competition.mypackage import *

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

primes = euler_all_primes(10 ** 5)
spec = [x * x for x in primes]

class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        p1 = bisect_right(spec, r)
        p2 = bisect_right(spec, l - 1)
        return r - l + 1 - (p1 - p2)



so = Solution()
print(so.nonSpecialCount(l = 182, r = 18677))
print(so.nonSpecialCount(l = 4, r = 7))
print(so.nonSpecialCount(l = 1, r = 4))
print(so.nonSpecialCount(l = 5, r = 7))
print(so.nonSpecialCount(l = 3, r = 7))
print(so.nonSpecialCount(l = 4, r = 16))




