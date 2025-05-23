# 给你一个整数数组 distance 。
#
# 从 X-Y 平面上的点 (0,0) 开始，先向北移动 distance[0] 米，然后向西移动 distance[1] 米，向南移动 distance[2] 米，向东移动 distance[3] 米，持续移动。也就是说，每次移动后你的方位会发生逆时针变化。
#
# 判断你所经过的路径是否相交。如果相交，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
#
# 输入：distance = [2,1,1,2]
# 输出：true
# 示例 2：
#
#
# 输入：distance = [1,2,3,4]
# 输出：false
# 示例 3：
#
#
# 输入：distance = [1,1,1,1]
# 输出：true
#
#
# 提示：
#
# 1 <= distance.length <= 105
# 1 <= distance[i] <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        n = len(distance)
        if n <= 3: return False
        for i in range(3, n):
            if distance[i] >= distance[i - 2] and distance[i - 1] <= distance[i - 3]:
                return True
            if i >= 4 and distance[i - 3] == distance[i - 1] and distance[i] + distance[i - 4] >= distance[i - 2]:
                return True
            if i >= 5 and distance[i - 5] + distance[i - 1] >= distance[i - 3] and distance[i - 1] <= distance[i - 3] and distance[i - 4] + distance[i] >= distance[i - 2] and distance[i - 4] < distance[i - 2]:
                return True
        return False

so = Solution()
print(so.isSelfCrossing(distance = [1,1,2,2,3,3,4,4,10,4,4,3,3,2,2,1,1]))
print(so.isSelfCrossing(distance = [2,1,1,2]))



