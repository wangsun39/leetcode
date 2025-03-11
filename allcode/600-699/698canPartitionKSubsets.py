# 给定一个整数数组nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
#
#
#
# 示例 1：
#
# 输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# 输出： True
# 说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
# 示例 2:
#
# 输入: nums = [1,2,3,4], k = 3
# 输出: false
#
#
# 提示：
#
# 1 <= k <= len(nums) <= 16
# 0 < nums[i] < 10000
# 每个元素的频率在 [1,4] 范围内

from leetcode.allcode.competition.mypackage import *

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % k: return False
        avg = total // k
        nums.sort()
        if nums[-1] > avg: return False

        @lru_cache(None)
        def find(bits, cur):
            if bits == 0: return True
            # k = 1
            for i in range(n):
                if cur + nums[i] > avg:
                    break
                if bits & (1 << i):
                    if find(bits ^ (1 << i), (cur + nums[i]) % avg):
                        return True
            return False
        return find((1 << n) - 1, 0)




so = Solution()
print(so.canPartitionKSubsets(nums = [4, 3, 2, 3, 5, 2, 1], k = 4))
