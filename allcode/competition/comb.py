
from leetcode.allcode.competition.mypackage import *

# 第二类斯特林数

MOD = 1_000_000_007
MX = 1001

s = [[0] * MX for _ in range(MX)]
s[0][0] = 1
for i in range(1, MX):
    for j in range(1, i + 1):
        s[i][j] = (s[i - 1][j - 1] + j * s[i - 1][j]) % MOD



# 杨辉三角
# https://leetcode.cn/problems/pascals-triangle-ii/solutions/601082/yang-hui-san-jiao-ii-by-leetcode-solutio-shuk
# (a+b) ^ n 的展开式（二项式展开）中的各项系数依次对应杨辉三角的第 n 行中的每一项。
# C(n, m) = C(n, m - 1) * (n - m + 1) // m


# 当组合数超过k时，退出
def comb(n: int, m: int) -> int:
    m = min(m, n - m)
    res = 1
    for i in range(1, m + 1):
        res = res * (n + 1 - i) // i
        if res >= k:  # 太大了
            return k
    return res


# 带模的组合数
MOD = 1_000_000_007
MX = 100_000

f = [0] * MX  # f[i] = i!
f[0] = 1
for i in range(1, MX):
    f[i] = f[i - 1] * i % MOD

inv_f = [0] * MX  # inv_f[i] = i!^-1
inv_f[-1] = pow(f[-1], -1, MOD)
for i in range(MX - 1, 0, -1):
    inv_f[i - 1] = inv_f[i] * i % MOD

def comb(n: int, m: int) -> int:
    return f[n] * inv_f[m] * inv_f[n - m] % MOD

