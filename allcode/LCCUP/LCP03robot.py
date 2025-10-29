# 力扣团队买了一个可编程机器人，机器人初始位置在原点(0, 0)。小伙伴事先给机器人输入一串指令command，机器人就会无限循环这条指令的步骤进行移动。指令有两种：
#
# U: 向y轴正方向移动一格
# R: 向x轴正方向移动一格。
# 不幸的是，在 xy 平面上还有一些障碍物，他们的坐标用obstacles表示。机器人一旦碰到障碍物就会被损毁。
#
# 给定终点坐标(x, y)，返回机器人能否完好地到达终点。如果能，返回true；否则返回false。
#
#
#
# 示例 1：
#
# 输入：command = "URR", obstacles = [], x = 3, y = 2
# 输出：true
# 解释：U(0, 1) -> R(1, 1) -> R(2, 1) -> U(2, 2) -> R(3, 2)。
# 示例 2：
#
# 输入：command = "URR", obstacles = [[2, 2]], x = 3, y = 2
# 输出：false
# 解释：机器人在到达终点前会碰到(2, 2)的障碍物。
# 示例 3：
#
# 输入：command = "URR", obstacles = [[4, 2]], x = 3, y = 2
# 输出：true
# 解释：到达终点后，再碰到障碍物也不影响返回结果。
#
#
# 限制：
#
# 2 <= command的长度 <= 1000
# command由U，R构成，且至少有一个U，至少有一个R
# 0 <= x <= 1e9, 0 <= y <= 1e9
# 0 <= obstacles的长度 <= 1000
# obstacles[i]不为原点或者终点

from leetcode.allcode.competition.mypackage import *

class Solution:
    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:
        n = len(command)
        path = [(0, 0)]
        for i in range(n):
            if command[i] == 'U':
                path.append((path[-1][0], path[-1][1] + 1))
            else:
                path.append((path[-1][0] + 1, path[-1][1]))
        fx, fy = path[-1]
        path = set(path)

        def judge(x, y):
            if fx and fy:
                k = max((x - 1) // fx, (y - 1) // fy)
            elif fx:
                k = (x - 1) // fx
            else:
                k = (y - 1) // fy
            kx, ky = k * fx, k * fy  # 机器人移动k个周期后的位置
            lx, ly = x - kx, y - ky  # 终点相对于第k个周期的位置 的相对位移
            return (lx, ly) in path

        for ox, oy in obstacles:
            if ox > x or oy > y: continue
            if judge(ox, oy):
                return False
        return judge(x, y)




so = Solution()
print(so.robot(command = "URR", obstacles = [[2, 2]], x = 3, y = 2))   # False
print(so.robot(command = "RRRUUU", obstacles = [[3, 0]], x = 3, y = 3))   # False
print(so.robot(command = "URR", obstacles = [[4, 2]], x = 3, y = 2))
print(so.robot(command = "URR", obstacles = [], x = 3, y = 2))




