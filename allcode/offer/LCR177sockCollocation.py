# 整数数组 sockets 记录了一个袜子礼盒的颜色分布情况，其中 sockets[i] 表示该袜子的颜色编号。礼盒中除了一款撞色搭配的袜子，每种颜色的袜子均有两只。请设计一个程序，在时间复杂度 O(n)，空间复杂度O(1) 内找到这双撞色搭配袜子的两个颜色编号。
#
#
#
# 示例 1：
#
# 输入：sockets = [4, 5, 2, 4, 6, 6]
# 输出：[2,5] 或 [5,2]
# 示例 2：
#
# 输入：sockets = [1, 2, 4, 1, 4, 3, 12, 3]
# 输出：[2,12] 或 [12,2]
#
#
# 提示：
#
# 2 <= sockets.length <= 10000

from leetcode.allcode.competition.mypackage import *

class Solution:
    def sockCollocation(self, sockets: List[int]) -> List[int]:
        v = reduce(lambda x, y: x ^ y, sockets)
        d = v & -v  # 取第一个非0位
        nums1, nums2 = [], []
        for x in sockets:
            if x & d:
                nums1.append(x)
            else:
                nums2.append(x)
        v1 = reduce(lambda x, y: x ^ y, nums1)
        v2 = reduce(lambda x, y: x ^ y, nums2)
        return [v1, v2]



so = Solution()
print(so.sockCollocation([4, 5, 2, 4, 6, 6]))




