# 给你一个整数数组 nums ，一个整数 k  和一个整数 multiplier 。
#
# 你需要对 nums 执行 k 次操作，每次操作中：
#
# 找到 nums 中的 最小 值 x ，如果存在多个最小值，选择最 前面 的一个。
# 将 x 替换为 x * multiplier 。
# k 次操作以后，你需要将 nums 中每一个数值对 109 + 7 取余。
#
# 请你返回执行完 k 次乘运算以及取余运算之后，最终的 nums 数组。
#
#
#
# 示例 1：
#
# 输入：nums = [2,1,3,5,6], k = 5, multiplier = 2
#
# 输出：[8,4,6,5,6]
#
# 解释：
#
# 操作	结果
# 1 次操作后	[2, 2, 3, 5, 6]
# 2 次操作后	[4, 2, 3, 5, 6]
# 3 次操作后	[4, 4, 3, 5, 6]
# 4 次操作后	[4, 4, 6, 5, 6]
# 5 次操作后	[8, 4, 6, 5, 6]
# 取余操作后	[8, 4, 6, 5, 6]
# 示例 2：
#
# 输入：nums = [100000,2000], k = 2, multiplier = 1000000
#
# 输出：[999999307,999999993]
#
# 解释：
#
# 操作	结果
# 1 次操作后	[100000, 2000000000]
# 2 次操作后	[100000000000, 2000000000]
# 取余操作后	[999999307, 999999993]
#
#
# 提示：
#
# 1 <= nums.length <= 104
# 1 <= nums[i] <= 109
# 1 <= k <= 109
# 1 <= multiplier <= 106

from leetcode.allcode.competition.mypackage import *

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        MOD = 10 ** 9 + 7
        n = len(nums)
        hp = [[x, i] for i, x in enumerate(nums)]
        mxi = max(hp)[1]
        heapify(hp)
        while k > 0:
            x, i = heappop(hp)
            heappush(hp, [x * multiplier, i])
            k -= 1
            if i == mxi:
                break
        q, r = divmod(k, n)

        ans = [0] * n
        while hp:
            x, i = heappop(hp)
            if r:
                ans[i] = x * pow(multiplier, q + 1, MOD) % MOD
                r -= 1
            else:
                ans[i] = x * pow(multiplier, q, MOD) % MOD
        return ans



so = Solution()
print(so.getFinalState(nums = [1,2], k = 3, multiplier = 4))  # [16, 8]
print(so.getFinalState(nums = [2,1,3,5,6], k = 5, multiplier = 2))  # [8,4,6,5,6]
print(so.getFinalState(nums = [100000,2000], k = 2, multiplier = 1000000))  # [999999307,999999993]




