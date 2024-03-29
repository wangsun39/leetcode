# 给你一个下标从 0 开始的数组 nums ，它包含 非负 整数，且全部为 2 的幂，同时给你一个整数 target 。
#
# 一次操作中，你必须对数组做以下修改：
#
# 选择数组中一个元素 nums[i] ，满足 nums[i] > 1 。
# 将 nums[i] 从数组中删除。
# 在 nums 的 末尾 添加 两个 数，值都为 nums[i] / 2 。
# 你的目标是让 nums 的一个 子序列 的元素和等于 target ，请你返回达成这一目标的 最少操作次数 。如果无法得到这样的子序列，请你返回 -1 。
#
# 数组中一个 子序列 是通过删除原数组中一些元素，并且不改变剩余元素顺序得到的剩余数组。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,8], target = 7
# 输出：1
# 解释：第一次操作中，我们选择元素 nums[2] 。数组变为 nums = [1,2,4,4] 。
# 这时候，nums 包含子序列 [1,2,4] ，和为 7 。
# 无法通过更少的操作得到和为 7 的子序列。
# 示例 2：
#
# 输入：nums = [1,32,1,2], target = 12
# 输出：2
# 解释：第一次操作中，我们选择元素 nums[1] 。数组变为 nums = [1,1,2,16,16] 。
# 第二次操作中，我们选择元素 nums[3] 。数组变为 nums = [1,1,2,16,8,8] 。
# 这时候，nums 包含子序列 [1,1,2,8] ，和为 12 。
# 无法通过更少的操作得到和为 12 的子序列。
# 示例 3：
#
# 输入：nums = [1,32,1], target = 35
# 输出：-1
# 解释：无法得到和为 35 的子序列。
#
#
# 提示：
#
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 230
# nums 只包含非负整数，且均为 2 的幂。
# 1 <= target < 231

from leetcode.allcode.competition.mypackage import *
import math
class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        t = []
        while target:
            if target & 1:
                t.append(1)
            else:
                t.append(0)
            target >>= 1
        nums = [int(math.log(x, 2)) for x in nums]
        heapify(nums)
        spop = set()  # 被pop出去的元素集合
        # print(nums, t)

        ans = 0
        for i, x in enumerate(t):
            if x == 0: continue
            while nums and nums[0] < i:
                y = nums[0]
                heappop(nums)
                while y in spop:   # 在pop出去的元素中凑一个更大的2的幂次
                    spop.remove(y)
                    y += 1
                if y >= i:
                    heappush(nums, y)
                else:
                    spop.add(y)
            while nums and nums[0] > i:
                y = nums[0]
                heappop(nums)
                y -= 1
                ans += 1
                heappush(nums, y)
                heappush(nums, y)
            if len(nums) == 0:
                return -1
            heappop(nums)
        return ans





so = Solution()
print(so.minOperations(nums = [1,32,1,2], target = 12))
print(so.minOperations(nums = [1,2,8], target = 7))
print(so.minOperations(nums = [1,32,1], target = 35))




