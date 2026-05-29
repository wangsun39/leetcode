# 给你一个长度为 n 的整数数组 nums 和一个查询数组 queries，其中 queries[i] = [li, ri, thresholdi]。
#
# 返回一个整数数组 ans，其中 ans[i] 等于子数组 nums[li...ri] 中出现 至少 thresholdi 次的元素，选择频率 最高 的元素（如果频率相同则选择 最小 的元素），如果不存在这样的元素则返回 -1。
#
#
#
# 示例 1:
#
# 输入： nums = [1,1,2,2,1,1], queries = [[0,5,4],[0,3,3],[2,3,2]]
#
# 输出： [1,-1,2]
#
# 解释：
#
# 查询	子数组	阈值	频率表	答案
# [0, 5, 4]	[1, 1, 2, 2, 1, 1]	4	1 → 4, 2 → 2	1
# [0, 3, 3]	[1, 1, 2, 2]	3	1 → 2, 2 → 2	-1
# [2, 3, 2]	[2, 2]	2	2 → 2	2
#
#
# 示例 2:
#
# 输入：nums = [3,2,3,2,3,2,3], queries = [[0,6,4],[1,5,2],[2,4,1],[3,3,1]]
#
# 输出：[3,2,3,2]
#
# 解释：
#
# 查询	子数组	阈值	频率表	答案
# [0, 6, 4]	[3, 2, 3, 2, 3, 2, 3]	4	3 → 4, 2 → 3	3
# [1, 5, 2]	[2, 3, 2, 3, 2]	2	2 → 3, 3 → 2	2
# [2, 4, 1]	[3, 2, 3]	1	3 → 2, 2 → 1	3
# [3, 3, 1]	[2]	1	2 → 1	2
#
#
# 提示：
#
# 1 <= nums.length == n <= 104
# 1 <= nums[i] <= 109
# 1 <= queries.length <= 5 * 104
# queries[i] = [li, ri, thresholdi]
# 0 <= li <= ri < n
# 1 <= thresholdi <= ri - li + 1

from leetcode.allcode.competition.mypackage import *

class Solution:
    def subarrayMajority(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        q = len(queries)
        b = int(n ** 0.5)  # 分块大小
        m = (n + b - 1) // b  # 分块的个数
        Qry = [[] for _ in range(m)]
        for i, [l, r, th] in enumerate(queries):
            Qry[l // b].append([i, l, r, th])
        for i in range(m):
            Qry[i].sort(key=lambda x: x[2])

        ans = [-1] * q
        for j, gq in enumerate(Qry):
            # j 是分块的序号
            bl, br = j * b, (j + 1) * b  # 第一个块的左右端点
            # tmp_val = tmp_mx = 0  # 回滚临时变量
            val, mx = inf, 0  # 变量
            stat = Counter()  #
            idx = br
            for i, l, r, th in gq:  # 对一组查询进行处理
                # 一组查询的左端点都在一个分块内
                if r < br:
                    # 左右端点都在一个分块内，暴力处理
                    counter = Counter(nums[l: r + 1])
                    e, mx1 = 0, 0
                    for x, c in counter.items():
                        if c > mx1:
                            e = x
                            mx1 = c
                        elif c == mx1 and x < e:
                            e = x
                    ans[i] = e if mx1 >= th else -1
                    continue
                # 右端点是在下个分块中的，并且右端点单调升，对应br只增不减
                while idx <= r:
                    stat[nums[idx]] += 1
                    if stat[nums[idx]] > mx:
                        val = nums[idx]
                        mx = stat[nums[idx]]
                    elif stat[nums[idx]] == mx and val > nums[idx]:
                        val = nums[idx]
                    idx += 1
                tmp_mx, tmp_val = mx, val
                for k in range(l, br):
                    stat[nums[k]] += 1
                    if stat[nums[k]] > mx:
                        val = nums[k]
                        mx = stat[nums[k]]
                    elif stat[nums[k]] == mx and val > nums[k]:
                        val = nums[k]

                # [l, r]所有元素都放入 stat
                ans[i] = val if mx >= th else -1

                # 回滚 [l, br) 的数
                for k in range(l, br):
                    stat[nums[k]] -= 1
                mx, val = tmp_mx, tmp_val

        return ans



so = Solution()
print(so.subarrayMajority(nums = [10,10,19,19], queries = [[1,2,1],[0,3,2],[3,3,1],[1,3,3],[1,1,1],[0,2,1],[0,1,2],[2,2,1],[3,3,1],[3,3,1],[0,2,1],[0,3,1],[1,3,1],[0,1,2],[3,3,1],[1,3,1]]))
print(so.subarrayMajority(nums = [4,5], queries = [[0,1,1],[1,1,1],[0,0,1],[1,1,1],[0,0,1],[0,0,1],[0,1,1],[0,1,1],[1,1,1],[0,1,1],[0,0,1],[1,1,1],[1,1,1],[0,0,1],[1,1,1],[0,1,1]]))
print(so.subarrayMajority(nums = [1,1,2,2,1,1], queries = [[0,5,4],[0,3,3],[2,3,2]]))



