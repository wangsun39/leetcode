# 给定两个整数 n 和 k，以及两个长度为 n 的整数数组 speed 和 efficiency。现有 n 名工程师，编号从 1 到 n。其中 speed[i] 和 efficiency[i] 分别代表第 i 位工程师的速度和效率。
#
# 从这 n 名工程师中最多选择 k 名不同的工程师，使其组成的团队具有最大的团队表现值。
#
# 团队表现值 的定义为：一个团队中「所有工程师速度的和」乘以他们「效率值中的最小值」。
#
# 请你返回该团队的​​​​​​最大团队表现值，由于答案可能很大，请你返回结果对 10^9 + 7 取余后的结果。
#
#
#
# 示例 1：
#
# 输入：n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
# 输出：60
# 解释：
# 我们选择工程师 2（speed=10 且 efficiency=4）和工程师 5（speed=5 且 efficiency=7）。他们的团队表现值为 performance = (10 + 5) * min(4, 7) = 60 。
# 示例 2：
#
# 输入：n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
# 输出：68
# 解释：
# 此示例与第一个示例相同，除了 k = 3 。我们可以选择工程师 1 ，工程师 2 和工程师 5 得到最大的团队表现值。表现值为 performance = (2 + 10 + 5) * min(5, 4, 7) = 68 。
# 示例 3：
#
# 输入：n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
# 输出：72
#
#
# 提示：
#
# 1 <= k <= n <= 10^5
# speed.length == n
# efficiency.length == n
# 1 <= speed[i] <= 10^5
# 1 <= efficiency[i] <= 10^8

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        comb = sorted(zip(speed, efficiency), reverse=True)
        comb1, comb2 = comb[:k], comb[k:]
        ss = sum(x for x, _ in comb1)  # 当前速度之和
        hp = [[y, x] for x, y in comb1]
        heapify(hp)
        ans = ss * hp[0][0]

        for s, e in comb2:
            if e <= hp[0][0]:
                continue
            # 替换当前效率最低的工程师 （替换后表现值未必提高）
            e1, s1 = heappop(hp)
            ss += (s - s1)
            heappush(hp, [s, e])
            cur = ss * hp[0][0]
            ans = max(ans, cur)
        return ans





so = Solution()
print(so.maxPerformance(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3))
print(so.maxPerformance(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2))
print(so.maxPerformance(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4))





