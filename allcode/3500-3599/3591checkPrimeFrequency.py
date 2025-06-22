# 给你一个整数数组 nums。
#
# 如果数组中任一元素的 频次 是 质数，返回 true；否则，返回 false。
#
# 元素 x 的 频次 是它在数组中出现的次数。
#
# 质数是一个大于 1 的自然数，并且只有两个因数：1 和它本身。
#
#
#
# 示例 1：
#
# 输入： nums = [1,2,3,4,5,4]
#
# 输出： true
#
# 解释：
#
# 数字 4 的频次是 2，而 2 是质数。
#
# 示例 2：
#
# 输入： nums = [1,2,3,4,5]
#
# 输出： false
#
# 解释：
#
# 所有元素的频次都是 1。
#
# 示例 3：
#
# 输入： nums = [2,2,2,4,4]
#
# 输出： true
#
# 解释：
#
# 数字 2 和 4 的频次都是质数。
#
#
#
# 提示：
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100

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

    return is_prime

primes = euler_all_primes(1000)

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        return any(primes[v] for k, v in counter.items())


so = Solution()
print(so.checkPrimeFrequency([1,2,3,4,5]))
print(so.checkPrimeFrequency([1,2,3,4,5,4]))




