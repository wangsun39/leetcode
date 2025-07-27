

from leetcode.allcode.competition.mypackage import *

min = lambda a, b: b if b < a else a
max = lambda a, b: b if b > a else a

def all_primes(n):
    is_prime = [False, False] + [True] * (n - 1)
    flg = False
    for i in range(2, n + 1):
        if not is_prime[i]: continue
        if flg:
            continue
        if i * i > n:
            flg = True
            continue
        j = i * i
        while j < n + 1:
            is_prime[j] = False
            j += i
    return is_prime

primes = all_primes(10 ** 6 + 1)

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        p_next = defaultdict(list)  # 质数的相邻节点 (包括质数和非质数)
        for i, x in enumerate(nums):
            if primes[x]:
                p_next[x].append(i)
        @cache
        def prime_factors(x):
            res = []
            i = 2
            while i * i <= x:
                if x % i != 0:
                    i += 1
                    continue
                res.append(i)
                while x % i == 0:
                    x //= i
                i += 1
            if x > 1:
                res.append(x)
            return res

        for i, x in enumerate(nums):
            if not primes[x]:
                arr = prime_factors(x)
                for y in arr:
                    p_next[y].append(i)

        dist = [inf] * n
        dist[0] = 0
        h = [(0, 0)]
        p_vis = set()  # 记录哪些质数已经访问过
        while h:
            d, i = heappop(h)
            x = nums[i]
            cand = []
            if i - 1 >= 0 and dist[i - 1] == inf:
                cand.append(i - 1)
            if i + 1 < n and dist[i + 1] == inf:
                cand.append(i + 1)
            if x in p_next and x not in p_vis:
                cand += p_next[x]
                p_vis.add(x)

            for y in cand:
                new_d = dist[i] + 1
                if new_d < dist[y]:
                    dist[y] = new_d
                    heappush(h, (new_d, y))

        return dist[n - 1]


so = Solution()
print(so.minJumps(nums = [2,7,7]))
print(so.minJumps(nums = [1,2,4,6]))
print(so.minJumps(nums = [7,5,7]))
print(so.minJumps(nums = [4,5,2]))




