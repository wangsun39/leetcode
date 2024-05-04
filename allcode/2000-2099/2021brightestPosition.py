# 一条街上有很多的路灯，路灯的坐标由数组 lights 的形式给出。 每个 lights[i] = [positioni, rangei] 代表坐标为 positioni 的路灯照亮的范围为 [positioni - rangei, positioni + rangei] （包括顶点）。
#
# 位置 p 的亮度由能够照到 p的路灯的数量来决定的。
#
# 给出 lights, 返回最亮的位置 。如果有很多，返回坐标最小的。
#
#
#
# 示例 1:
#
#
# 输入: lights = [[-3,2],[1,2],[3,3]]
# 输出: -1
# 解释:
# 第一个路灯照亮的范围是[(-3) - 2, (-3) + 2] = [-5, -1].
# 第二个路灯照亮的范围是 [1 - 2, 1 + 2] = [-1, 3].
# 第三个路灯照亮的范围是 [3 - 3, 3 + 3] = [0, 6].
#
# 坐标-1被第一个和第二个路灯照亮，亮度为2
# 坐标0，1，2都被第二个和第三个路灯照亮，亮度为2.
# 对于以上坐标，-1最小，所以返回-1
# 示例 2：
#
# 输入: lights = [[1,0],[0,1]]
# 输出: 1
# 示例 3：
#
# 输入: lights = [[1,2]]
# 输出: -1
#
#
# 提示:
#
# 1 <= lights.length <= 105
# lights[i].length == 2
# -108 <= positioni <= 108
# 0 <= rangei <= 108

from leetcode.allcode.competition.mypackage import *

class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        diff = defaultdict(int)
        for x, r in lights:
            diff[x - r] += 1
            diff[x + r + 1] -= 1
        diff = sorted([k, v] for k, v in diff.items())
        cur = 0
        mx = -inf
        ans = -inf
        for k, v in diff:
            cur += v
            if cur > mx:
                mx = cur
                ans = k

        return ans



so = Solution()
print(so.brightestPosition([[-3,2],[1,2],[3,3]]))
print(so.brightestPosition(lights = [[1,0],[0,1]]))
print(so.brightestPosition([[1,2]]))




