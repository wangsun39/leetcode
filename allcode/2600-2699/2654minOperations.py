# 给你一个下标从 0 开始的 正 整数数组 nums 。你可以对数组执行以下操作 任意 次：
#
# 选择一个满足 0 <= i < n - 1 的下标 i ，将 nums[i] 或者 nums[i+1] 两者之一替换成它们的最大公约数。
# 请你返回使数组 nums 中所有元素都等于 1 的 最少 操作次数。如果无法让数组全部变成 1 ，请你返回 -1 。
#
# 两个正整数的最大公约数指的是能整除这两个数的最大正整数。
#
#
#
# 示例 1：
#
# 输入：nums = [2,6,3,4]
# 输出：4
# 解释：我们可以执行以下操作：
# - 选择下标 i = 2 ，将 nums[2] 替换为 gcd(3,4) = 1 ，得到 nums = [2,6,1,4] 。
# - 选择下标 i = 1 ，将 nums[1] 替换为 gcd(6,1) = 1 ，得到 nums = [2,1,1,4] 。
# - 选择下标 i = 0 ，将 nums[0] 替换为 gcd(2,1) = 1 ，得到 nums = [1,1,1,4] 。
# - 选择下标 i = 2 ，将 nums[3] 替换为 gcd(1,4) = 1 ，得到 nums = [1,1,1,1] 。
# 示例 2：
#
# 输入：nums = [2,10,6,14]
# 输出：-1
# 解释：无法将所有元素都变成 1 。
#
#
# 提示：
#
# 2 <= nums.length <= 50
# 1 <= nums[i] <= 106
from math import gcd

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if min(nums) == 1:
            return sum(1 for x in nums if x != 1)
        ans = inf
        for i in range(n):
            j = i
            cur = nums[i]
            while j < n:
                cur = gcd(cur, nums[j])
                if cur == 1:
                    break
                j += 1
            if cur == 1:
                ans = min(ans, j - i + n - 1)
        return ans if ans < inf else -1


so = Solution()
print(so.minOperations([1,1]))
print(so.minOperations([2,6,3,4]))   # 4
print(so.minOperations([2,10,6,14]))




