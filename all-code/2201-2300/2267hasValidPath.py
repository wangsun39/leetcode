# 一个括号字符串是一个 非空 且只包含 '(' 和 ')' 的字符串。如果下面 任意 条件为 真 ，那么这个括号字符串就是 合法的 。
#
# 字符串是 () 。
# 字符串可以表示为 AB（A 连接 B），A 和 B 都是合法括号序列。
# 字符串可以表示为 (A) ，其中 A 是合法括号序列。
# 给你一个 m x n 的括号网格图矩阵 grid 。网格图中一个 合法括号路径 是满足以下所有条件的一条路径：
#
# 路径开始于左上角格子 (0, 0) 。
# 路径结束于右下角格子 (m - 1, n - 1) 。
# 路径每次只会向 下 或者向 右 移动。
# 路径经过的格子组成的括号字符串是 合法 的。
# 如果网格图中存在一条 合法括号路径 ，请返回 true ，否则返回 false 。
#
#  
#
# 示例 1：
#
#
#
# 输入：grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
# 输出：true
# 解释：上图展示了两条路径，它们都是合法括号字符串路径。
# 第一条路径得到的合法字符串是 "()(())" 。
# 第二条路径得到的合法字符串是 "((()))" 。
# 注意可能有其他的合法括号字符串路径。
# 示例 2：
#
#
#
# 输入：grid = [[")",")"],["(","("]]
# 输出：false
# 解释：两条可行路径分别得到 "))(" 和 ")((" 。由于它们都不是合法括号字符串，我们返回 false 。
#  
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# grid[i][j] 要么是 '(' ，要么是 ')' 。

# Map = [['U' for _ in range(n)] for _ in range(m)]

from typing import List
from collections import deque
# Definition for a binary tree node.
from collections import Counter

from functools import lru_cache
from typing import List
# @lru_cache(None)

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        row, col = len(grid), len(grid[0])

        @lru_cache(None)
        def dfs(i, j, left):
            if grid[i][j] == ')':
                if left <= 0:
                    return False
                left -= 1
            else:
                left += 1
            if i == row - 1 and j == col - 1:
                return left == 0
            if i < row - 1 and dfs(i + 1, j, left):
                return True
            if j < col - 1 and dfs(i, j + 1, left):
                return True
            return False
        return dfs(0, 0, 0)



so = Solution()
print(so.hasValidPath( [["(",")",")","(",")",")",")"]]))
print(so.hasValidPath( [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]))
print(so.hasValidPath( [[")",")"],["(","("]]))




