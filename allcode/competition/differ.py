
from leetcode.allcode.competition.mypackage import *

# 二维前缀和
# https://leetcode.cn/circle/discuss/UUuRex/

# 二维差分
# https://leetcode.cn/problems/stamping-the-grid/solutions/1199642/wu-nao-zuo-fa-er-wei-qian-zhui-he-er-wei-zwiu

# 差分
# 差分数组求前缀和得到原数组
# 前缀和数组求差分得到原数组

class Solution:

    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # 二维差分模板
        diff = [[0] * (n + 2) for _ in range(n + 2)]
        for r1, c1, r2, c2 in queries:
            diff[r1 + 1][c1 + 1] += 1
            diff[r1 + 1][c2 + 2] -= 1
            diff[r2 + 2][c1 + 1] -= 1
            diff[r2 + 2][c2 + 2] += 1

        # 用二维前缀和复原（原地修改）
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                diff[i][j] += diff[i][j - 1] + diff[i - 1][j] - diff[i - 1][j - 1]
        # 保留中间 n*n 的部分，即为答案
        diff = diff[1:-1]
        for i, row in enumerate(diff):
            diff[i] = row[1:-1]
        return diff



    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        r, c = len(grid), len(grid[0])

        # 1. 计算 grid 的二维前缀和
        s = [[0] * (c + 1) for _ in range(r + 1)]
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + v

        # 2. 计算任意矩形区域和
        def sumRegion(row1: int, col1: int, row2: int, col2: int) -> int:
            return s[row2 + 1][col2 + 1] - s[row1][col2 + 1] - s[row2 + 1][col1] + s[row1][col1]



so = Solution()




