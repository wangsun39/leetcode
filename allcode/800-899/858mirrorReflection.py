# 有一个特殊的正方形房间，每面墙上都有一面镜子。除西南角以外，每个角落都放有一个接受器，编号为 0， 1，以及 2。
#
# 正方形房间的墙壁长度为 p，一束激光从西南角射出，首先会与东墙相遇，入射点到接收器 0 的距离为 q 。
#
# 返回光线最先遇到的接收器的编号（保证光线最终会遇到一个接收器）。
#
#
# 示例 1：
#
#
# 输入：p = 2, q = 1
# 输出：2
# 解释：这条光线在第一次被反射回左边的墙时就遇到了接收器 2 。
# 示例 2：
#
# 输入：p = 3, q = 1
# 输入：1
#
#
# 提示：
#
# 1 <= q <= p <= 1000
import math

from leetcode.allcode.competition.mypackage import *

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        # 根据光的放射原理，可以考虑突破盒子的上方边界，也就是只有两侧的镜子，光一直其间在反射
        # 看光先到达左侧的某个p的倍数点，还是右侧的某个p的倍数点
        # 实际就是看p和q的最小公倍数l，
        # 看l是q的多少倍：t=l/q 如果t是偶数就先在左侧与p的倍数点相遇，否则就先在右侧与p的倍数点相遇
        # 再根据l是p的多少倍l/p，判断是在上面点相遇还是下面点相遇

        # 考虑1或3到达的次数
        l = math.lcm(p, q)
        t = l // q  # t1 应该是个奇数
        if t & 1 == 0:  # 如果t1 是偶数，说明先到达点2
            return 2
        if (l // p) & 1: # 奇数个方块
            return 1
        return 0


so = Solution()

print(so.mirrorReflection(p = 3, q = 1))
print(so.mirrorReflection(p = 2, q = 1))


