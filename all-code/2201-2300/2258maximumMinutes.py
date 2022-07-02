# 给你一个下标从 0 开始大小为 m x n 的二维整数数组 grid ，它表示一个网格图。每个格子为下面 3 个值之一：
#
# 0 表示草地。
# 1 表示着火的格子。
# 2 表示一座墙，你跟火都不能通过这个格子。
# 一开始你在最左上角的格子 (0, 0) ，你想要到达最右下角的安全屋格子 (m - 1, n - 1) 。每一分钟，你可以移动到 相邻 的草地格子。每次你移动 之后 ，着火的格子会扩散到所有不是墙的 相邻 格子。
#
# 请你返回你在初始位置可以停留的 最多 分钟数，且停留完这段时间后你还能安全到达安全屋。如果无法实现，请你返回 -1 。如果不管你在初始位置停留多久，你 总是 能到达安全屋，请你返回 109 。
#
# 注意，如果你到达安全屋后，火马上到了安全屋，这视为你能够安全到达安全屋。
#
# 如果两个格子有共同边，那么它们为 相邻 格子。
#
#  
#
# 示例 1：
#
#
#
# 输入：grid = [[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]]
# 输出：3
# 解释：上图展示了你在初始位置停留 3 分钟后的情形。
# 你仍然可以安全到达安全屋。
# 停留超过 3 分钟会让你无法安全到达安全屋。
# 示例 2：
#
#
#
# 输入：grid = [[0,0,0,0],[0,1,2,0],[0,2,0,0]]
# 输出：-1
# 解释：上图展示了你马上开始朝安全屋移动的情形。
# 火会蔓延到你可以移动的所有格子，所以无法安全到达安全屋。
# 所以返回 -1 。
# 示例 3：
#
#
#
# 输入：grid = [[0,0,0],[2,2,0],[1,2,0]]
# 输出：1000000000
# 解释：上图展示了初始网格图。
# 注意，由于火被墙围了起来，所以无论如何你都能安全到达安全屋。
# 所以返回 109 。
#  
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 2 <= m, n <= 300
# 4 <= m * n <= 2 * 104
# grid[i][j] 是 0 ，1 或者 2 。
# grid[0][0] == grid[m - 1][n - 1] == 0


from typing import List
from collections import deque
# Definition for a binary tree node.
from collections import Counter

from functools import lru_cache
from typing import List
from collections import deque
# Definition for a binary tree node.
from collections import Counter
class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[10000 for _ in range(n)] for _ in range(m)]
        queue = [[m - 1, n - 1]]
        dp[m - 1][n - 1] = 0
        dirs = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        while len(queue) > 0:
            [x, y] = queue.pop(0)
            if grid[x][y] == 2:
                continue
            for dir in dirs:
                if 0 <= x + dir[0] < m and 0 <= y + dir[1] < n and grid[x + dir[0]][y + dir[1]] != 2 and dp[x + dir[0]][y + dir[1]] > dp[x][y] + 1:
                    dp[x + dir[0]][y + dir[1]] = dp[x][y] + 1
                    queue.append([x + dir[0], y + dir[1]])
        fireMinTime = 10000
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fireMinTime = min(fireMinTime, dp[i][j])
        print(dp)
        print(fireMinTime)
        if fireMinTime == 10000 and dp[0][0] != 10000:
            return 1000000000
        if fireMinTime < dp[0][0] or dp[0][0] == 10000:
            return -1

        def search(start, step, target):
            queue = [start, '#']
            if dp[start[0]][start[1]] != 1:
                return []
            cur = 2
            while True:
                if queue[0] == '#':
                    queue.pop(0)
                    if cur == step:
                        break
                    queue.append('#')
                    cur += 1
                    continue
                [x, y] = queue.pop(0)
                for dir in dirs:
                    if 0 <= x + dir[0] < m and 0 <= y + dir[1] < n and dp[x + dir[0]][y + dir[1]] == cur:
                        queue.append([x + dir[0], y + dir[1]])
            ans = []
            for [x, y] in queue:
                if grid[x][y] == target:
                    ans.append([x, y])
            return ans

        fireUp = len(search([m - 2, n - 1], fireMinTime, 1)) > 0  #在最短时间内，火从[m - 2, n - 1]到达安全屋
        manUp = [0, 0] in search([m - 2, n - 1], dp[0][0], 0)

        fireLeft = len(search([m - 1, n - 2], fireMinTime, 1)) > 0  #在最短时间内，火从[m - 1, n - 2]到达安全屋
        manLeft = [0, 0] in search([m - 1, n - 2], dp[0][0], 0)

        if (not fireUp and manUp) or (not fireLeft and manLeft):
            return fireMinTime - dp[0][0]

        return fireMinTime - dp[0][0] - 1

