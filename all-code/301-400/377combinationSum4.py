# 给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。
#
# 题目数据保证答案符合 32 位整数范围。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,2,3], target = 4
# 输出：7
# 解释：
# 所有可能的组合为：
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# 请注意，顺序不同的序列被视作不同的组合。
# 示例 2：
#
# 输入：nums = [9], target = 3
# 输出：0
#  
#
# 提示：
#
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 1000
# nums 中的所有元素 互不相同
# 1 <= target <= 1000



from typing import List
from functools import lru_cache

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()

        @lru_cache(None)
        def helper(target):
            if nums[0] >= target:
                return 1 if target == nums[0] else 0
            ret = 0
            for n in nums:
                if n > target:
                    return ret
                elif n == target:
                    return ret + 1
                ret += helper(target - n)
            return ret

        return helper(target)



so = Solution()
print(so.combinationSum4(nums = [1,2,3], target = 4))
print(so.combinationSum4(nums = [9], target = 3))

