# 字母迷宫游戏初始界面记作 m x n 二维字符串数组 grid，请判断玩家是否能在 grid 中找到目标单词 target。
# 注意：寻找单词时 必须 按照字母顺序，通过水平或垂直方向相邻的单元格内的字母构成，同时，同一个单元格内的字母 不允许被重复使用 。
#
#
#
#
#
#
#
# 示例 1：
#
# 输入：grid = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], target = "ABCCED"
# 输出：true
# 示例 2：
#
# 输入：grid = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], target = "SEE"
# 输出：true
# 示例 3：
#
# 输入：grid = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], target = "ABCB"
# 输出：false
#
#
# 提示：
#
# m == grid.length
# n = grid[i].length
# 1 <= m, n <= 6
# 1 <= target.length <= 15
# grid 和 target 仅由大小写英文字母组成
#
#
# 注意：本题与主站 79 题相同： https://leetcode-cn.com/problems/word-search/

from leetcode.allcode.competition.mypackage import *

class Solution:
    def wordPuzzle(self, grid: List[List[str]], target: str) -> bool:
        r, c = len(grid), len(grid[0])
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        n = len(target)

        vis = set()

        def dfs(i, j, k): # 在grid的i行，j列，匹配target[k]
            if grid[i][j] != target[k]: return False
            if k == n - 1: return True
            vis.add((i, j))
            for x, y in dir:
                u, v = i + x, j + y
                if 0 <= u < r and 0 <= v < c and (u, v) not in vis:
                    if dfs(u, v, k + 1): return True
            vis.remove((i, j))
            return False

        for i in range(r):
            for j in range(c):
                if dfs(i, j, 0):
                    return True
        return False

so = Solution()
print(so.wordPuzzle(grid = [["a","a"]], target = "aaa"))
print(so.wordPuzzle(grid = [["a"]], target = "a"))
print(so.wordPuzzle(grid = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], target = "ABCCED"))




