# 给你一个长度为 n 的整数数组 nums 和一个大小为 q 的二维整数数组 queries，其中 queries[i] = [li, ri, ki, vi]。
#
# 对于每个查询，按以下步骤执行操作：
#
# 设定 idx = li。
# 当 idx <= ri 时：
# 更新：nums[idx] = (nums[idx] * vi) % (109 + 7)
# 将 idx += ki。
# 在处理完所有查询后，返回数组 nums 中所有元素的 按位异或 结果。
#
#
#
# 示例 1：
#
# 输入： nums = [1,1,1], queries = [[0,2,1,4]]
#
# 输出： 4
#
# 解释：
#
# 唯一的查询 [0, 2, 1, 4] 将下标 0 到下标 2 的每个元素乘以 4。
# 数组从 [1, 1, 1] 变为 [4, 4, 4]。
# 所有元素的异或为 4 ^ 4 ^ 4 = 4。
# 示例 2：
#
# 输入： nums = [2,3,1,5,4], queries = [[1,4,2,3],[0,2,1,2]]
#
# 输出： 31
#
# 解释：
#
# 第一个查询 [1, 4, 2, 3] 将下标 1 和 3 的元素乘以 3，数组变为 [2, 9, 1, 15, 4]。
# 第二个查询 [0, 2, 1, 2] 将下标 0、1 和 2 的元素乘以 2，数组变为 [4, 18, 2, 15, 4]。
# 所有元素的异或为 4 ^ 18 ^ 2 ^ 15 ^ 4 = 31。
#
#
# 提示：
#
# 1 <= n == nums.length <= 103
# 1 <= nums[i] <= 109
# 1 <= q == queries.length <= 103
# queries[i] = [li, ri, ki, vi]
# 0 <= li <= ri < n
# 1 <= ki <= n
# 1 <= vi <= 105

from leetcode.allcode.competition.mypackage import *

min = lambda a, b: b if b < a else a
max = lambda a, b: b if b > a else a

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        for l, r, k, v in queries:
            for i in range(l, r + 1, k):
                nums[i] = nums[i] * v % MOD
        return reduce(lambda x, y: x ^ y, nums)


so = Solution()
print(so.xorAfterQueries(nums = [1,1,1], queries = [[0,2,1,4]]))




