# 给你一个整数数组 nums，nums 是 严格递增 的。
#
# 对于每个下标 x，设 closest(x) 为使得 abs(nums[x] - nums[y]) 最小化 的 相邻 下标。如果两个 相邻 下标的差值相同，则选择 较小 的下标。
#
# 从任意下标 x 出发，你可以通过以下两种方式移动：
#
# 移动到任意下标 y，代价为 abs(nums[x] - nums[y])，或者
# 移动到 closest(x)，代价为 1。
# 同时给你一个二维整数数组 queries，其中每个 queries[i] = [li, ri]。
#
# 对于每个查询，计算从下标 li 移动到下标 ri 的 最小总代价。
#
# 返回一个整数数组 ans，其中 ans[i] 是第 i 个查询的答案。
#
# 如果一个数组的每个元素都 严格大于 其前一个元素，则称该数组为 严格递增 的。
#
# 两个值 x 和 y 之间的 绝对差 定义为 abs(x - y)。
#
#
#
# 示例 1：
#
# 输入： nums = [-5,-2,3], queries = [[0,2],[2,0],[1,2]]
#
# 输出： [6,2,5]
#
# 解释：
#
# 最近的下标分别是 [1, 0, 1]。
# 对于 [0, 2]，路径 0 → 1 → 2 包含一次从下标 0 到 1 的最近移动，代价为 1，以及一次从下标 1 到 2 的移动，代价为 |-2 - 3| = 5，总代价为 1 + 5 = 6。
# 对于 [2, 0]，路径 2 → 1 → 0 包含两次最近移动，分别从下标 2 到 1 和从下标 1 到 0，每次代价为 1，总代价为 2。
# 对于 [1, 2]，从下标 1 直接移动到下标 2 的代价为 |-2 - 3| = 5，这是最优的。
# 因此，ans = [6, 2, 5]。
#
# 示例 2：
#
# 输入： nums = [0,2,3,9], queries = [[3,0],[1,2],[2,0]]
#
# 输出： [4,1,3]
#
# 解释：
#
# 最近的下标分别是 [1, 2, 1, 2]。
# 对于 [3, 0]，路径 3 → 2 → 1 → 0 包含两次最近移动，分别从下标 3 到 2 和从 2 到 1，每次代价为 1，以及一次从 1 到 0 的移动，代价为 |2 - 0| = 2，总代价为 1 + 1 + 2 = 4。
# 对于 [1, 2]，从下标 1 到 2 的最近移动代价为 1。
# 对于 [2, 0]，路径 2 → 1 → 0 包含一次从下标 2 到 1 的最近移动，代价为 1，以及一次从 1 到 0 的移动，代价为 |2 - 0| = 2，总代价为 1 + 2 = 3。
# 因此，ans = [4, 1, 3]。
#
#
#
# 提示：
#
# 2 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums 严格递增
# 1 <= queries.length <= 105
# queries[i] = [li, ri]
# 0 <= li, ri < nums.length

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        left[1] = 1
        right[n - 2] = 1
        for i in range(1, n - 1):
            if nums[i] - nums[i - 1] <= nums[i + 1] - nums[i]:
                left[i + 1] = left[i] + nums[i + 1] - nums[i]
            else:
                left[i + 1] = left[i] + 1
        for i in range(n - 2, 0, -1):
            if nums[i] - nums[i - 1] <= nums[i + 1] - nums[i]:
                right[i - 1] = right[i] + 1
            else:
                right[i - 1] = right[i] + nums[i] - nums[i - 1]

        ans = []
        for x, y in queries:
            if x == y:
                ans.append(0)
            elif x < y:
                ans.append(left[y] - left[x])
            else:
                ans.append(right[y] - right[x])
        return ans


so = Solution()
print(so.minCost(nums = [-5,-2,3], queries = [[0,2],[2,0],[1,2]]))
print(so.minCost(nums = [-12,-4,17,24], queries = [[2,0],[0,2]]))
print(so.minCost(nums = [-5,13,20], queries = [[0,1]]))




