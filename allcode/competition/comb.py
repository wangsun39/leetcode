
from leetcode.allcode.competition.mypackage import *

# 第二类斯特林数

MOD = 1_000_000_007
MX = 1001

s = [[0] * MX for _ in range(MX)]
s[0][0] = 1
for i in range(1, MX):
    for j in range(1, i + 1):
        s[i][j] = (s[i - 1][j - 1] + j * s[i - 1][j]) % MOD




