

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

# 只需找出sqrt(10 ** 5)以内的质数就可以了，其他的在计算过程中可以得到
primes = euler_all_primes(int((10 ** 5) ** 0.5) + 1)

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        nums = list(set(nums))
        n = len(nums)
        if n == 1:
            return nums[0] != 1

        d = defaultdict(list)

        fa = {x: x for x in nums}
        def find(x):
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]
        def union(x, y):
            fa[find(y)] = find(x)

        for x in nums:
            x0 = x
            for p in primes:
                if x % p != 0:
                    continue
                d[p].append(x0)
                union(x0, d[p][0])
                while x % p == 0:
                    x //= p
            if x > 1:
                d[x].append(x0)  # 剩下的是超过 sqrt(10 ** 5) 的质数
                union(x0, d[x][0])

        for x in nums:
            find(x)

        return all(find(x) == find(nums[0]) for x in nums)

so = Solution()
print(so.canTraverseAllPairs(nums = [51,46,4,3,48,9,49,7,54]))
print(so.canTraverseAllPairs(nums = [1,1]))
print(so.canTraverseAllPairs(nums = [20,6]))
print(so.canTraverseAllPairs(nums = [3,9,5]))
print(so.canTraverseAllPairs(nums = [2,3,6]))
print(so.canTraverseAllPairs(nums = [4,3,12,8]))




