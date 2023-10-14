# 给你一个下标从 0 开始的整数数组 nums 和一个正整数 k 。
#
# 你可以对数组执行下述操作 任意次 ：
#
# 从数组中选出长度为 k 的 任一 子数组，并将子数组中每个元素都 减去 1 。
# 如果你可以使数组中的所有元素都等于 0 ，返回  true ；否则，返回 false 。
#
# 子数组 是数组中的一个非空连续元素序列。
#
#
#
# 示例 1：
#
# 输入：nums = [2,2,3,1,1,0], k = 3
# 输出：true
# 解释：可以执行下述操作：
# - 选出子数组 [2,2,3] ，执行操作后，数组变为 nums = [1,1,2,1,1,0] 。
# - 选出子数组 [2,1,1] ，执行操作后，数组变为 nums = [1,1,1,0,0,0] 。
# - 选出子数组 [1,1,1] ，执行操作后，数组变为 nums = [0,0,0,0,0,0] 。
# 示例 2：
#
# 输入：nums = [1,3,1,1], k = 2
# 输出：false
# 解释：无法使数组中的所有元素等于 0 。
#
#
# 提示：
#
# 1 <= k <= nums.length <= 105
# 0 <= nums[i] <= 106

from leetcode.allcode.competition.mypackage import *

class Solution:
    def checkArray1(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        diff = [0] * n
        acc = 0
        for i, x in enumerate(nums):
            if i - k >= 0:
                acc -= diff[i - k]
            cur = x - acc
            if cur < 0:
                return False
            if cur > 0:
                if i + k > n:
                    return False
                acc += cur
                diff[i] = cur
        return True

    def checkArray(self, nums: List[int], k: int) -> bool:
        # 2023/9/21 差分数组
        n = len(nums)
        diff = [0] * n
        diff[0] = nums[0]
        for i in range(n - 1):
            diff[i + 1] = nums[i + 1] - nums[i]
        cur = 0
        for i in range(n):
            cur += diff[i]
            if cur < 0: return False
            if i + k > n:
                if cur != 0: return False
                continue
            if i + k < n:
                diff[i + k] += cur
            cur = 0
        return True



so = Solution()
print(so.checkArray([60,72,87,89,63,52,64,62,31,37,57,83,98,94,92,77,94,91,87,100,91,91,50,26], 4))
print(so.checkArray(nums = [2,2,3,1,1,0], k = 3))
print(so.checkArray(nums = [1,3,1,1], k = 2))




