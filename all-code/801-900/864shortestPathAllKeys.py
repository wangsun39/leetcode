# 给定一个二维网格 grid ，其中：
#
# '.' 代表一个空房间
# '#' 代表一堵
# '@' 是起点
# 小写字母代表钥匙
# 大写字母代表锁
# 我们从起点开始出发，一次移动是指向四个基本方向之一行走一个单位空间。我们不能在网格外面行走，也无法穿过一堵墙。如果途经一个钥匙，我们就把它捡起来。除非我们手里有对应的钥匙，否则无法通过锁。
#
# 假设 k 为 钥匙/锁 的个数，且满足 1 <= k <= 6，字母表中的前 k 个字母在网格中都有自己对应的一个小写和一个大写字母。换言之，每个锁有唯一对应的钥匙，每个钥匙也有唯一对应的锁。另外，代表钥匙和锁的字母互为大小写并按字母顺序排列。
#
# 返回获取所有钥匙所需要的移动的最少次数。如果无法获取所有钥匙，返回 -1 。
#
#
#
# 示例 1：
#
#
#
# 输入：grid = ["@.a.#","###.#","b.A.B"]
# 输出：8
# 解释：目标是获得所有钥匙，而不是打开所有锁。
# 示例 2：
#
#
#
# 输入：grid = ["@..aA","..B#.","....b"]
# 输出：6
# 示例 3:
#
#
# 输入: grid = ["@Aa"]
# 输出: -1
#
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 30
# grid[i][j] 只含有 '.', '#', '@', 'a'-'f' 以及 'A'-'F'
# 钥匙的数目范围是 [1, 6]
# 每个钥匙都对应一个 不同 的字母
# 每个钥匙正好打开一个对应的锁

import bisect
import collections
from typing import List

from itertools import accumulate
from cmath import inf
from collections import deque
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        row, col = len(grid), len(grid[0])
        d = {}  # (x, y, mask) => step 最小步数
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def dfs(x, y, mask, step):
            for dir in dirs:
                xx, yy = x + dir[0], y + dir[1]
                if 0 <= xx < row and 0 <= yy < col and grid[xx][yy] != '#':

        for i in row:
            for j in col:
                if grid[i][j] == '@':
                    d[(i, j, 0)] = 0
                    dfs(i, j, 0, 0)



so = Solution()
print(so.shortestSubarray3([1, 2], 4))

