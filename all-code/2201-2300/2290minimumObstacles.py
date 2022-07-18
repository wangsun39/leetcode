# 给你一个下标从 0 开始的二维整数数组 grid ，数组大小为 m x n 。每个单元格都是两个值之一：
#
# 0 表示一个 空 单元格，
# 1 表示一个可以移除的 障碍物 。
# 你可以向上、下、左、右移动，从一个空单元格移动到另一个空单元格。
#
# 现在你需要从左上角 (0, 0) 移动到右下角 (m - 1, n - 1) ，返回需要移除的障碍物的 最小 数目。
#
#  
#
# 示例 1：
#
#
#
# 输入：grid = [[0,1,1],[1,1,0],[1,1,0]]
# 输出：2
# 解释：可以移除位于 (0, 1) 和 (0, 2) 的障碍物来创建从 (0, 0) 到 (2, 2) 的路径。
# 可以证明我们至少需要移除两个障碍物，所以返回 2 。
# 注意，可能存在其他方式来移除 2 个障碍物，创建出可行的路径。
# 示例 2：
#
#
#
# 输入：grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
# 输出：0
# 解释：不移除任何障碍物就能从 (0, 0) 到 (2, 4) ，所以返回 0 。
#  
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 105
# 2 <= m * n <= 105
# grid[i][j] 为 0 或 1
# grid[0][0] == grid[m - 1][n - 1] == 0


from typing import List
from collections import deque
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)


import bisect
# bisect_right：
# 若序列a中存在与x相同的元素，则返回x相等元素右侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x左侧距离最近元素插入点的索引位置
# pos = bisect.bisect_right(left, tail)
# bisect_left：
# 若序列a中存在与x相同的元素，则返回x相等元素左侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x右侧距离最近元素插入点的索引位置

# Map = [['U' for _ in range(n)] for _ in range(m)]

from functools import lru_cache
from typing import List
# @lru_cache(None)

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dp = [[1 for _ in range(col)] for _ in range(row)]
        # ans = 0
        finish = set()
        # if grid[0][0] == 1:
        #     ans += 1
        finish.add((0, 0))
        cur, next = set(), set()
        dp[0][0] = 0
        def dfs(x, y):
            dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for dir in dirs:
                if 0 <= x + dir[0] < row and 0 <= y + dir[1] < col:
                    if (x + dir[0], y + dir[1]) in finish:
                        continue
                    if (x + dir[0], y + dir[1]) in cur or (x + dir[0], y + dir[1]) in next:
                        continue
                    if grid[x + dir[0]][y + dir[1]] == 0:
                        finish.add((x + dir[0], y + dir[1]))
                        dfs(x + dir[0], y + dir[1])
                    else:
                        next.add((x + dir[0], y + dir[1]))
        ans = 0
        cur.add((0, 0))
        while True:
            for point in cur:
                dfs(point[0], point[1])
            # print(finish)
            # print(next)
            if (row - 1, col - 1) in finish:
                return ans
            for p in next:
                grid[p[0]][p[1]] = 0
            print(grid)
            ans += 1
            cur = next
            next = set()


so = Solution()
print(so.minimumObstacles([[0,1,1],[1,1,0],[1,1,0]]))
print(so.minimumObstacles([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]))




