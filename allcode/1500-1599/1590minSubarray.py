# 给你一个正整数数组 nums，请你移除 最短 子数组（可以为 空），使得剩余元素的 和 能被 p 整除。 不允许 将整个数组都移除。
#
# 请你返回你需要移除的最短子数组的长度，如果无法满足题目要求，返回 -1 。
#
# 子数组 定义为原数组中连续的一组元素。
#
#
#
# 示例 1：
#
# 输入：nums = [3,1,4,2], p = 6
# 输出：1
# 解释：nums 中元素和为 10，不能被 p 整除。我们可以移除子数组 [4] ，剩余元素的和为 6 。
# 示例 2：
#
# 输入：nums = [6,3,5,2], p = 9
# 输出：2
# 解释：我们无法移除任何一个元素使得和被 9 整除，最优方案是移除子数组 [5,2] ，剩余元素为 [6,3]，和为 9 。
# 示例 3：
#
# 输入：nums = [1,2,3], p = 3
# 输出：0
# 解释：和恰好为 6 ，已经能被 3 整除了。所以我们不需要移除任何元素。
# 示例  4：
#
# 输入：nums = [1,2,3], p = 7
# 输出：-1
# 解释：没有任何方案使得移除子数组后剩余元素的和被 7 整除。
# 示例 5：
#
# 输入：nums = [1000000000,1000000000,1000000000], p = 3
# 输出：0
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= p <= 109





from leetcode.allcode.competition.mypackage import *


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        left = list(accumulate(nums, initial=0))
        right = list(accumulate(nums[::-1]))[::-1] + [0]
        # print(left, right)
        r_dict = defaultdict(list)
        for i, x in enumerate(right):
            r_dict[x % p].append(i)
        for k in r_dict:
            r_dict[k].sort()
        # print(r_dict)
        n = len(nums)
        ans = n
        for i in range(n):
            t = (p - left[i] % p) % p
            pos = bisect_left(r_dict[t], i)
            if pos < len(r_dict[t]):
                ans = min(ans, r_dict[t][pos] - i)
        return ans if ans < n else -1


so = Solution()
print(so.minSubarray(nums = [1,2,3], p = 3))  # 0
print(so.minSubarray(nums = [6,3,5,2], p = 9))  # 2
print(so.minSubarray(nums = [3,1,4,2], p = 6))  # 1
print(so.minSubarray(nums = [1,2,3], p = 7))  # -1
print(so.minSubarray(nums = [1000000000,1000000000,1000000000], p = 3))  # 0





