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
