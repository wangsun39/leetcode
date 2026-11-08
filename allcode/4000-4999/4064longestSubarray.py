# 给你一个整数数组 nums 和一个整数 k。
#
# 如果一个子数组的和能够被 k 整除，或者在 将该子数组中的一个元素取反 后能使和被 k 整除，则称该子数组是 有效的 。
#
# 将一个元素取反意味着将其值 x 替换为 -x。
#
# 返回 最长有效子数组的长度 。如果不存在有效的子数组，则返回 0。
#
# 子数组 是数组中一个连续且非空的元素序列。
#
#
#
# 示例 1：
#
# 输入： nums = [4,1,2], k = 3
#
# 输出： 3
#
# 解释：
#
# 整个数组的和为 7，且 7 % 3 = 1，因此它不能被 k = 3 整除。
# 将 nums[2] = 2 取反，其和变为 4 + 1 − 2 = 3，能够被 k 整除。
# 因此，整个数组是一个有效子数组，其长度为 3。
# 示例 2：
#
# 输入： nums = [5,3,4], k = 7
#
# 输出： 2
#
# 解释：
#
# 整个数组的和为 12，且将其中任何一个元素取反都无法使其和被 7 整除。
# 然而，子数组 [3, 4] 的和为 7，无需任何取反操作即可被 k = 7 整除。
# 因此，最长有效子数组的长度为 2。
# 示例 3：
#
# 输入： nums = [2,2,5], k = 6
#
# 输出： 2
#
# 解释：
#
# 整个数组的和为 9，且将其中任何一个元素取反都无法使其和被 6 整除。
# 子数组 [2, 2] 的和为 4。将其中任意一个元素取反会使其变为 [-2, 2] 或 [2, -2]，这两者的和皆为 0。
# 因此，最长有效子数组的长度为 2。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# -105 <= nums[i] <= 105
# 1 <= k <= 3000

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a


class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        left = [inf] * k  # 前缀和模k为i的最左侧下标
        left[0] = 0
        right = [-inf] * k  # 前缀和模k为i的最右侧下标
        right[0] = 0
        pos = defaultdict(list)  # 记录每个元素*2模k后值的在数组中的位置位置
        s = 0
        for i, x in enumerate(nums):
            s += x
            s %= k
            left[s] = MIN(left[s], i + 1)
            right[s] = MAX(right[s], i + 1)
            pos[x * 2 % k].append(i)

        ans = 0
        # 枚举左端点模k为i，右端点模k为j的子数组
        for i in range(k):
            if left[i] == inf: continue
            for j in range(k):
                if right[j] <= left[i]: continue

                # [left[i], right[j]) 的和模k余 i-j，需要在相同区间找一个数a，如果能保证 (i-j-2a )%k==0 ，那么这个区间满足要求
                t = (j - i) % k
                if t == 0:
                    ans = MAX(ans, right[j] - left[i])
                elif t in pos:
                    p = bisect_left(pos[t], left[i])
                    if p < len(pos[t]) and pos[t][p] < right[j]:
                        ans = MAX(ans, right[j] - left[i])

        return ans




so = Solution()
print(so.longestSubarray(nums = [2,2,5], k = 6))
print(so.longestSubarray(nums = [4,1,2], k = 3))
print(so.longestSubarray(nums = [5,3,4], k = 7))



