# 给你一个下标从 0 开始的整数数组 nums ，数组长度为 n 。
#
# 你可以执行无限次下述运算：
#
# 选择一个之前未选过的下标 i ，并选择一个 严格小于 nums[i] 的质数 p ，从 nums[i] 中减去 p 。
# 如果你能通过上述运算使得 nums 成为严格递增数组，则返回 true ；否则返回 false 。
#
# 严格递增数组 中的每个元素都严格大于其前面的元素。
#
#
#
# 示例 1：
#
# 输入：nums = [4,9,6,10]
# 输出：true
# 解释：
# 在第一次运算中：选择 i = 0 和 p = 3 ，然后从 nums[0] 减去 3 ，nums 变为 [1,9,6,10] 。
# 在第二次运算中：选择 i = 1 和 p = 7 ，然后从 nums[1] 减去 7 ，nums 变为 [1,2,6,10] 。
# 第二次运算后，nums 按严格递增顺序排序，因此答案为 true 。
# 示例 2：
#
# 输入：nums = [6,8,11,12]
# 输出：true
# 解释：nums 从一开始就按严格递增顺序排序，因此不需要执行任何运算。
# 示例 3：
#
# 输入：nums = [5,8,3]
# 输出：false
# 解释：可以证明，执行运算无法使 nums 按严格递增顺序排序，因此答案是 false 。
#
#
# 提示：
#
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 1000
# nums.length == n

from leetcode.allcode.competition.mypackage import *


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
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
        mx = max(nums)
        primes = all_primes(1200)
        print(primes)
        pre = 0
        for i, x in enumerate(nums):
            pos = bisect_left(primes, x - pre)
            if pos == 0:
                if x <= pre:
                    return False
                pre = x
            elif x - primes[pos - 1] > 0:
                pre = x - primes[pos - 1]
            else:
                return False
        return True


so = Solution()
print(so.primeSubOperation([2,2]))
print(so.primeSubOperation([5,8,3]))
print(so.primeSubOperation([998,2]))
print(so.primeSubOperation([6,8,11,12]))
print(so.primeSubOperation([4,9,6,10]))




