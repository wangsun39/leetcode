from leetcode.allcode.competition.mypackage import *

# 编写一段程序来查找第 n 个超级丑数。
#
# 超级丑数是指其所有质因数都是长度为k的质数列表primes中的正整数。
#
# 示例:
#
# 输入: n = 12, primes = [2,7,13,19]
# 输出: 32
# 解释: 给定长度为 4 的质数列表 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。
# 说明:
#
# 1是任何给定primes的超级丑数。
# 给定primes中的数字以升序排列。
# 0 < k ≤ 100, 0 < n ≤ 10^6, 0 < primes[i] < 1000 。
# 第n个超级丑数确保在 32 位有符整数范围内。

import time
class Solution:

    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        seq = [1]
        N = len(primes)
        primeList = [[primes[i], 0] for i in range(N)]

        while len(seq) < n:
            curIdx, curVal = 0, primeList[0][0] * seq[primeList[0][1]]
            for i in range(1, N):
                pair = primeList[i]
                if pair[0] * seq[pair[1]] < curVal:
                    curIdx, curVal = i, pair[0] * seq[pair[1]]
            if curVal > seq[-1]:
                seq.append(curVal)
            primeList[curIdx][1] += 1
        return seq[-1]


so = Solution()
print(so.nthSuperUglyNumber(800,
[37,43,59,61,67,71,79,83,89,97,101,103,113,127,131,157,163,167,173,179,191,193,197,199,211,229,233,239,251,257]))
print(so.nthSuperUglyNumber(85, [5,7,11,13,17,19,29,43,47,53]))
#print(so.nthSuperUglyNumber(12, [2,7,13,19]))

