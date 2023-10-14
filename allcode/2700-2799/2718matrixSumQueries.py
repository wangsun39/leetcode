# 给你一个整数 n 和一个下标从 0 开始的 二维数组 queries ，其中 queries[i] = [typei, indexi, vali] 。
#
# 一开始，给你一个下标从 0 开始的 n x n 矩阵，所有元素均为 0 。每一个查询，你需要执行以下操作之一：
#
# 如果 typei == 0 ，将第 indexi 行的元素全部修改为 vali ，覆盖任何之前的值。
# 如果 typei == 1 ，将第 indexi 列的元素全部修改为 vali ，覆盖任何之前的值。
# 请你执行完所有查询以后，返回矩阵中所有整数的和。
#
#
#
# 示例 1：
#
#
#
# 输入：n = 3, queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]]
# 输出：23
# 解释：上图展示了每个查询以后矩阵的值。所有操作执行完以后，矩阵元素之和为 23 。
# 示例 2：
#
#
#
# 输入：n = 3, queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]
# 输出：17
# 解释：上图展示了每一个查询操作之后的矩阵。所有操作执行完以后，矩阵元素之和为 17 。
#
#
# 提示：
#
# 1 <= n <= 104
# 1 <= queries.length <= 5 * 104
# queries[i].length == 3
# 0 <= typei <= 1
# 0 <= indexi < n
# 0 <= vali <= 105
from leetcode.allcode.competition.mypackage import *

class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        # mat = [[0] * n for _ in range(n)]
        m = len(queries)
        unvis_r, unvis_c = set(range(n)), set(range(n))
        ans = 0
        for i in range(m - 1, -1, -1):
            t, idx, v = queries[i]
            if t == 0:
                if idx not in unvis_r: continue
                ans += v * (len(unvis_c))
                unvis_r.remove(idx)
            else:
                if idx not in unvis_c: continue
                ans += v * (len(unvis_r))
                unvis_c.remove(idx)
        return ans
        # print(mat)
        # return sum([sum(x) for x in mat])




so = Solution()

print(so.matrixSumQueries(8,
[[0,6,30094],[0,7,99382],[1,2,18599],[1,3,49292],[1,0,81549],[1,1,38280],[0,0,19405],[0,4,30065],[1,4,60826],[1,5,9241],[0,5,33729],[0,1,41456],[0,2,62692],[0,3,30807],[1,7,70613],[1,6,9506],[0,5,39344],[1,0,44658],[1,1,56485],[1,2,48112],[0,6,43384]]))  # 23
print(so.matrixSumQueries(n = 3, queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]]))  # 23

print(so.matrixSumQueries(n = 3, queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]))  # 17




