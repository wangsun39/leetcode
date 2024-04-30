# 给你一个二维整数数组 queries ，其中 queries[i] = [ni, ki] 。第 i 个查询 queries[i] 要求构造长度为 ni 、每个元素都是正整数的数组，且满足所有元素的乘积为 ki ，请你找出有多少种可行的方案。由于答案可能会很大，方案数需要对 109 + 7 取余 。
#
# 请你返回一个整数数组 answer，满足 answer.length == queries.length ，其中 answer[i]是第 i 个查询的结果。
#
#
#
# 示例 1：
#
# 输入：queries = [[2,6],[5,1],[73,660]]
# 输出：[4,1,50734910]
# 解释：每个查询之间彼此独立。
# [2,6]：总共有 4 种方案得到长度为 2 且乘积为 6 的数组：[1,6]，[2,3]，[3,2]，[6,1]。
# [5,1]：总共有 1 种方案得到长度为 5 且乘积为 1 的数组：[1,1,1,1,1]。
# [73,660]：总共有 1050734917 种方案得到长度为 73 且乘积为 660 的数组。1050734917 对 109 + 7 取余得到 50734910 。
# 示例 2 ：
#
# 输入：queries = [[1,1],[2,2],[3,3],[4,4],[5,5]]
# 输出：[1,2,3,10,5]
#
#
# 提示：
#
# 1 <= queries.length <= 104
# 1 <= ni, ki <= 104
import math

from leetcode.allcode.competition.mypackage import *

MX = 10 ** 4 + 1
# MX = 10 ** 1 + 1
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

primes = euler_all_primes(MX)
# print(len(primes))

factors = []  # factors[i][j] 表示i的质因子j的个数
factors.append(None)
factors.append(defaultdict(int))
# 以下处理是预处理所有质数的做法
# for x in range(2, MX):
#     factors.append(defaultdict(int))
#     for y in primes:
#         if y * y > x:
#             if x > 1:
#                 factors[-1][x] += 1  # 剩余的一个质数
#             break
#         while x % y == 0:
#             factors[-1][y] += 1
#             x //= y

# 这个做法不依赖与计算所有质数
for x in range(2, MX):
    factors.append(defaultdict(int))
    y = 2
    while y * y <= x:
        while x % y == 0:
            factors[-1][y] += 1
            x //= y
        y += 1
    if x > 1:
        factors[-1][x] += 1  # 剩余的一个质数
# print(factors)

class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7
        def calc(n, k):
            res = 1
            for p, num in factors[k].items():
                # num个相同的球，放入n个不同的盒子有多少种方法
                # num个球和k-1个隔板，
                res *= math.comb(num + n - 1, num)
                res %= MOD
            return res

        return [calc(a, b) for a, b in queries]

so = Solution()
print(so.waysToFillArray(queries = [[1,1],[2,2],[3,3],[4,4],[5,5]]))
print(so.waysToFillArray(queries = [[2,6],[5,1],[73,660]]))


