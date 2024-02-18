# 给出矩阵 matrix 和目标值 target，返回元素总和等于目标值的非空子矩阵的数量。
#
# 子矩阵 x1, y1, x2, y2 是满足 x1 <= x <= x2 且 y1 <= y <= y2 的所有单元 matrix[x][y] 的集合。
#
# 如果 (x1, y1, x2, y2) 和 (x1', y1', x2', y2') 两个子矩阵中部分坐标不同（如：x1 != x1'），那么这两个子矩阵也不同。
#
#
#
# 示例 1：
#
#
#
# 输入：matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
# 输出：4
# 解释：四个只含 0 的 1x1 子矩阵。
# 示例 2：
#
# 输入：matrix = [[1,-1],[-1,1]], target = 0
# 输出：5
# 解释：两个 1x2 子矩阵，加上两个 2x1 子矩阵，再加上一个 2x2 子矩阵。
# 示例 3：
#
# 输入：matrix = [[904]], target = 0
# 输出：0
#
#
# 提示：
#
# 1 <= matrix.length <= 100
# 1 <= matrix[0].length <= 100
# -1000 <= matrix[i] <= 1000
# -10^8 <= target <= 10^8

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        r, c = len(matrix), len(matrix[0])
        ans = 0
        for k in range(r):   # 以k行的每个点作为左上角的点
            arr = [0] * c
            for i in range(k, r):   # 以i行为右下角的点
                arr = [arr[j] + matrix[i][j] for j in range(c)]
                s = list(accumulate(arr, initial=0))
                counter = Counter(s)   #统计前缀和的计数
                for j in range(c + 1):
                    counter[s[j]] -= 1  # 只考虑j右侧的格子，要删掉左边的计数
                    ans += counter[s[j] + target]
        return ans


so = Solution()
print(so.numSubmatrixSumTarget(matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0))
print(so.numSubmatrixSumTarget(matrix = [[1,-1],[-1,1]], target = 0))
print(so.numSubmatrixSumTarget(matrix = [[904]], target = 0))




