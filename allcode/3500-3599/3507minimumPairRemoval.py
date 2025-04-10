# 给你一个数组 nums，你可以执行以下操作任意次数：
#
# 选择 相邻 元素对中 和最小 的一对。如果存在多个这样的对，选择最左边的一个。
# 用它们的和替换这对元素。
# 返回将数组变为 非递减 所需的 最小操作次数 。
#
# 如果一个数组中每个元素都大于或等于它前一个元素（如果存在的话），则称该数组为非递减。
#
#
#
# 示例 1：
#
# 输入： nums = [5,2,3,1]
#
# 输出： 2
#
# 解释：
#
# 元素对 (3,1) 的和最小，为 4。替换后 nums = [5,2,4]。
# 元素对 (2,4) 的和为 6。替换后 nums = [5,6]。
# 数组 nums 在两次操作后变为非递减。
#
# 示例 2：
#
# 输入： nums = [1,2,2]
#
# 输出： 0
#
# 解释：
#
# 数组 nums 已经是非递减的。
#
#
#
# 提示：
#
# 1 <= nums.length <= 50
# -1000 <= nums[i] <= 1000

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def check(arr):
            # print(list(p <= q for p, q in pairwise(arr)))
            return all(p <= q for p, q in pairwise(arr))
        ans = 0
        while not check(nums):
            print(nums)
            pair = list(q + p for p, q in pairwise(nums))
            mn = min(pair)
            for i, x in enumerate(pair):
                if x == mn:
                    break
            nums = nums[:i] + [pair[i]] + nums[i + 2:]
            ans += 1
        return ans


so = Solution()
print(so.minimumPairRemoval([-2,1,2,-1,-1,-2,-2,-1,-1,1,1]))  # 10
print(so.minimumPairRemoval([5,2,3,1]))
print(so.minimumPairRemoval([1,2,2]))