so = Solution()
print(so.maximumMinutes(grid = [[0,0,0,0,0],[0,2,0,2,0],[0,2,0,2,0],[0,2,1,2,0],[0,2,2,2,0],[0,0,0,0,0]]))
print(so.maximumMinutes([[0,0,2,2,1,1,0,2,1,1,2,2,0,2,2,1,2,0,1,2,2,0,1,2,2,1,2,2],[2,2,2,1,1,2,2,1,2,0,1,1,1,2,2,1,1,0,2,2,2,0,1,0,1,2,2,2],[0,0,1,1,0,1,2,0,1,1,1,1,0,2,0,2,0,2,1,1,0,2,1,2,2,2,1,2],[2,2,0,0,0,0,1,0,1,0,2,0,1,0,2,0,0,1,2,1,0,1,1,1,2,0,2,0],[2,2,1,1,1,1,1,0,0,0,0,2,0,1,1,1,1,2,0,2,1,1,2,0,2,0,2,0],[0,1,0,1,2,2,2,0,2,0,2,2,1,2,0,0,1,0,2,0,2,0,1,2,2,0,2,0],[1,0,2,2,2,0,2,0,2,0,2,0,1,0,2,2,0,2,1,1,1,0,1,0,1,1,0,0],[0,1,2,0,1,0,1,0,2,1,2,0,1,1,1,1,0,1,1,0,0,2,0,1,0,1,0,2],[2,1,1,0,1,1,2,2,1,2,2,1,0,1,0,0,0,2,1,0,2,2,1,2,1,2,0,1],[1,1,2,0,2,2,1,2,0,2,1,1,0,0,0,2,2,2,2,1,2,2,0,2,1,1,2,0],[2,1,2,2,0,0,1,0,1,2,1,0,1,0,2,0,0,1,1,0,2,0,2,0,1,2,2,0],[1,0,1,1,0,0,0,0,0,1,0,2,0,2,1,2,1,1,0,1,0,0,2,1,2,1,0,2],[2,0,1,0,2,0,1,0,2,0,2,1,2,0,2,2,2,1,0,2,1,0,1,2,1,0,1,1],[0,2,2,1,0,2,1,0,1,2,2,1,2,2,1,2,0,1,2,2,0,2,1,0,2,1,0,0],[0,2,2,2,1,2,1,0,0,2,2,0,1,0,2,1,0,0,2,1,1,1,2,1,2,1,0,1],[2,2,2,1,1,1,1,0,2,2,2,1,0,0,2,2,0,0,1,1,0,0,2,1,2,1,2,2],[2,1,2,1,1,1,0,2,1,0,1,1,2,1,0,0,1,1,2,1,2,2,1,2,0,2,0,0]]))  # -1
print(so.maximumMinutes([[0,2,0,0,1],[0,2,0,2,2],[0,2,0,0,0],[0,0,2,2,0],[0,0,0,0,0]])) # 0
print(so.maximumMinutes(grid = [[0,0,0,0],[0,1,2,0],[0,2,0,0]]))
print(so.maximumMinutes(grid = [[0,0,0],[2,2,0],[1,2,0]]))



