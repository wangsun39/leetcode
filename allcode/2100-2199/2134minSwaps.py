# 交换 定义为选中一个数组中的两个 互不相同 的位置并交换二者的值。
#
# 环形 数组是一个数组，可以认为 第一个 元素和 最后一个 元素 相邻 。
#
# 给你一个 二进制环形 数组 nums ，返回在 任意位置 将数组中的所有 1 聚集在一起需要的最少交换次数。
#
#
#
# 示例 1：
#
# 输入：nums = [0,1,0,1,1,0,0]
# 输出：1
# 解释：这里列出一些能够将所有 1 聚集在一起的方案：
# [0,0,1,1,1,0,0] 交换 1 次。
# [0,1,1,1,0,0,0] 交换 1 次。
# [1,1,0,0,0,0,1] 交换 2 次（利用数组的环形特性）。
# 无法在交换 0 次的情况下将数组中的所有 1 聚集在一起。
# 因此，需要的最少交换次数为 1 。
# 示例 2：
#
# 输入：nums = [0,1,1,1,0,0,1,1,0]
# 输出：2
# 解释：这里列出一些能够将所有 1 聚集在一起的方案：
# [1,1,1,0,0,0,0,1,1] 交换 2 次（利用数组的环形特性）。
# [1,1,1,1,1,0,0,0,0] 交换 2 次。
# 无法在交换 0 次或 1 次的情况下将数组中的所有 1 聚集在一起。
# 因此，需要的最少交换次数为 2 。
# 示例 3：
#
# 输入：nums = [1,1,0,0,1]
# 输出：0
# 解释：得益于数组的环形特性，所有的 1 已经聚集在一起。
# 因此，需要的最少交换次数为 0 。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# nums[i] 为 0 或者 1

from leetcode.allcode.competition.mypackage import *


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        c0 = nums.count(0)

        def calc(l):
            v0 = l[:c0].count(0)
            cur = res = c0 - v0  # 1 子区间内1的数量
            for i in range(c0, n):
                pre, now = l[i - c0], l[i]
                if now == 1: cur += 1
                if pre == 1: cur -= 1
                res = min(res, cur)
            return res

        r1 = calc(nums)
        # 以下翻转0和1
        c0 = n - c0
        r2 = calc([1 - x for x in nums])
        return min(r1, r2)


so = Solution()






