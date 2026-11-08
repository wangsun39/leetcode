# 给定一个整数数组 nums 和一个整数 k。
#
# 同时给定一个二维整数数组 queries，其中 queries[i] = [li, ri] 表示子数组 nums[li..ri]。
#
# 对于每个查询，如果子数组 nums[li..ri] 满足以下条件，则认为该 子数组 是 有效的：
#
# 它 恰好 包含 k 个 不同 的数字，并且
# 子数组中每个数字出现的 频率 都是 偶数。
# 返回一个布尔数组 ans，其中如果 nums[li..ri] 是 有效的，则 ans[i] 为 true，否则为 false。
#
#
#
# 示例 1：
#
# 输入： nums = [1,2,2,1], k = 2, queries = [[0,1],[0,3],[1,2]]
#
# 输出： [false,true,false]
#
# 解释：
#
# i	[li, ri]	子数组	不同的数字	频率	有效性检查
# 0	[0, 1]	[1, 2]	{1, 2} → 2	{1: 1, 2: 1}	false：元素出现的次数不是偶数。
# 1	[0, 3]	[1, 2, 2, 1]	{1, 2} → 2	{1: 2, 2: 2}	true：恰好有 k = 2 个不同的元素，并且所有元素出现的次数都是偶数。
# 2	[1, 2]	[2, 2]	{2} → 1	{2: 2}	false：不同元素的数量小于 k = 2。
# 因此，ans = [false, true, false]。
#
# 示例 2：
#
# 输入： nums = [3,3,3], k = 1, queries = [[1,2],[0,2]]
#
# 输出： [true,false]
#
# 解释：
#
# i	[li, ri]	子数组	不同的数字	频率	有效性检查
# 0	[1, 2]	[3, 3]	{3} → 1	{3: 2}	true：恰好有 k = 1 个不同的元素，并且该元素出现的次数为偶数。
# 1	[0, 2]	[3, 3, 3]	{3} → 1	{3: 3}	false：数字 3 出现的次数不是偶数。
# 因此，ans = [true, false]。
#
#
#
# 提示：
#
# 2 <= n == nums.length <= 105
# 1 <= nums[i] <= 105
# 1 <= k <= n
# 1 <= queries.length <= 105
# queries[i] == [li, ri]
# 0 <= li < ri <= n - 1

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a


class Solution:
    def validSubarrays(self, nums: list[int], k: int, queries: list[list[int]]) -> list[bool]:
        n = len(nums)
        q = len(queries)
        b = int(n ** 0.5)  # 分块大小
        m = (n + b - 1) // b  # 分块的个数
        Qry = [[] for _ in range(m)]
        for i, [l, r] in enumerate(queries):
            Qry[l // b].append([i, l, r])
        for i in range(m):
            Qry[i].sort(key=lambda x: x[2])

        ans = [-1] * q
        for j, gq in enumerate(Qry):
            # j 是分块的序号
            if len(gq) == 0: continue
            bl, br = j * b, (j + 1) * b  # 第一个块的左右端点
            stat = Counter()
            even_num = 0
            cur_l, cur_r = min(br - 1, n - 1), min(br, n)
            for i, l, r in gq:  # 对一组查询进行处理

                while cur_l >= l:
                    # print(cur_l, n, l, r)
                    stat[nums[cur_l]] += 1
                    if stat[nums[cur_l]] % 2 == 0:
                        even_num += 1
                    elif stat[nums[cur_l]] > 1:
                        even_num -= 1
                    cur_l -= 1
                # 右端点是在下个分块中的，并且右端点单调升，对应br只增不减
                while cur_r <= r:
                    stat[nums[cur_r]] += 1
                    if stat[nums[cur_r]] % 2 == 0:
                        even_num += 1
                    elif stat[nums[cur_r]] > 1:
                        even_num -= 1
                    cur_r += 1
                while cur_l < l - 1:
                    stat[nums[cur_l + 1]] -= 1
                    if stat[nums[cur_l + 1]] % 2 == 1:
                        even_num -= 1
                    elif stat[nums[cur_l + 1]] > 0:
                        even_num += 1
                    else:
                        del (stat[nums[cur_l + 1]])
                    cur_l += 1
                while cur_r > r + 1:
                    stat[nums[cur_r - 1]] -= 1
                    if stat[nums[cur_r - 1]] % 2 == 1:
                        even_num -= 1
                    elif stat[nums[cur_r - 1]] > 0:
                        even_num += 1
                    else:
                        del (stat[nums[cur_r - 1]])
                    cur_r -= 1

                ans[i] = (len(stat) == k) and (even_num == k)

        return ans


so = Solution()
print(so.validSubarrays(nums = [184,184,262,262,113,113,259,259,246,93,93,246,126,35,126,35,213], k = 2, queries = [[4,7]]))
print(so.validSubarrays(nums = [1,2,2,1], k = 2, queries = [[0,1],[0,3],[1,2]]))



