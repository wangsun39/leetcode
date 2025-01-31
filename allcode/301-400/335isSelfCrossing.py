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
        right = [[0, 0], [0, distance[0]]]
        up = [[-distance[1], distance[0]], [0, distance[0]]]
        left = [[-distance[1], distance[0] - distance[2]], [-distance[1], distance[0]]]
        down =  [[-distance[1], distance[0] - distance[2]], [-distance[1] + distance[3], distance[0] - distance[2]]]
        pre = [-distance[1], distance[0] - distance[2]]
        for i, x in enumerate(distance[3:], 3):
            if i % 4 == 0:




so = Solution()
print(so.findItinerary(tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))



