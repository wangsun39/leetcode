# 给你一个整数数组 nums。
#
# 根据以下规则将 nums 分割成两个数组 A 和 B：
#
# nums 中位于 质数 下标的元素必须放入数组 A。
# 所有其他元素必须放入数组 B。
# 返回两个数组和的 绝对 差值：|sum(A) - sum(B)|。
#
# 质数 是一个大于 1 的自然数，它只有两个因子，1和它本身。
#
# 注意：空数组的和为 0。
#
#
#
# 示例 1:
#
# 输入: nums = [2,3,4]
#
# 输出: 1
#
# 解释:
#
# 数组中唯一的质数下标是 2，所以 nums[2] = 4 被放入数组 A。
# 其余元素 nums[0] = 2 和 nums[1] = 3 被放入数组 B。
# sum(A) = 4，sum(B) = 2 + 3 = 5。
# 绝对差值是 |4 - 5| = 1。
# 示例 2:
#
# 输入: nums = [-1,5,7,0]
#
# 输出: 3
#
# 解释:
#
# 数组中的质数下标是 2 和 3，所以 nums[2] = 7 和 nums[3] = 0 被放入数组 A。
# 其余元素 nums[0] = -1 和 nums[1] = 5 被放入数组 B。
# sum(A) = 7 + 0 = 7，sum(B) = -1 + 5 = 4。
# 绝对差值是 |7 - 4| = 3。
#
#
# 提示:
#
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

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

is_prime = euler_all_primes(100000)

class Solution:
    def splitArray(self, nums: List[int]) -> int:

        s = sum(nums)
        s1 = sum(x for i, x in enumerate(nums) if is_prime[i])
        return abs(s - s1 * 2)




so = Solution()
print(so.splitArray([-1,5,7,0]))


