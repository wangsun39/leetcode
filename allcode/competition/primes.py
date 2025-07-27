# https://leetcode.cn/circle/discuss/mDfnkW/

from leetcode.allcode.competition.mypackage import *

# 计算所有 <= n 的质数

# 埃氏筛
def all_primes(n):
    is_prime = [False, False] + [True] * (n - 1)
    primes = []
    flg = False
    for i in range(2, n + 1):
        if not is_prime[i]: continue
        primes.append(i)
        if flg:
            continue
        if i * i > n:
            flg = True
            continue
        j = i * i
        while j < n + 1:
            is_prime[j] = False
            j += i
    return primes

# 欧拉筛
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

MX = 10 ** 5 + 1
is_prime = [True] * MX
is_prime[1] = False
for i in range(2, isqrt(MX) + 1):
    if is_prime[i]:
        for j in range(i * i, MX, i):
            is_prime[j] = False


def is_prime(n: int) -> bool:
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return n >= 2  # 1 不是质数

print(euler_all_primes(100))

# 质因数分解
MX = 10 ** 5 + 1
omega = [0] * MX  # omega[i]  表示i的质因子个数
for i in range(2, MX):  # 预处理 omega
    if omega[i] == 0:  # i 是质数
        for j in range(i, MX, i):
            omega[j] += 1  # i 是 j 的一个质因子
# print(omega)

# MX = 1000000  # 可以用于10^5个最多10^6的数
min_factor = [1] * (MX + 1)  # 记录每个数x的最小质因子 min_factor[x]，对于质数x来说，最小质因子就是x
p = 2
min_factor[2] = 2
# O(M loglog M)
while p <= MX:
    i = p
    while i * p <= MX:
        if min_factor[i * p] == 1:
            min_factor[i * p] = p
        i += 1

    p += 1
    while p <= MX:
        if min_factor[p] == 1:
            min_factor[p] = p
            break
        p += 1


# MX = 100001
divisors = [[] for _ in range(MX)]  # divisors[i] 表示 i 的所有因子
for i in range(1, MX):  # 预处理每个数的所有因子，时间复杂度 O(MlogM)，M=1e5
    for j in range(i, MX, i):
        divisors[j].append(i)

MX = 10 ** 5 + 1
# MX = 10
omega = [[] for _ in range(MX)]  # omega[i]  表示i的所有质因子
for i in range(2, MX):  # 预处理 omega
    if len(omega[i]) == 0:  # i 是质数
        for j in range(i, MX, i):
            omega[j].append(i)  # i 是 j 的一个质因子

# 因子分解
def factors(x):
    res = []
    i = 1
    while i * i <= x:
        if x % i == 0:
            res.append(i)
            if i * i != x:
                res.append(x // i)
        i += 1
    return res

print(factors(12))

#质因子分解
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

print(prime_factors(12))

factors = []  # factors[i][j] 表示i的质因子j的个数
factors.append(None)
factors.append(defaultdict(int))

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

# 预处理每个数的质因子列表
mx = 1000001
PRIME_FACTORS = [[] for _ in range(mx)]
for i in range(2, mx):
    if not PRIME_FACTORS[i]:  # i 是质数
        for j in range(i, mx, i):  # i 的倍数有质因子 i
            PRIME_FACTORS[j].append(i)


# MOD = 1_000_000_007
#
# // 加
# (a + b) % MOD
#
# // 减
# (a - b + MOD) % MOD
#
# // 乘
# a * b % MOD
#
# // 多个数相乘，要步步取模，防止溢出
# a * b % MOD * c % MOD
#
# // 除（MOD 是质数且 b 不是 MOD 的倍数）
# a * qpow(b, MOD - 2, MOD) % MOD
# 其中 qpow 为快速幂。
#
# 注：Python 内置快速幂函数 pow(x, y, m) 用于计算
# 特别地，除法也可以写成 a * pow(b, -1, MOD) % MOD。


