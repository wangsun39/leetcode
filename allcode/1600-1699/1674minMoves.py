# 给你一个长度为 偶数 n 的整数数组 nums 和一个整数 limit 。每一次操作，你可以将 nums 中的任何整数替换为 1 到 limit 之间的另一个整数。
#
# 如果对于所有下标 i（下标从 0 开始），nums[i] + nums[n - 1 - i] 都等于同一个数，则数组 nums 是 互补的 。例如，数组 [1,2,3,4] 是互补的，因为对于所有下标 i ，nums[i] + nums[n - 1 - i] = 5 。
#
# 返回使数组 互补 的 最少 操作次数。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,4,3], limit = 4
# 输出：1
# 解释：经过 1 次操作，你可以将数组 nums 变成 [1,2,2,3]（加粗元素是变更的数字）：
# nums[0] + nums[3] = 1 + 3 = 4.
# nums[1] + nums[2] = 2 + 2 = 4.
# nums[2] + nums[1] = 2 + 2 = 4.
# nums[3] + nums[0] = 3 + 1 = 4.
# 对于每个 i ，nums[i] + nums[n-1-i] = 4 ，所以 nums 是互补的。
# 示例 2：
#
# 输入：nums = [1,2,2,1], limit = 2
# 输出：2
# 解释：经过 2 次操作，你可以将数组 nums 变成 [2,2,2,2] 。你不能将任何数字变更为 3 ，因为 3 > limit 。
# 示例 3：
#
# 输入：nums = [1,2,1,2], limit = 2
# 输出：0
# 解释：nums 已经是互补的。
#
#
# 提示：
#
# n == nums.length
# 2 <= n <= 105
# 1 <= nums[i] <= limit <= 105
# n 是偶数。

from leetcode.allcode.competition.mypackage import *


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        seg1 = []
        n = len(nums)
        nums1 = nums[: n // 2][:]
        nums2 = nums[n // 2:][::-1]
        for i in range(n // 2):
            seg1.append([nums1[i] + 1, nums1[i] + limit, i])
            seg1.append([nums2[i] + 1, nums2[i] + limit, i])
        seg0 = []
        for i in range(n // 2):
            seg0.append([nums1[i] + nums2[i], i])
        seg0.sort()
        seg1.sort()
        ans = n * 2
        idx0 = 0
        idx1l = idx1r = 0  # 区间 [idx1l, idx1r) 是 seg1 的滑窗
        s1 = Counter()
        for x in range(2, max(nums) * 2 + 1):
            # 枚举最终 nums[i] + nums[n - 1 - i] 的和
            s0 = set()
            while idx0 < len(seg0) and seg0[idx0][0] == x:
                s0.add(seg0[idx0][1])
                idx0 += 1
            while idx1l < len(seg1) and seg1[idx1l][1] < x:
                s1[seg1[idx1l][2]] -= 1
                if s1[seg1[idx1l][2]] == 0:
                    del(s1[seg1[idx1l][2]])
                idx1l += 1
            while idx1r < len(seg1) and seg1[idx1r][0] <= x <= seg1[idx1r][1]:
                s1[seg1[idx1r][2]] += 1
                idx1r += 1
            # 在s0中的不需要操作，s1 中的要操作一次，其他的要操作 2 次
            cnt = res = len(s1)
            for y in s0:
                if y in s1:
                    res -= 1  # 从res减去，s0中的点
                else:
                    cnt += 1  # 统计s0和s1合计的点
            res += (n // 2 - cnt) * 2
            ans = min(ans, res)
        return ans



so = Solution()
print(so.minMoves(nums = [1,2,4,3], limit = 4))




