# 给你一个二维字符网格数组 grid ，大小为 m x n ，你需要检查 grid 中是否存在 相同值 形成的环。
#
# 一个环是一条开始和结束于同一个格子的长度 大于等于 4 的路径。对于一个给定的格子，你可以移动到它上、下、左、右四个方向相邻的格子之一，可以移动的前提是这两个格子有 相同的值 。
#
# 同时，你也不能回到上一次移动时所在的格子。比方说，环  (1, 1) -> (1, 2) -> (1, 1) 是不合法的，因为从 (1, 2) 移动到 (1, 1) 回到了上一次移动时的格子。
#
# 如果 grid 中有相同值形成的环，请你返回 true ，否则返回 false 。
#
#
#
# 示例 1：
#
# 
#
# 输入：grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
# 输出：true
# 解释：如下图所示，有 2 个用不同颜色标出来的环：
#
# 示例 2：
#
#
#
# 输入：grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
# 输出：true
# 解释：如下图所示，只有高亮所示的一个合法环：
#
# 示例 3：
#
#
#
# 输入：grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
# 输出：false
#
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 1 <= m <= 500
# 1 <= n <= 500
# grid 只包含小写英文字母。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        r, c = len(grid), len(grid[0])
        g = defaultdict(list)
        for i in range(r):
            for j in range(c):
                if i < r - 1:
                    if grid[i][j] == grid[i + 1][j]:
                        g[i * c + j].append((i + 1) * c + j)
                        g[(i + 1) * c + j].append(i * c + j)
                if j < c - 1:
                    if grid[i][j] == grid[i][j + 1]:
                        g[i * c + j].append((i * c + j + 1))
                        g[i * c + j + 1].append((i * c + j))
        vis = [0] * r * c
        vis2 = [0] * r * c

        def dfs(x, fa):
            vis[x] = 1
            vis2[x] = 1
            for y in g[x]:
                if y == fa: continue
                if vis[y]:
                    return True
                if dfs(y, x):
                    return True
            vis[x] = 0
            return False
        for i in range(r * c):
            if not vis2[i] and dfs(i, -1):
                return True
        return False



so = Solution()
print(so.containsCycle(grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]))
print(so.containsCycle(grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]))
print(so.containsCycle(grid = [["a","b","b"],["b","z","b"],["b","b","a"]]))




