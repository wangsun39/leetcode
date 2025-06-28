# 给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
#
#
#
# 示例 1：
#
# 输入：nums = [3,2,3]
# 输出：[3]
# 示例 2：
#
# 输入：nums = [1]
# 输出：[1]
# 示例 3：
#
# 输入：nums = [1,2]
# 输出：[1,2]
#
#
# 提示：
#
# 1 <= nums.length <= 5 * 104
# -109 <= nums[i] <= 109
#
#
# 进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        n = len(nums)
        ans = []
        for k, v in counter.items():
            if v > n // 3:
                ans.append(k)
        return ans



so = Solution()
print(so.majorityElement([3,2,3]))




