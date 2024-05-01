# X 轴上有一些机器人和工厂。给你一个整数数组 robot ，其中 robot[i] 是第 i 个机器人的位置。再给你一个二维整数数组 factory ，其中 factory[j] = [positionj, limitj] ，表示第 j 个工厂的位置在 positionj ，且第 j 个工厂最多可以修理 limitj 个机器人。
#
# 每个机器人所在的位置 互不相同 。每个工厂所在的位置也 互不相同 。注意一个机器人可能一开始跟一个工厂在 相同的位置 。
#
# 所有机器人一开始都是坏的，他们会沿着设定的方向一直移动。设定的方向要么是 X 轴的正方向，要么是 X 轴的负方向。当一个机器人经过一个没达到上限的工厂时，这个工厂会维修这个机器人，且机器人停止移动。
#
# 任何时刻，你都可以设置 部分 机器人的移动方向。你的目标是最小化所有机器人总的移动距离。
#
# 请你返回所有机器人移动的最小总距离。测试数据保证所有机器人都可以被维修。
#
# 注意：
#
# 所有机器人移动速度相同。
# 如果两个机器人移动方向相同，它们永远不会碰撞。
# 如果两个机器人迎面相遇，它们也不会碰撞，它们彼此之间会擦肩而过。
# 如果一个机器人经过了一个已经达到上限的工厂，机器人会当作工厂不存在，继续移动。
# 机器人从位置 x 到位置 y 的移动距离为 |y - x| 。
#
#
# 示例 1：
#
#
#
# 输入：robot = [0,4,6], factory = [[2,2],[6,2]]
# 输出：4
# 解释：如上图所示：
# - 第一个机器人从位置 0 沿着正方向移动，在第一个工厂处维修。
# - 第二个机器人从位置 4 沿着负方向移动，在第一个工厂处维修。
# - 第三个机器人在位置 6 被第二个工厂维修，它不需要移动。
# 第一个工厂的维修上限是 2 ，它维修了 2 个机器人。
# 第二个工厂的维修上限是 2 ，它维修了 1 个机器人。
# 总移动距离是 |2 - 0| + |2 - 4| + |6 - 6| = 4 。没有办法得到比 4 更少的总移动距离。
# 示例 2：
#
#
#
# 输入：robot = [1,-1], factory = [[-2,1],[2,1]]
# 输出：2
# 解释：如上图所示：
# - 第一个机器人从位置 1 沿着正方向移动，在第二个工厂处维修。
# - 第二个机器人在位置 -1 沿着负方向移动，在第一个工厂处维修。
# 第一个工厂的维修上限是 1 ，它维修了 1 个机器人。
# 第二个工厂的维修上限是 1 ，它维修了 1 个机器人。
# 总移动距离是 |2 - 1| + |(-2) - (-1)| = 2 。没有办法得到比 2 更少的总移动距离。
#
#
# 提示：
#
# 1 <= robot.length, factory.length <= 100
# factory[j].length == 2
# -109 <= robot[i], positionj <= 109
# 0 <= limitj <= robot.length
# 测试数据保证所有机器人都可以被维修。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        n, m = len(robot), len(factory)
        dp = [[inf] * n for _ in range(m)]
        if factory[0][1]:
            dp[0][0] = abs(robot[0] - factory[0][0])
        for i in range(1, n):
            if i + 1 <= factory[0][1]:
                dp[0][i] = dp[0][i-1] + abs(robot[i] - factory[0][0])
        for i in range(1, m):
            for j in range(n):
                mi = inf
                sm = 0
                for k in range(j, -1, -1):
                    if j - k > factory[i][1]:
                        break
                    mi = min(mi, sm + dp[i - 1][k])
                    sm += abs(robot[k] - factory[i][0])
                if j + 1 <= factory[i][1]:
                    mi = min(mi, sm)
                dp[i][j] = mi
        print(dp)
        return dp[-1][-1]


so = Solution()
print(so.minimumTotalDistance(robot = [-333539942,359275673,89966494,949684497,-733065249,241002388,325009248,403868412,-390719486,-670541382,563735045,119743141,323190444,534058139,-684109467,425503766,761908175], factory = [[-590277115,0],[-80676932,3],[396659814,0],[480747884,9],[118956496,10]]))  # 4412966458
print(so.minimumTotalDistance(robot = [9,11,99,101], factory = [[10,1],[7,1],[14,1],[100,1],[96,1],[103,1]]))  # 6
print(so.minimumTotalDistance(robot = [1,-1], factory = [[-2,1],[2,1]]))  # 2
print(so.minimumTotalDistance(robot = [0,4,6], factory = [[2,2],[6,2]]))  # 4




