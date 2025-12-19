# 给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit。
#
#
#
# 示例 1：
#
# 输入：nums = [8,2,4,7], limit = 4
# 输出：2
# 解释：所有子数组如下：
# [8] 最大绝对差 |8-8| = 0 <= 4.
# [8,2] 最大绝对差 |8-2| = 6 > 4.
# [8,2,4] 最大绝对差 |8-2| = 6 > 4.
# [8,2,4,7] 最大绝对差 |8-2| = 6 > 4.
# [2] 最大绝对差 |2-2| = 0 <= 4.
# [2,4] 最大绝对差 |2-4| = 2 <= 4.
# [2,4,7] 最大绝对差 |2-7| = 5 > 4.
# [4] 最大绝对差 |4-4| = 0 <= 4.
# [4,7] 最大绝对差 |4-7| = 3 <= 4.
# [7] 最大绝对差 |7-7| = 0 <= 4.
# 因此，满足题意的最长子数组的长度为 2 。
# 示例 2：
#
# 输入：nums = [10,1,2,4,7,2], limit = 5
# 输出：4
# 解释：满足题意的最长子数组是 [2,4,7,2]，其最大绝对差 |2-7| = 5 <= 5 。
# 示例 3：
#
# 输入：nums = [4,2,2,2,4,4,2,2], limit = 0
# 输出：3
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 0 <= limit <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans = 0
        n = len(nums)
        st1 = deque()  # 单调不减，记录最小值，队头是滑窗内的最小值
        st2 = deque()  # 单调不增，记录最大值，队头是滑窗内的最大值
        l = 0
        for r in range(n):
            while st1 and st1[-1][0] > nums[r]:
                st1.pop()
            st1.append([nums[r], r])
            while st2 and st2[-1][0] < nums[r]:
                st2.pop()
            st2.append([nums[r], r])
            while st1 and st2 and st2[0][0] - st1[0][0] > limit:
                if nums[l] == st2[0][0]:
                    st2.popleft()
                if nums[l] == st1[0][0]:
                    st1.popleft()
                l += 1
            ans = max(ans, r - l + 1)
        return ans


so = Solution()
print(so.longestSubarray(nums = [4,10,2,6,1], limit = 10))
print(so.longestSubarray(nums = [8,2,4,7], limit = 4))




