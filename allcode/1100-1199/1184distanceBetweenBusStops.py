# 环形公交路线上有n个站，按次序从0到n - 1进行编号。我们已知每一对相邻公交站之间的距离，distance[i]表示编号为i的车站和编号为(i + 1) % n的车站之间的距离。
#
# 环线上的公交车都可以按顺时针和逆时针的方向行驶。
#
# 返回乘客从出发点start到目的地destination之间的最短距离。
#
#
#
# 示例 1：
#
#
#
# 输入：distance = [1,2,3,4], start = 0, destination = 1
# 输出：1
# 解释：公交站 0 和 1 之间的距离是 1 或 9，最小值是 1。
#
#
# 示例 2：
#
#
#
# 输入：distance = [1,2,3,4], start = 0, destination = 2
# 输出：3
# 解释：公交站 0 和 2 之间的距离是 3 或 7，最小值是 3。
#
#
# 示例 3：
#
#
#
# 输入：distance = [1,2,3,4], start = 0, destination = 3
# 输出：4
# 解释：公交站 0 和 3 之间的距离是 6 或 4，最小值是 4。
#


from leetcode.allcode.competition.mypackage import *
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if destination < start: start, destination = destination, start
        s1, s = 0, sum(distance)
        for i in range(start, destination):
            s1 += distance[i]
        return min(s1, s - s1)



obj = Solution()
print(obj.distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 1))
print(obj.distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 3))

