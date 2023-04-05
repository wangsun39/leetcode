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
        def bfs(x0, y0, target):
            q= [(x0, y0, 0)]
            while len(q):
                x, y, mask = q.pop(0)
                for dir in dirs:
                    xx, yy = x + dir[0], y + dir[1]
                    if xx < 0 or xx >= row or yy < 0 or yy >= col or grid[xx][yy] == '#':
                        continue
                    mask1 = mask
                    if grid[xx][yy].islower():
                        mask1 |= (1 << (ord(grid[xx][yy]) - ord('a')))
                        if mask1 == target:
                            return d[(x, y, mask)] + 1
                    elif grid[xx][yy].isupper():
                        if mask & (1 << (ord(grid[xx][yy]) - ord('A'))) == 0:
                            continue
                    if (xx, yy, mask1) in d:
                        continue
                    d[(xx, yy, mask1)] = d[(x, y, mask)] + 1
                    q.append((xx, yy, mask1))
            return -1

        letter = set()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '@':
                    x0, y0 = i, j
                elif grid[i][j].islower():
                    letter.add(grid[i][j])
        target = 0
        for l in letter:
            target |= (1 << (ord(l) - ord('a')))
        d[(x0, y0, 0)] = 0
        return bfs(x0, y0, target)



so = Solution()
print(so.shortestPathAllKeys(["@...a",".###A","b.BCc"]))   # 10
print(so.shortestPathAllKeys(["@.a.#","###.#","b.A.B"]))   # 8
print(so.shortestPathAllKeys(["@..aA","..B#.","....b"]))   # 6
print(so.shortestPathAllKeys(["@Aa"]))   # -1

