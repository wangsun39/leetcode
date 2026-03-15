# 给你两个正整数 left 和 right ，请你找到两个整数 num1 和 num2 ，它们满足：
#
# left <= nums1 < nums2 <= right  。
# nums1 和 nums2 都是 质数 。
# nums2 - nums1 是满足上述条件的质数对中的 最小值 。
# 请你返回正整数数组 ans = [nums1, nums2] 。如果有多个整数对满足上述条件，请你返回 nums1 最小的质数对。如果不存在符合题意的质数对，请你返回 [-1, -1] 。
#
# 如果一个整数大于 1 ，且只能被 1 和它自己整除，那么它是一个质数。
#
#
#
# 示例 1：
#
# 输入：left = 10, right = 19
# 输出：[11,13]
# 解释：10 到 19 之间的质数为 11 ，13 ，17 和 19 。
# 质数对的最小差值是 2 ，[11,13] 和 [17,19] 都可以得到最小差值。
# 由于 11 比 17 小，我们返回第一个质数对。
# 示例 2：
#
# 输入：left = 4, right = 6
# 输出：[-1,-1]
# 解释：给定范围内只有一个质数，所以题目条件无法被满足。
#
#
# 提示：
#
# 1 <= left <= right <= 106

from leetcode.allcode.competition.mypackage import *

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = []
        def all_prime(mi, mx):  # 获取[mi, mx) 内所有质数
            if mx < 2:
                return 0
            isPrime = [1] * mx
            isPrime[0] = isPrime[1] = 0
            for i in range(2, int(mx ** 0.5) + 1):
                if isPrime[i]:
                    isPrime[i * i:mx:i] = [0] * ((mx - 1 - i * i) // i + 1)
            for i in range(mi, mx):
                if isPrime[i]:
                    primes.append(i)
        all_prime(left, right + 1)
        mi = inf
        ans = [-1, -1]
        for i in range(len(primes)):
            if i == len(primes) -1 or primes[i + 1] > right:
                break
            if left <= primes[i] < primes[i + 1] <= right:
                if primes[i + 1] - primes[i] < mi:
                    mi = primes[i + 1] - primes[i]
                    ans = [primes[i], primes[i + 1]]
        return ans


so = Solution()
print(so.closestPrimes(left = 10, right = 19))
print(so.closestPrimes(left = 4, right = 6))


