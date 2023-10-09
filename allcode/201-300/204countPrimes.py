import math
class Solution:
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

so = Solution()
print(so.countPrimes(9))
print(so.countPrimes(1500000))
1500000

