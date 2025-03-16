# 给你一个 循环 数组 nums 和一个数组 queries 。
#
# 对于每个查询 i ，你需要找到以下内容：
#
# 数组 nums 中下标 queries[i] 处的元素与 任意 其他下标 j（满足 nums[j] == nums[queries[i]]）之间的 最小 距离。如果不存在这样的下标 j，则该查询的结果为 -1 。
# 返回一个数组 answer，其大小与 queries 相同，其中 answer[i] 表示查询i的结果。
#
#
#
# 示例 1：
#
# 输入： nums = [1,3,1,4,1,3,2], queries = [0,3,5]
#
# 输出： [2,-1,3]
#
# 解释：
#
# 查询 0：下标 queries[0] = 0 处的元素为 nums[0] = 1 。最近的相同值下标为 2，距离为 2。
# 查询 1：下标 queries[1] = 3 处的元素为 nums[3] = 4 。不存在其他包含值 4 的下标，因此结果为 -1。
# 查询 2：下标 queries[2] = 5 处的元素为 nums[5] = 3 。最近的相同值下标为 1，距离为 3（沿着循环路径：5 -> 6 -> 0 -> 1）。
# 示例 2：
#
# 输入： nums = [1,2,3,4], queries = [0,1,2,3]
#
# 输出： [-1,-1,-1,-1]
#
# 解释：
#
# 数组 nums 中的每个值都是唯一的，因此没有下标与查询的元素值相同。所有查询的结果均为 -1。
#
#
#
# 提示：
#
# 1 <= queries.length <= nums.length <= 105
# 1 <= nums[i] <= 106
# 0 <= queries[i] < nums.length

from leetcode.allcode.competition.mypackage import *

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        dd = defaultdict(list)
        for i, x in enumerate(nums):
            dd[x].append(i)
        n = len(nums)
        ans = []
        for i in queries:
            x = nums[i]
            p = bisect_left(dd[x], i)
            l = len(dd[x])
            if l == 1:
                ans.append(-1)
                continue
            mn = inf
            if p > 0:
                mn = min(mn, i - dd[x][p - 1])
            else:
                mn = min(mn, i + n - dd[x][-1])
            if p < l - 1:
                mn = min(mn, dd[x][p + 1] - i)
            else:
                mn = min(mn, dd[x][0] + n - i)
            ans.append(mn)
        return ans



so = Solution()
print(so.solveQueries(nums = [1,3,1,4,1,3,2], queries = [0,3,5]))




