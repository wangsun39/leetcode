# 「以扣会友」线下活动所在场地由若干主题空间与走廊组成，场地的地图记作由一维字符串型数组 grid，字符串中仅包含 "0"～"5" 这 6 个字符。地图上每一个字符代表面积为 1 的区域，其中 "0" 表示走廊，其他字符表示主题空间。相同且连续（连续指上、下、左、右四个方向连接）的字符组成同一个主题空间。
#
# 假如整个 grid 区域的外侧均为走廊。请问，不与走廊直接相邻的主题空间的最大面积是多少？如果不存在这样的空间请返回 0。
#
# 示例 1：
#
# 输入：grid = ["110","231","221"]
#
# 输出：1
#
# 解释：4 个主题空间中，只有 1 个不与走廊相邻，面积为 1。image.png
#
# 示例 2：
#
# 输入：grid = ["11111100000","21243101111","21224101221","11111101111"]
#
# 输出：3
#
# 解释：8 个主题空间中，有 5 个不与走廊相邻，面积分别为 3、1、1、1、2，最大面积为 3。image.png
#
# 提示：
#
# 1 <= grid.length <= 500
# 1 <= grid[i].length <= 500
# grid[i][j] 仅可能为 "0"～"5"

from leetcode.allcode.competition.mypackage import *

class Solution:
    def largestArea(self, grid: List[str]) -> int:
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        r, c = len(grid), len(grid[0])
        n = r * c  # n 表示 不能作为主题公园的点
        fa = list(range(n + 1))

        def find(x):
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]

        def union(x, y):
            fa[find(y)] = find(x)

        zeros = []
        for i in range(r):
            for j in range(c):
                x = i * c + j
                if grid[i][j] == '0' or i == 0 or i == r - 1 or j == 0 or j == c - 1:
                    zeros.append([i, j])
                    union(n, x)  # 排除
                    continue
                for dx, dy in dir:
                    u, v = i + dx, j + dy
                    y = u * c + v
                    if 0 <= u < r and 0 <= v < c:
                        if grid[i][j] == grid[u][v]:
                            if find(y) == n:
                                union(n, x)
                            elif find(x) == n:
                                union(n, y)
                            else:
                                union(x, y)
                        elif grid[u][v] == '0':
                            union(n, x)
        for i in range(n):
            find(i)
        counter = Counter(fa)
        ans = 0
        for k, v in counter.items():
            if k != n:
                ans = max(ans, v)
        return ans


so = Solution()
print(so.largestArea(grid = ["111","222","333"]))
print(so.largestArea(grid = ["110","231","221"]))




