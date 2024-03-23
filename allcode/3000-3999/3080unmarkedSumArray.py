# 给你一个长度为 n 下标从 0 开始的正整数数组 nums 。
#
# 同时给你一个长度为 m 的二维操作数组 queries ，其中 queries[i] = [indexi, ki] 。
#
# 一开始，数组中的所有元素都 未标记 。
#
# 你需要依次对数组执行 m 次操作，第 i 次操作中，你需要执行：
#
# 如果下标 indexi 对应的元素还没标记，那么标记这个元素。
# 然后标记 ki 个数组中还没有标记的 最小 元素。如果有元素的值相等，那么优先标记它们中下标较小的。如果少于 ki 个未标记元素存在，那么将它们全部标记。
# 请你返回一个长度为 m 的数组 answer ，其中 answer[i]是第 i 次操作后数组中还没标记元素的 和 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,2,1,2,3,1], queries = [[1,2],[3,3],[4,2]]
#
# 输出：[8,3,0]
#
# 解释：
#
# 我们依次对数组做以下操作：
#
# 标记下标为 1 的元素，同时标记 2 个未标记的最小元素。标记完后数组为 nums = [1,2,2,1,2,3,1] 。未标记元素的和为 2 + 2 + 3 + 1 = 8 。
# 标记下标为 3 的元素，由于它已经被标记过了，所以我们忽略这次标记，同时标记最靠前的 3 个未标记的最小元素。标记完后数组为 nums = [1,2,2,1,2,3,1] 。未标记元素的和为 3 。
# 标记下标为 4 的元素，由于它已经被标记过了，所以我们忽略这次标记，同时标记最靠前的 2 个未标记的最小元素。标记完后数组为 nums = [1,2,2,1,2,3,1] 。未标记元素的和为 0 。
# 示例 2：
#
# 输入：nums = [1,4,2,3], queries = [[0,1]]
#
# 输出：[7]
#
# 解释：我们执行一次操作，将下标为 0 处的元素标记，并且标记最靠前的 1 个未标记的最小元素。标记完后数组为 nums = [1,4,2,3] 。未标记元素的和为 4 + 3 = 7 。
#
#
#
# 提示：
#
# n == nums.length
# m == queries.length
# 1 <= m <= n <= 105
# 1 <= nums[i] <= 105
# queries[i].length == 2
# 0 <= indexi, ki <= n - 1

from leetcode.allcode.competition.mypackage import *

class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        snums = deque(sorted([x, i] for i, x in enumerate(nums)))
        vis = set()
        s = sum(nums)
        ans = [0] * len(queries)
        for ii, [idx, k] in enumerate(queries):
            if idx not in vis:
                s -= nums[idx]
                vis.add(idx)
            j = k
            while j > 0 and len(snums):
                x, i = snums.popleft()
                if i not in vis:
                    j -= 1
                    vis.add(i)
                    s -= x
            ans[ii] = s
            if s == 0:
                break
        return ans


so = Solution()
print(so.unmarkedSumArray(nums = [1,2,2,1,2,3,1], queries = [[1,2],[3,3],[4,2]]))
print(so.unmarkedSumArray(nums = [1,4,2,3], queries = [[0,1]]))




