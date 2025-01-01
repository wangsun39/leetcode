# https://leetcode.cn/circle/discuss/mDfnkW/

from leetcode.allcode.competition.mypackage import *

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

# 组合数计算
def comb(n: int, m: int) -> int:
    return f[n] * inv_f[m] * inv_f[n - m] % MOD

# (a // b) % MOD == a * qpow(b, MOD - 2, MOD) % MOD


