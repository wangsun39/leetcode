# 给你一个整数数组 nums 和一个目标值 goal 。
#
# 你需要从 nums 中选出一个子序列，使子序列元素总和最接近 goal 。也就是说，如果子序列元素和为 sum ，你需要 最小化绝对差 abs(sum - goal) 。
#
# 返回 abs(sum - goal) 可能的 最小值 。
#
# 注意，数组的子序列是通过移除原始数组中的某些元素（可能全部或无）而形成的数组。
#
#
#
# 示例 1：
#
# 输入：nums = [5,-7,3,5], goal = 6
# 输出：0
# 解释：选择整个数组作为选出的子序列，元素和为 6 。
# 子序列和与目标值相等，所以绝对差为 0 。
# 示例 2：
#
# 输入：nums = [7,-9,15,-2], goal = -5
# 输出：1
# 解释：选出子序列 [7,-9,-2] ，元素和为 -4 。
# 绝对差为 abs(-4 - (-5)) = abs(1) = 1 ，是可能的最小值。
# 示例 3：
#
# 输入：nums = [1,2,3], goal = -7
# 输出：7
#
#
# 提示：
#
# 1 <= nums.length <= 40
# -107 <= nums[i] <= 107
# -109 <= goal <= 109

from leetcode.allcode.competition.mypackage import *


class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        if n == 1:
            return min(abs(goal - nums[0]), abs(goal))
        nums1, nums2 = nums[:n//2], nums[n//2:]

        def calc(arr):
            m = len(arr)
            ss = set()
            for i in range(1 << m):
                s = 0
                for j in range(m):
                    if i & (1 << j):
                        s += arr[j]
                ss.add(s)
            return ss

        s1, s2 = calc(nums1), calc(nums2)
        arr1 = sorted(list(s1))
        arr2 = sorted(list(s2))
        ans = inf
        idx = len(arr2) - 1
        for x in arr1:
            while idx >= 0:
                if x + arr2[idx] == goal:
                    return 0
                v = abs(x + arr2[idx] - goal)
                if ans > v: ans = v
                if x + arr2[idx] < goal:
                    break
                idx -= 1
            if idx < 0:
                break

        return ans



so = Solution()

print(so.minAbsDifference(nums = [5,-7,3,5], goal = 6))  # 0




