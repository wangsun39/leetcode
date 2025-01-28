# 有 n名工人。给定两个数组quality和wage，其中，quality[i]表示第i名工人的工作质量，其最低期望工资为wage[i]。
#
# 现在我们想雇佣k名工人组成一个工资组。在雇佣一组 k名工人时，我们必须按照下述规则向他们支付工资：
#
# 对工资组中的每名工人，应当按其工作质量与同组其他工人的工作质量的比例来支付工资。
# 工资组中的每名工人至少应当得到他们的最低期望工资。
# 给定整数 k ，返回 组成满足上述条件的付费群体所需的最小金额。在实际答案的10-5以内的答案将被接受。。
#
#
#
# 示例 1：
#
# 输入： quality = [10,20,5], wage = [70,50,30], k = 2
# 输出： 105.00000
# 解释： 我们向 0 号工人支付 70，向 2 号工人支付 35。
# 示例 2：
#
# 输入： quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
# 输出： 30.66667
# 解释： 我们向 0 号工人支付 4，向 2 号和 3 号分别支付 13.33333。
#
#
# 提示：
#
# n == quality.length == wage.length
# 1 <= k <= n <= 104
# 1 <= quality[i], wage[i] <= 104

from typing import List
import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        wq = [[wage[i] / quality[i], i] for i in range(n)]
        wq.sort()
        dq, s = [], 0
        for i in range(k):
            heapq.heappush(dq, -quality[wq[i][1]])
            s += quality[wq[i][1]]
        ans = s * wq[k - 1][0]
        for i in range(k, n):
            if -quality[wq[i][1]] > dq[0]:
                top = heapq.heappop(dq)
                heapq.heappush(dq, -quality[wq[i][1]])
                s += (quality[wq[i][1]] + top)
                ans = min(ans, s * wq[i][0])
        return ans

so = Solution()

print(so.mincostToHireWorkers( quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3))
print(so.mincostToHireWorkers( quality = [10,20,5], wage = [70,50,30], k = 2))


