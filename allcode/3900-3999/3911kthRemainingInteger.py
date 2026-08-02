# 给你一个整数数组 nums，其中 nums 是 严格递增 的。
#
# 另给你一个二维整数数组 queries，其中 queries[i] = [li, ri, ki]。
#
# 对于每个查询 [li, ri, ki]：
#
# 考虑 子数组 nums[li..ri]
# 从 无限 的所有 正偶数 序列中：2, 4, 6, 8, 10, 12, 14, ...
# 移除 所有出现在 子数组 nums[li..ri] 中的元素。
# 找到移除后序列中剩余的第 ki 个 最小整数。
# 返回一个整数数组 ans，其中 ans[i] 是第 i 个查询的结果。
#
# 子数组 是数组中连续的 非空 元素序列。
#
# 如果数组中的每个元素都 严格大于 它的 前一个 元素（如果存在），则称该数组是 严格递增 的。
#
#
#
# 示例 1：
#
# 输入： nums = [1,4,7], queries = [[0,2,1],[1,1,2],[0,0,3]]
#
# 输出： [2,6,6]
#
# 解释：
#
# i	queries[i]	nums[li..ri]	移除的
# 偶数	剩余的
# 偶数	ki	ans[i]
# 0	[0, 2, 1]	[1, 4, 7]	[4]	2, 6, 8, ...	1	2
# 1	[1, 1, 2]	[4]	[4]	2, 6, 8, ...	2	6
# 2	[0, 0, 3]	[1]	[]	2, 4, 6, ...	3	6
# 因此，ans = [2, 6, 6]。
#
# 示例 2：
#
# 输入： nums = [2,5,8], queries = [[0,1,2],[1,2,1],[0,2,4]]
#
# 输出： [6,2,12]
#
# 解释：
#
# i	queries[i]	nums[li..ri]	移除的
# 偶数	剩余的
# 偶数	ki	ans[i]
# 0	[0, 1, 2]	[2, 5]	[2]	4, 6, 8, ...	2	6
# 1	[1, 2, 1]	[5, 8]	[8]	2, 4, 6, ...	1	2
# 2	[0, 2, 4]	[2, 5, 8]	[2, 8]	4, 6, 10, 12, ...	4	12
# 因此，ans = [6, 2, 12]。
#
# 示例 3：
#
# 输入： nums = [3,6], queries = [[0,1,1],[1,1,3]]
#
# 输出： [2,8]
#
# 解释：
#
# i	queries[i]	nums[li..ri]	移除的
# 偶数	剩余的
# 偶数	ki	ans[i]
# 0	[0, 1, 1]	[3, 6]	[6]	2, 4, 8, ...	1	2
# 1	[1, 1, 3]	[6]	[6]	2, 4, 8, ...	3	8
# 因此，ans = [2, 8]。
#
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# nums 是严格递增的
# 1 <= queries.length <= 105
# queries[i] = [li, ri, ki]
# 0 <= li <= ri < nums.length
# 1 <= ki <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def kthRemainingInteger(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        s = [0] * n  # s[i] 表示 nums[:i + 1] 中 区间[0, nums[i]] 内不能选的偶数个数
        s2 = [0] * n  # s[i] 表示 nums[:i + 1] 中 区间[0, nums[i]] 内能选的偶数个数
        s[0] = 0 if nums[0] & 1 else 1
        for i, x in enumerate(nums[1:], 1):
            if x & 1:
                s[i] = s[i - 1]
            else:
                s[i] = s[i - 1] + 1
        for i, x in enumerate(nums):
            s2[i] = nums[i] // 2 - s[i]

        def lastEven(i):  # 不超过nums[i]的最大偶数
            return nums[i] // 2 * 2

        def pre(i):  # [0, nums[i]] 中有多少个偶数，l<=i<=r
            if l:
                tm = s[i] - s[l - 1]
            else:
                tm = s[i]
            return nums[i] // 2 -  tm

        ans = [0] * len(queries)
        for i, [l, r, k] in enumerate(queries):
            tl = (nums[l] - 1) // 2   # < nums[l] 的偶数总个数
            pre_r = pre(r)
            if tl >= k:
                ans[i] = 2 * k
            elif pre_r < k:
                t = k - pre_r
                ans[i] = lastEven(r) + 2 * t
            else:
                t1 = k - tl  # 在区间[nums[l],  nums[r]] 中找第 t1 个偶数
                a = s2[l] + t1
                # 等价于在s2中找 <a 的最后一个位置
                p = bisect_left(s2, a) - 1
                if p < 0:
                    if l:
                        p = l - 1
                    else:
                        p = 0
                # 下面计算 [0, nums[p]] 中有多少个偶数
                sq = pre(p)
                st = k - sq
                ans[i] = lastEven(p) + st * 2

        return ans



so = Solution()
print(so.kthRemainingInteger(nums = [5,15,18,26], queries = [[1,3,10],[2,3,26]]))  # [22,56]
print(so.kthRemainingInteger(nums = [16,19], queries = [[1,1,10]]))  # [20]
print(so.kthRemainingInteger(nums = [9,15], queries = [[0,1,7]]))
print(so.kthRemainingInteger(nums = [1,4,7], queries = [[0,2,1],[1,1,2],[0,0,3]]))




