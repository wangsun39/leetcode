# 有一个 m x n 的二元网格 grid ，其中 1 表示砖块，0 表示空白。砖块 稳定（不会掉落）的前提是：
#
# 一块砖直接连接到网格的顶部，或者
# 至少有一块相邻（4 个方向之一）砖块 稳定 不会掉落时
# 给你一个数组 hits ，这是需要依次消除砖块的位置。每当消除 hits[i] = (rowi, coli) 位置上的砖块时，对应位置的砖块（若存在）会消失，然后其他的砖块可能因为这一消除操作而 掉落 。一旦砖块掉落，它会 立即 从网格 grid 中消失（即，它不会落在其他稳定的砖块上）。
#
# 返回一个数组 result ，其中 result[i] 表示第 i 次消除操作对应掉落的砖块数目。
#
# 注意，消除可能指向是没有砖块的空白位置，如果发生这种情况，则没有砖块掉落。
#
#
#
# 示例 1：
#
# 输入：grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
# 输出：[2]
# 解释：网格开始为：
# [[1,0,0,0]，
#  [1,1,1,0]]
# 消除 (1,0) 处加粗的砖块，得到网格：
# [[1,0,0,0]
#  [0,1,1,0]]
# 两个加粗的砖不再稳定，因为它们不再与顶部相连，也不再与另一个稳定的砖相邻，因此它们将掉落。得到网格：
# [[1,0,0,0],
#  [0,0,0,0]]
# 因此，结果为 [2] 。
# 示例 2：
#
# 输入：grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]
# 输出：[0,0]
# 解释：网格开始为：
# [[1,0,0,0],
#  [1,1,0,0]]
# 消除 (1,1) 处加粗的砖块，得到网格：
# [[1,0,0,0],
#  [1,0,0,0]]
# 剩下的砖都很稳定，所以不会掉落。网格保持不变：
# [[1,0,0,0],
#  [1,0,0,0]]
# 接下来消除 (1,0) 处加粗的砖块，得到网格：
# [[1,0,0,0],
#  [0,0,0,0]]
# 剩下的砖块仍然是稳定的，所以不会有砖块掉落。
# 因此，结果为 [0,0] 。
#
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# grid[i][j] 为 0 或 1
# 1 <= hits.length <= 4 * 104
# hits[i].length == 2
# 0 <= xi <= m - 1
# 0 <= yi <= n - 1
# 所有 (xi, yi) 互不相同

from leetcode.allcode.competition.mypackage import *

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        r, c = len(grid), len(grid[0])
        n = r * c
        fa = list(range(n))
        grid0 = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                grid0[i][j] = grid[i][j]

        def find(x):
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]

        def union(x, y):
            # 用小的数作代表元，这步很关键
            if find(x) < find(y):
                fa[find(y)] = find(x)
            else:
                fa[find(x)] = find(y)

        def dfs(i, j):
            cnt = 1
            vis.add(tuple([i, j]))
            for dx, dy in dir:
                x, y = i + dx, j + dy
                if 0 <= x < r and 0 <= y < c and grid[x][y] and find(x * c + y) >= c and (x, y) not in vis:
                    # union(i * c + j, x * c + j)
                    cnt += dfs(x, y)
            return cnt

        for x, y in hits:
            grid[x][y] = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0: continue
                for dx, dy in dir:
                    x, y = i + dx, j + dy
                    if 0 <= x < r and 0 <= y < c and grid[x][y]:
                        union(x * c + y, i * c + j)
        ans = []
        for i, j in hits[::-1]:
            if grid0[i][j] == 0:
                ans.insert(0, 0)
                continue
            fij = find(i * c + j)
            l1 = []  # 存放不稳定的岛
            l2 = []  # 存放稳定的岛
            for dx, dy in dir:
                x, y = i + dx, j + dy
                if 0 <= x < r and 0 <= y < c and grid[x][y]:
                    fxy = find(x * c + y)
                    if fxy < c:
                        l2.append([x, y])
                    else:
                        l1.append([x, y])

            grid[i][j] = 1
            if len(l2):
                union(i * c + j, l2[0][0] * c + l2[0][1])  # 将(i,j)置为稳定
            if len(l1) == 0:
                # 周围已经都是稳定的岛了
                ans.insert(0, 0)
                continue
            if len(l2) == 0 and fij >= c:
                # 周围都没有稳定的岛了
                ans.insert(0, 0)
                for x, y in l1:
                    union(x * c + y, i * c + j)
                continue

            # 不稳定的岛，都是因为这步hit产生的
            vis = set()
            cnt = 0
            for x, y in l1:
                if find(x * c + y) < c: continue
                cnt += dfs(x, y)
                union(x * c + y, i * c + j)  # 合并到(i,j) 因为(i,j)已经稳定了
            ans.insert(0, cnt)

        return ans


so = Solution()
print(so.hitBricks(grid = [[1,1,1],[1,1,1],[1,1,1]], hits = [[2,0],[2,1],[2,2],[1,0],[1,1],[1,2],[0,0],[0,1],[0,2]]))
print(so.hitBricks(grid = [[0,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1],[0,0,0,1,0,0,1,1,1],[0,0,1,1,0,1,1,1,0],[0,0,0,0,0,1,1,1,1],[0,0,0,0,0,0,0,1,0]], hits = [[1,8],[2,1],[1,4],[3,0],[3,4],[0,7],[1,6],[0,8],[2,5],[3,2],[2,0],[0,2],[0,5],[0,1],[4,8],[3,7],[0,6],[5,7],[5,3],[2,6],[2,2],[5,8],[2,8],[4,0],[3,3],[1,1],[0,0],[4,7],[0,3],[2,4],[3,1],[1,0],[5,2],[3,8],[4,2],[5,0],[1,2],[1,7],[3,6],[4,1],[5,6],[0,4],[5,5],[5,4],[1,5],[4,4],[3,5],[4,6],[2,3],[2,7]]))
print(so.hitBricks(grid = [[1,0,1],[1,1,1]], hits = [[0,0],[0,2],[1,1]]))
print(so.hitBricks(grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]))

