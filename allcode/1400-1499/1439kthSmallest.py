# 给你一个 m * n 的矩阵 mat，以及一个整数 k ，矩阵中的每一行都以非递减的顺序排列。
#
# 你可以从每一行中选出 1 个元素形成一个数组。返回所有可能数组中的第 k 个 最小 数组和。
#
#
#
# 示例 1：
#
# 输入：mat = [[1,3,11],[2,4,6]], k = 5
# 输出：7
# 解释：从每一行中选出一个元素，前 k 个和最小的数组分别是：
# [1,2], [1,4], [3,2], [3,4], [1,6]。其中第 5 个的和是 7 。
# 示例 2：
#
# 输入：mat = [[1,3,11],[2,4,6]], k = 9
# 输出：17
# 示例 3：
#
# 输入：mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
# 输出：9
# 解释：从每一行中选出一个元素，前 k 个和最小的数组分别是：
# [1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]。其中第 7 个的和是 9 。
# 示例 4：
#
# 输入：mat = [[1,1,10],[2,2,9]], k = 7
# 输出：12
#
#
# 提示：
#
# m == mat.length
# n == mat.length[i]
# 1 <= m, n <= 40
# 1 <= k <= min(200, n ^ m)
# 1 <= mat[i][j] <= 5000
# mat[i] 是一个非递减数组





from leetcode.allcode.competition.mypackage import *
import math
from heapq import *

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        def calc(r1, r2):  # 计算2行，前 k 小的和
            n1, n2 = len(r1), len(r2)
            hq = [[r1[0] + r2[0], 0, 0]]  # 优先队列 [r1[i] + r2[j], i, j]
            heapify(hq)
            vis = {(0, 0)}
            res = []
            while hq:
                s, i, j = heappop(hq)
                res.append(s)
                if len(res) == k:
                    return res
                if i + 1 < n1 and (i + 1, j) not in vis:
                    vis.add((i + 1, j))
                    heappush(hq, [r1[i + 1] + r2[j], i + 1, j])
                if j + 1 < n2 and (i, j + 1) not in vis:
                    vis.add((i, j + 1))
                    heappush(hq, [r1[i] + r2[j + 1], i, j + 1])
            return res

        acc = [0]  # 计算前 i 行的前k个最小和
        for r in mat:
            acc = calc(acc, r)
        return acc[k - 1]


so = Solution()
print(so.kthSmallest(mat = [[1,3,11],[2,4,6]], k = 9))
print(so.kthSmallest(mat = [[1,3,11],[2,4,6]], k = 5))
print(so.kthSmallest(mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7))




