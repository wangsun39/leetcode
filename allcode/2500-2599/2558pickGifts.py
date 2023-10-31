# 给你一个整数数组 gifts ，表示各堆礼物的数量。每一秒，你需要执行以下操作：
#
# 选择礼物数量最多的那一堆。
# 如果不止一堆都符合礼物数量最多，从中选择任一堆即可。
# 选中的那一堆留下平方根数量的礼物（向下取整），取走其他的礼物。
# 返回在 k 秒后剩下的礼物数量。
#
#
#
# 示例 1：
#
# 输入：gifts = [25,64,9,4,100], k = 4
# 输出：29
# 解释：
# 按下述方式取走礼物：
# - 在第一秒，选中最后一堆，剩下 10 个礼物。
# - 接着第二秒选中第二堆礼物，剩下 8 个礼物。
# - 然后选中第一堆礼物，剩下 5 个礼物。
# - 最后，再次选中最后一堆礼物，剩下 3 个礼物。
# 最后剩下的礼物数量分别是 [5,8,9,4,3] ，所以，剩下礼物的总数量是 29 。
# 示例 2：
#
# 输入：gifts = [1,1,1,1], k = 4
# 输出：4
# 解释：
# 在本例中，不管选中哪一堆礼物，都必须剩下 1 个礼物。
# 也就是说，你无法获取任一堆中的礼物。
# 所以，剩下礼物的总数量是 4 。
#
#
# 提示：
#
# 1 <= gifts.length <= 103
# 1 <= gifts[i] <= 109
# 1 <= k <= 103

import heapq
from leetcode.allcode.competition.mypackage import *

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        q = []
        heapify(q)
        for g in gifts:
            heappush(q, -g)
        while k > 0:
            x = int((-heappop(q)) ** 0.5)
            heappush(q, -x)
            k -= 1
        return -sum(q)


so = Solution()
print(so.pickGifts(gifts = [25,64,9,4,100], k = 4))
print(so.pickGifts(gifts = [1,1,1,1], k = 4))



