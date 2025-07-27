# 给你一个下标从 0 开始的整数数组 nums 。
#
# nums 一个长度为 k 的 子序列 指的是选出 k 个 下标 i0 < i1 < ... < ik-1 ，如果这个子序列满足以下条件，我们说它是 平衡的 ：
#
# 对于范围 [1, k - 1] 内的所有 j ，nums[ij] - nums[ij-1] >= ij - ij-1 都成立。
# nums 长度为 1 的 子序列 是平衡的。
#
# 请你返回一个整数，表示 nums 平衡 子序列里面的 最大元素和 。
#
# 一个数组的 子序列 指的是从原数组中删除一些元素（也可能一个元素也不删除）后，剩余元素保持相对顺序得到的 非空 新数组。
#
#
#
# 示例 1：
#
# 输入：nums = [3,3,5,6]
# 输出：14
# 解释：这个例子中，选择子序列 [3,5,6] ，下标为 0 ，2 和 3 的元素被选中。
# nums[2] - nums[0] >= 2 - 0 。
# nums[3] - nums[2] >= 3 - 2 。
# 所以，这是一个平衡子序列，且它的和是所有平衡子序列里最大的。
# 包含下标 1 ，2 和 3 的子序列也是一个平衡的子序列。
# 最大平衡子序列和为 14 。
# 示例 2：
#
# 输入：nums = [5,-1,-3,8]
# 输出：13
# 解释：这个例子中，选择子序列 [5,8] ，下标为 0 和 3 的元素被选中。
# nums[3] - nums[0] >= 3 - 0 。
# 所以，这是一个平衡子序列，且它的和是所有平衡子序列里最大的。
# 最大平衡子序列和为 13 。
# 示例 3：
#
# 输入：nums = [-2,-1]
# 输出：-1
# 解释：这个例子中，选择子序列 [-1] 。
# 这是一个平衡子序列，而且它的和是 nums 所有平衡子序列里最大的。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

from leetcode.allcode.competition.mypackage import *

class Fenwick2:
    # 求前缀最大值（区间求max不能用!!!）
    # 所有函数参数下标从1开始，可以传入使用者的数值x+1的值
    __slots__ = ['f', 'nums']

    def __init__(self, n: int):
        # n 是能调用下面函数的下标最大值
        self.f = [-inf] * (n + 1)   # 关键区间最大值

    def update(self, i: int, val: int) -> None:  # nums[i] = val
        while i < len(self.f):
            self.f[i] = max(self.f[i], val)
            i += i & -i

    def query(self, i: int) -> int:  # 下标<=i的最大值
        mx = -inf
        while i > 0:
            mx = max(mx, self.f[i])
            i &= i - 1
        return mx

class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        n = len(nums)
        fw = Fenwick2(n)
        b = [[i, x - i] for i, x in enumerate(nums)]
        b.sort(key=lambda x: x[1])
        ans = -inf
        for i, bi in b:
            mx = fw.query(i + 1)
            if mx == -inf:
                fw.update(i + 1, nums[i])
                ans = max(ans, nums[i])
            elif mx < 0:
                if mx < nums[i]:
                    fw.update(i + 1, nums[i])
                    ans = max(ans, nums[i])
            else:
                fw.update(i + 1, mx + nums[i])
                ans = max(ans, mx + nums[i])

        return ans




so = Solution()
print(so.maxBalancedSubsequenceSum([-2,-1]))
print(so.maxBalancedSubsequenceSum([3,3,5,6]))
print(so.maxBalancedSubsequenceSum([-1,4,8,5,8,2,-8]))
print(so.maxBalancedSubsequenceSum([5,-1,-3,8]))




