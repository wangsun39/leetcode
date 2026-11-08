# 给你两个整数 n 和 s。
#
# 考虑所有小于等于 n 的 质数 。从这些质数中选择一个 子集 ，并满足以下条件：
#
# 每个质数 最多只能选择一次。
# 在所选质数的 总和 不超过 s 的前提下，使总和 尽可能大。
# 在总和达到 最大值 的所有子集中，选择包含质数数量 最少 的子集。
# 如果仍有多个子集满足条件，则将各子集中的元素按递增顺序排列，并选择 字典序最小 的数组。
# 返回一个包含所选质数的整数数组，并按 递增 顺序排列。如果不存在合法的 非空 子集，则返回空数组。
#
# 质数 是大于 1 且只有 1 和它本身两个因数的自然数。
#
# 子集 是从一个集合中选择零个或多个不同元素得到的集合。
#
# 如果数组 a 和数组 b 在第一个不同的位置上，a 中的元素更小，则称 a 的 字典序更小。如果在较短数组的长度范围内所有元素都相同，则较短的数组字典序更小。
#
#
#
# 示例 1：
#
# 输入： n = 7, s = 20
#
# 输出： [2, 3, 5, 7]
#
# 解释：
#
# 小于等于 n = 7 的质数为 2、3、5 和 7。
# 这些质数的总和为 2 + 3 + 5 + 7 = 17，小于等于 s = 20。
# 因此，答案为 [2, 3, 5, 7]。
# 示例 2：
#
# 输入： n = 15, s = 18
#
# 输出： [5,13]
#
# 解释：
#
# 小于等于 15 的质数为 2、3、5、7、11 和 13。
# 总和为 18 的子集包括 [5, 13]、[7, 11]、[2, 3, 13] 和 [2, 5, 11]。由于该总和恰好等于 s，因此 18 是可能达到的最大总和。
# 在这些子集中，[5, 13] 和 [7, 11] 包含的质数最少，均为两个。
# 在这两个子集中，[5, 13] 的字典序更小，因为它的第一个元素 5 小于 7。因此，答案为 [5, 13]。
# 示例 3：
#
# 输入： n = 5, s = 1
#
# 输出： []
#
# 解释：
#
# 最小的质数是 2，大于 s = 1。
# 因此，无法选择任何质数，答案为空数组。
#
#
# 提示：
#
# 1 <= n <= 1000
# 1 <= s <= 1000

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

primes = euler_all_primes(1001)
np = len(primes)

class Solution:
    def maxPrimeSubset(self, n: int, s: int) -> list[int]:
        if s < 2 or n < 2:
            return []
        m = bisect_right(primes, n)
        dp = [[inf] * m for _ in range(s + 1)]  # dp[i][j]  从第j个数开始向后，能凑出和为i的取最少元素个数
        pre = [[inf] * m for _ in range(s + 1)]  # 转移方向，
        for j in range(m):
            dp[0][j] = 0
        for i in range(2, s + 1):
            if i == primes[m - 1]:
                dp[i][m - 1] = 1
                pre[i][m - 1] = 0
            for j in range(m - 2, -1, -1):
                dp[i][j] = dp[i][j + 1]
                if dp[i][j] < inf:
                    pre[i][j] = i
                t = i - primes[j]
                if t >= 0 and dp[i][j] >= dp[t][j + 1] + 1:  # 第二个等号保证字典序最小
                    dp[i][j] = dp[t][j + 1] + 1
                    pre[i][j] = t

        ans = []
        for i in range(s, -1, -1):
            if dp[i][0] < inf:
                # 最大和为i，下面要推出字典序最小的一个组合
                ss = i
                for j in range(m):
                    if pre[ss][j] != ss:
                        ans.append(primes[j])
                        ss = pre[ss][j]
                    # p = pre[ss][j]
                    if ss == 0:
                        break
                break

        # print(dp)
        return ans





so = Solution()
print(so.maxPrimeSubset(n = 15, s = 18))
print(so.maxPrimeSubset(n = 7, s = 1))
print(so.maxPrimeSubset(n = 7, s = 20))



