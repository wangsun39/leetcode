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


from leetcode.allcode.competition.mypackage import *

from functools import lru_cache
from leetcode.allcode.competition.mypackage import *
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


    def maximumMinutes1(self, grid: List[List[int]]) -> int:
        # 2023/6/23  BFS + 二分
        r, c = len(grid), len(grid[0])
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        dq1 = deque()
        t = [[inf] * c for _ in range(r)]  # 火烧到的最早时间
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    dq1.append([i, j])
        cur = 1
        dq2 = deque()
        while dq1:
            while dq1:
                x, y = dq1.popleft()
                for u, v in dir:
                    x1, y1 = x + u, y + v
                    if 0 <= x1 < r and 0 <= y1 < c and grid[x1][y1] == 0 and t[x1][y1] == inf:
                        t[x1][y1] = cur
                        dq2.append([x1, y1])
            cur += 1
            dq1, dq2 = dq2, deque()

        dq1, dq2 = deque([[0, 0]]), deque()
        arr = [[inf] * c for _ in range(r)]  # 记录人到达的最早时间
        arr[0][0] = 0
        cur = 1
        while dq1:
            while dq1:
                x, y = dq1.popleft()
                for x1, y1 in dir:
                    u, v = x + x1, y + y1
                    if 0 <= u < r and 0 <= v < c and grid[u][v] == 0 and arr[u][v] == inf:
                        if u == r - 1 and v == r - 1:
                            if cur > t[u][v]:
                                continue  # 已烧到
                        elif cur >= t[u][v]: continue  # 已烧到
                        arr[u][v] = cur
                        dq2.append([u, v])
            cur += 1
            dq1, dq2 = dq2, deque()
        if arr[-1][-1] == inf:
            return -1
        if t[-1][-1] == inf:
            return 10 ** 9

        def check(val):  # 判断提前val时间，能否完成
            dq1, dq2 = deque([[0, 0]]), deque()
            vis = [[0] * c for _ in range(r)]  # 记录人是否到达过
            vis[0][0] = 1
            cur = 1
            while dq1:
                while dq1:
                    x, y = dq1.popleft()
                    for x1, y1 in dir:
                        u, v = x + x1, y + y1
                        if 0 <= u < r and 0 <= v < c and grid[u][v] == 0 and vis[u][v] == 0:
                            if u == r - 1 and v == c - 1 and t[u][v] - arr[u][v] >= val:
                                return True
                            if t[u][v] - arr[u][v] > val:
                                dq2.append([u, v])
                            vis[u][v] = 1

                cur += 1
                dq1, dq2 = dq2, deque()
            return False
        lo, hi = 0, r * c
        while lo < hi - 1:
            mid = (lo + hi) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid
        return lo

so = Solution()
print(so.maximumMinutes(grid = [[0,0,0,0,0],[0,2,0,2,0],[0,2,0,2,0],[0,2,1,2,0],[0,2,2,2,0],[0,0,0,0,0]]))
print(so.maximumMinutes([[0,0,2,2,1,1,0,2,1,1,2,2,0,2,2,1,2,0,1,2,2,0,1,2,2,1,2,2],[2,2,2,1,1,2,2,1,2,0,1,1,1,2,2,1,1,0,2,2,2,0,1,0,1,2,2,2],[0,0,1,1,0,1,2,0,1,1,1,1,0,2,0,2,0,2,1,1,0,2,1,2,2,2,1,2],[2,2,0,0,0,0,1,0,1,0,2,0,1,0,2,0,0,1,2,1,0,1,1,1,2,0,2,0],[2,2,1,1,1,1,1,0,0,0,0,2,0,1,1,1,1,2,0,2,1,1,2,0,2,0,2,0],[0,1,0,1,2,2,2,0,2,0,2,2,1,2,0,0,1,0,2,0,2,0,1,2,2,0,2,0],[1,0,2,2,2,0,2,0,2,0,2,0,1,0,2,2,0,2,1,1,1,0,1,0,1,1,0,0],[0,1,2,0,1,0,1,0,2,1,2,0,1,1,1,1,0,1,1,0,0,2,0,1,0,1,0,2],[2,1,1,0,1,1,2,2,1,2,2,1,0,1,0,0,0,2,1,0,2,2,1,2,1,2,0,1],[1,1,2,0,2,2,1,2,0,2,1,1,0,0,0,2,2,2,2,1,2,2,0,2,1,1,2,0],[2,1,2,2,0,0,1,0,1,2,1,0,1,0,2,0,0,1,1,0,2,0,2,0,1,2,2,0],[1,0,1,1,0,0,0,0,0,1,0,2,0,2,1,2,1,1,0,1,0,0,2,1,2,1,0,2],[2,0,1,0,2,0,1,0,2,0,2,1,2,0,2,2,2,1,0,2,1,0,1,2,1,0,1,1],[0,2,2,1,0,2,1,0,1,2,2,1,2,2,1,2,0,1,2,2,0,2,1,0,2,1,0,0],[0,2,2,2,1,2,1,0,0,2,2,0,1,0,2,1,0,0,2,1,1,1,2,1,2,1,0,1],[2,2,2,1,1,1,1,0,2,2,2,1,0,0,2,2,0,0,1,1,0,0,2,1,2,1,2,2],[2,1,2,1,1,1,0,2,1,0,1,1,2,1,0,0,1,1,2,1,2,2,1,2,0,2,0,0]]))  # -1
print(so.maximumMinutes([[0,2,0,0,1],[0,2,0,2,2],[0,2,0,0,0],[0,0,2,2,0],[0,0,0,0,0]])) # 0
print(so.maximumMinutes(grid = [[0,0,0,0],[0,1,2,0],[0,2,0,0]]))
print(so.maximumMinutes(grid = [[0,0,0],[2,2,0],[1,2,0]]))



