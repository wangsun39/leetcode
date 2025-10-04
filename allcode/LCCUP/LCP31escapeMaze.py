# 某解密游戏中，有一个 N*M 的迷宫，迷宫地形会随时间变化而改变，迷宫出口一直位于 (n-1,m-1) 位置。迷宫变化规律记录于 maze 中，maze[i] 表示 i 时刻迷宫的地形状态，"." 表示可通行空地，"#" 表示陷阱。
#
# 地形图初始状态记作 maze[0]，此时小力位于起点 (0,0)。此后每一时刻可选择往上、下、左、右其一方向走一步，或者停留在原地。
#
# 小力背包有以下两个魔法卷轴（卷轴使用一次后消失）：
#
# 临时消除术：将指定位置在下一个时刻变为空地；
# 永久消除术：将指定位置永久变为空地。
# 请判断在迷宫变化结束前（含最后时刻），小力能否在不经过任意陷阱的情况下到达迷宫出口呢？
#
# 注意： 输入数据保证起点和终点在所有时刻均为空地。
#
# 示例 1：
#
# 输入：maze = [[".#.","#.."],["...",".#."],[".##",".#."],["..#",".#."]]
#
# 输出：true
#
# 解释：maze.gif
#
# 示例 2：
#
# 输入：maze = [[".#.","..."],["...","..."]]
#
# 输出：false
#
# 解释：由于时间不够，小力无法到达终点逃出迷宫。
#
# 示例 3：
#
# 输入：maze = [["...","...","..."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."]]
#
# 输出：false
#
# 解释：由于道路不通，小力无法到达终点逃出迷宫。
#
# 提示：
#
# 1 <= maze.length <= 100
# 1 <= maze[i].length, maze[i][j].length <= 50
# maze[i][j] 仅包含 "."、"#"

from leetcode.allcode.competition.mypackage import *

class Solution:
    def escapeMaze(self, maze: List[List[str]]) -> bool:
        n = len(maze)
        if maze[0][0][0] == '#': return False
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        r, c = len(maze[0]), len(maze[0][0])

        @cache
        def dfs(t, px, py, f1, f2):  # t 表示时间， f1,f2分别表示两种消除术是否使用
            if [px, py] == [r - 1, c - 1]:
                return True
            if t >= n - 1:
                return False

            # 先考虑不移动的场景
            if maze[t + 1][px][py] == '.':
                if dfs(t + 1, px, py, f1, f2): return True
            else:
                if not f1:
                    if dfs(t + 1, px, py, f1 ^ 1, f2): return True
                if not f2:
                    for k in range(t + 1, n):
                        if dfs(t + 1, px, py, f1, f2 ^ 1): return True

            # 再考虑移动的场景
            for dx, dy in dir:
                x, y = px + dx, py + dy
                if 0 <= x < r and 0 <= y < c:
                    if maze[t + 1][x][y] == '.':
                        if dfs(t + 1, x, y, f1, f2): return True
                    else:
                        if not f1:
                            if dfs(t + 1, x, y, 1, f2): return True
                        if not f2:
                            for k in range(t + 1, n):
                                if dfs(k, x, y, f1, 1): return True
            return False

        return dfs(0, 0, 0, 0, 0)



so = Solution()
print(so.escapeMaze(maze = [["....","...."],[".#..","#..."],["..#.",".#.."],["...#","..#."],["....",".##."]]))
print(so.escapeMaze(maze = [["...","...","..."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."]]))





