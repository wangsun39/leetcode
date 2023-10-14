
from leetcode.allcode.competition.mypackage import *

class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:

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
        ans = []
        primes = euler_all_primes(n)
        primes = set(primes)
        for i in range(2, n // 2 + 1):
            if i in primes and n - i in primes and i <= n - i:
                ans.append([i, n - i])
        return ans


so = Solution()
print(so.findPrimePairs(10 ** 6))
print(so.findPrimePairs(10))
print(so.findPrimePairs(2))




