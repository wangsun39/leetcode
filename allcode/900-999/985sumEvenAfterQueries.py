# 给出一个整数数组 A 和一个查询数组 queries。
#
# 对于第 i 次查询，有 val = queries[i][0], index = queries[i][1]，我们会把 val 加到 A[index] 上。然后，第 i 次查询的答案是 A 中偶数值的和。
#
# （此处给定的 index = queries[i][1] 是从 0 开始的索引，每次查询都会永久修改数组 A。）
#
# 返回所有查询的答案。你的答案应当以数组 answer 给出，answer[i] 为第 i 次查询的答案。
#
#
#
# 示例：
#
# 输入：A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
# 输出：[8,6,2,4]
# 解释：
# 开始时，数组为 [1,2,3,4]。
# 将 1 加到 A[0] 上之后，数组为 [2,2,3,4]，偶数值之和为 2 + 2 + 4 = 8。
# 将 -3 加到 A[1] 上之后，数组为 [2,-1,3,4]，偶数值之和为 2 + 4 = 6。
# 将 -4 加到 A[0] 上之后，数组为 [-2,-1,3,4]，偶数值之和为 -2 + 4 = 2。
# 将 2 加到 A[3] 上之后，数组为 [-2,-1,3,6]，偶数值之和为 -2 + 6 = 4。
#
#
# 提示：
#
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# 1 <= queries.length <= 10000
# -10000 <= queries[i][0] <= 10000
# 0 <= queries[i][1] < A.length

from typing import List


class Solution:
    def sumEvenAfterQueries(self, A, queries):
        cur_sum = 0
        for i in A:
            if 0 == i % 2:
                cur_sum += i
        res = []
        for e in queries:
            if 0 == A[e[1]] % 2:
                if 0 == e[0] % 2:
                    cur_sum += e[0]
                else:
                    cur_sum -= A[e[1]]
                res.append(cur_sum)
                A[e[1]] += e[0]
            else:
                if 1 == e[0] % 2:
                    cur_sum += (A[e[1]]+e[0])
                res.append(cur_sum)
                A[e[1]] += e[0]
        return res

    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s = sum(x for x in nums if x & 1 == 0)
        ans = [0] * len(queries)
        for i, x in enumerate(queries):
            if nums[x[1]] & 1 == 0:
                s -= nums[x[1]]
            nums[x[1]] += x[0]
            if nums[x[1]] & 1 == 0:
                s += nums[x[1]]
            ans[i] = s
        return ans

so = Solution()
print(so.sumEvenAfterQueries([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]]))

