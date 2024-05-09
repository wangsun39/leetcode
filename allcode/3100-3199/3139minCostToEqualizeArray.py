# 给你一个整数数组 nums 和两个整数 cost1 和 cost2 。你可以执行以下 任一 操作 任意 次：
#
# 从 nums 中选择下标 i 并且将 nums[i] 增加 1 ，开销为 cost1。
# 选择 nums 中两个 不同 下标 i 和 j ，并且将 nums[i] 和 nums[j] 都 增加 1 ，开销为 cost2 。
# 你的目标是使数组中所有元素都 相等 ，请你返回需要的 最小开销 之和。
#
# 由于答案可能会很大，请你将它对 109 + 7 取余 后返回。
#
#
#
# 示例 1：
#
# 输入：nums = [4,1], cost1 = 5, cost2 = 2
#
# 输出：15
#
# 解释：
#
# 执行以下操作可以使数组中所有元素相等：
#
# 将 nums[1] 增加 1 ，开销为 5 ，nums 变为 [4,2] 。
# 将 nums[1] 增加 1 ，开销为 5 ，nums 变为 [4,3] 。
# 将 nums[1] 增加 1 ，开销为 5 ，nums 变为 [4,4] 。
# 总开销为 15 。
#
# 示例 2：
#
# 输入：nums = [2,3,3,3,5], cost1 = 2, cost2 = 1
#
# 输出：6
#
# 解释：
#
# 执行以下操作可以使数组中所有元素相等：
#
# 将 nums[0] 和 nums[1] 同时增加 1 ，开销为 1 ，nums 变为 [3,4,3,3,5] 。
# 将 nums[0] 和 nums[2] 同时增加 1 ，开销为 1 ，nums 变为 [4,4,4,3,5] 。
# 将 nums[0] 和 nums[3] 同时增加 1 ，开销为 1 ，nums 变为 [5,4,4,4,5] 。
# 将 nums[1] 和 nums[2] 同时增加 1 ，开销为 1 ，nums 变为 [5,5,5,4,5] 。
# 将 nums[3] 增加 1 ，开销为 2 ，nums 变为 [5,5,5,5,5] 。
# 总开销为 6 。
#
# 示例 3：
#
# 输入：nums = [3,5,3], cost1 = 1, cost2 = 3
#
# 输出：4
#
# 解释：
#
# 执行以下操作可以使数组中所有元素相等：
#
# 将 nums[0] 增加 1 ，开销为 1 ，nums 变为 [4,5,3] 。
# 将 nums[0] 增加 1 ，开销为 1 ，nums 变为 [5,5,3] 。
# 将 nums[2] 增加 1 ，开销为 1 ，nums 变为 [5,5,4] 。
# 将 nums[2] 增加 1 ，开销为 1 ，nums 变为 [5,5,5] 。
# 总开销为 4 。
#
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 106
# 1 <= cost1 <= 106
# 1 <= cost2 <= 106

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        if n == 1: return 0
        if n == 2:
            return abs(nums[0] - nums[1]) * cost1 % MOD
        mx, mn = max(nums), min(nums)
        if cost1 * 2 <= cost2:
            ans = 0
            for x in nums:
                ans += (mx - x) * cost1
                ans %= MOD
            return ans
        ans = inf
        diff = sum(mx - x for x in nums) - (mx - mn) # 把所有x都变成mx需要增加多少（除了mn不动）
        for up in range(mx, mx * 2 + 1):
            # 枚举操作完之后的结果是up时，计算最小的开销是多少
            # 尽可能多的使用操作2
            x1 = up - mn   # 最小值到up的距离
            x2 = diff + (up - mx) * (n - 1)  # 除了一个最小值其他元素与up的距离和
            if x1 <= x2:  # 能找到一种方式都用操作2，把这些元素处理掉，最多剩一个
                if (x1 + x2) & 1:
                    v = cost1 + cost2 * ((x1 + x2) // 2)
                else:
                    v = cost2 * (x1 + x2) // 2
            else:  # 用最小值把其他元素都用操作2，提升到mx
                v = cost2 * x2 + cost1 * (x1 - x2)
            if v < ans:
                ans = v
        return ans % MOD



so = Solution()
print(so.minCostToEqualizeArray([5,5,7,8],7,5))  # 22
print(so.minCostToEqualizeArray([4,3,1,8],5,1))
print(so.minCostToEqualizeArray([1,1000000], 1000000, 1))
print(so.minCostToEqualizeArray([60,19,53,31,57], 60, 2))
print(so.minCostToEqualizeArray([1,14,14,15],2,1))
print(so.minCostToEqualizeArray(nums = [2,3,3,3,5], cost1 = 2, cost2 = 1))
print(so.minCostToEqualizeArray(nums = [3,5,3], cost1 = 1, cost2 = 3))
print(so.minCostToEqualizeArray(nums = [4,1], cost1 = 5, cost2 = 2))   # 15




