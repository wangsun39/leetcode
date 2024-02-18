

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

primes = euler_all_primes(10 ** 6)
primes = set(x for x in primes if x > 10)
class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        counter = Counter()
        dir = [[-1, 0], [1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1], [0, -1], [0, 1]]
        r, c = len(mat), len(mat[0])

        def proc(i, j):
            for u, v in dir:
                num = mat[i][j]
                for k in range(1, max(r, c)):
                    x, y = i + u * k, j + v * k
                    if x < 0 or x >= r or y < 0 or y >= c:
                        break
                    num = num * 10 + mat[x][y]
                    if num in primes:
                        counter[num] += 1


        for i in range(r):
            for j in range(c):
                proc(i, j)
        if len(counter) == 0:
            return -1
        counter = [[k, v] for k, v in counter.items()]
        counter.sort(key=lambda x: [x[1], x[0]], reverse=True)
        return counter[0][0]



so = Solution()
print(so.mostFrequentPrime(mat = [[4,5,3]]))
print(so.mostFrequentPrime(mat = [[1,1],[9,9],[1,1]]))
print(so.mostFrequentPrime(mat = [[7]]))
print(so.mostFrequentPrime(mat = [[9,7,8],[4,6,5],[2,8,6]]))




