# 在由 1 x 1 方格组成的 n x n 网格 grid 中，每个 1 x 1 方块由 '/'、'\' 或空格构成。这些字符会将方块划分为一些共边的区域。
#
# 给定网格 grid 表示为一个字符串数组，返回 区域的数量 。
#
# 请注意，反斜杠字符是转义的，因此 '\' 用 '\\' 表示。
#
#
#
# 示例 1：
#
#
#
# 输入：grid = [" /","/ "]
# 输出：2
# 示例 2：
#
#
#
# 输入：grid = [" /","  "]
# 输出：1
# 示例 3：
#
#
#
# 输入：grid = ["/\\","\\/"]
# 输出：5
# 解释：回想一下，因为 \ 字符是转义的，所以 "/\\" 表示 /\，而 "\\/" 表示 \/。
#
#
# 提示：
#
# n == grid.length == grid[i].length
# 1 <= n <= 30
# grid[i][j] 是 '/'、'\'、或 ' '

from leetcode.allcode.competition.mypackage import *

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        r, c = len(grid), len(grid[0])
        n = r * c * 4  # 每个格子在细分成4个小格子，上下左右，分别对接4个方向的相邻格子，编号从上方开始依次加1
        fa = list(range(n))
        # fa = {x: x for x in nums}  # 另一种写法，x不连续
        def find(x):
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]
        def union(x, y):
            fa[find(y)] = find(x)

        for i in range(r):
            for j in range(c):
                x = i * c + j
                up, right, down, left = x * 4, x * 4 + 1, x * 4 + 2, x * 4 + 3  # 细分的4个子节点

                # 与相邻节点连起来
                if i & 1 == j & 1:  # 为了减少重复union，可以隔一个位置处理一个节点与其周围节点的关系
                    if i > 0:
                        y = (i - 1) * c + j
                        union(y * 4 + 2, up)
                    if i < r - 1:
                        y = (i + 1) * c + j
                        union(y * 4, down)
                    if j > 0:
                        y = i * c + j - 1
                        union(y * 4 + 1, left)
                    if j < c - 1:
                        y = i * c + j + 1
                        union(y * 4 + 3, right)
                # 内部连接，都需要处理
                if grid[i][j] == ' ':
                    union(up, right)
                    union(right, down)
                    union(down, left)
                if grid[i][j] == '/':
                    union(up, left)
                    union(down, right)
                if grid[i][j] == '\\':
                    union(up, right)
                    union(down, left)
        for i in range(n):
            find(i)
        ans = set()
        for i in range(n):
            ans.add(find(i))
        return len(ans)



so = Solution()
print(so.regionsBySlashes(grid = [" /","/ "]))
print(so.regionsBySlashes(grid = [" /","  "]))
print(so.regionsBySlashes(grid = ["/\\","\\/"]))




