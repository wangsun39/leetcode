# 给你一个非负整数数组 nums 和一个整数 k 。每次操作，你可以选择 nums 中 任一 元素并将它 增加 1 。
#
# 请你返回 至多 k 次操作后，能得到的 nums的 最大乘积 。由于答案可能很大，请你将答案对 109 + 7 取余后返回。
#
#
#
# 示例 1：
#
# 输入：nums = [0,4], k = 5
# 输出：20
# 解释：将第一个数增加 5 次。
# 得到 nums = [5, 4] ，乘积为 5 * 4 = 20 。
# 可以证明 20 是能得到的最大乘积，所以我们返回 20 。
# 存在其他增加 nums 的方法，也能得到最大乘积。
# 示例 2：
#
# 输入：nums = [6,3,3,2], k = 2
# 输出：216
# 解释：将第二个数增加 1 次，将第四个数增加 1 次。
# 得到 nums = [6, 4, 3, 3] ，乘积为 6 * 4 * 3 * 3 = 216 。
# 可以证明 216 是能得到的最大乘积，所以我们返回 216 。
# 存在其他增加 nums 的方法，也能得到最大乘积。
#
#
# 提示：
#
# 1 <= nums.length, k <= 105
# 0 <= nums[i] <= 106

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        n = len(nums)
        s = 0
        for i, x in enumerate(nums):
            if i < n - 1:
                if s + (nums[i + 1] - x) * (i + 1) >= k:
                    h, r = divmod(k - s, i + 1)
                    for j in range(r):
                        nums[j] = x + h + 1
                    for j in range(r, i + 1):
                        nums[j] = x + h
                    break
                s += (nums[i + 1] - x) * (i + 1)
            else:
                mx = nums[-1]
                k -= sum(mx - x for x in nums)
                h, r = divmod(k, n)
                for j in range(r):
                    nums[j] = mx + h + 1
                for j in range(r, i + 1):
                    nums[j] = mx + h
        ans = 1
        for x in nums:
            ans *= x
            ans %= MOD
        return ans

so = Solution()
print(so.maximumProduct(nums = [0,4], k = 5))

