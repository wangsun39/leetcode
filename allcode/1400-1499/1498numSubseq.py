# 给你一个整数数组 nums 和一个整数 target 。
#
# 请你统计并返回 nums 中能满足其最小元素与最大元素的 和 小于或等于 target 的 非空 子序列的数目。
#
# 由于答案可能很大，请将结果对 109 + 7 取余后返回。
#
#
#
# 示例 1：
#
# 输入：nums = [3,5,6,7], target = 9
# 输出：4
# 解释：有 4 个子序列满足该条件。
# [3] -> 最小元素 + 最大元素 <= target (3 + 3 <= 9)
# [3,5] -> (3 + 5 <= 9)
# [3,5,6] -> (3 + 6 <= 9)
# [3,6] -> (3 + 6 <= 9)
# 示例 2：
#
# 输入：nums = [3,3,6,8], target = 10
# 输出：6
# 解释：有 6 个子序列满足该条件。（nums 中可以有重复数字）
# [3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
# 示例 3：
#
# 输入：nums = [2,3,3,4,6,7], target = 12
# 输出：61
# 解释：共有 63 个非空子序列，其中 2 个不满足条件（[6,7], [7]）
# 有效序列总数为（63 - 2 = 61）
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 106
# 1 <= target <= 106


from bisect import *
from heapq import *
from collections import defaultdict
from functools import cache
from typing import List
# from math import *

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        ans = 0
        for i, x in enumerate(nums):
            if x * 2 <= target: ans += 1
            p = bisect_right(nums, target - x)
            p = min(p, i)
            if p <= 0: continue
            ans += (int(pow(2, p, MOD)) - 1) * (int(pow(2, i - p, MOD)))  # [0, p) 只少要取一个数，[p, i) 每个数都可以取或不取
            ans %= MOD
        return ans



so = Solution()
print(so.numSubseq(nums = [3,5,6,7], target = 9))
print(so.numSubseq(nums = [2,3,3,4,6,7], target = 12))
print(so.numSubseq(nums = [3,3,6,8], target = 10))




