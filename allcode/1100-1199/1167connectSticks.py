# 你有一些长度为正整数的木棍。这些长度以数组 sticks 的形式给出， sticks[i] 是第 i 个木棍的长度。
#
# 你可以通过支付 x + y 的成本将任意两个长度为 x 和 y 的木棍连接成一个木棍。你必须连接所有的木棍，直到剩下一个木棍。
#
# 返回以这种方式将所有给定的木棍连接成一个木棍的 最小成本 。
#
#
#
# 示例 1：
#
# 输入：sticks = [2,4,3]
# 输出：14
# 解释：从 sticks = [2,4,3] 开始。
# 1. 连接 2 和 3 ，费用为 2 + 3 = 5 。现在 sticks = [5,4]
# 2. 连接 5 和 4 ，费用为 5 + 4 = 9 。现在 sticks = [9]
# 所有木棍已经连成一根，总费用 5 + 9 = 14
# 示例 2：
#
# 输入：sticks = [1,8,3,5]
# 输出：30
# 解释：从 sticks = [1,8,3,5] 开始。
# 1. 连接 1 和 3 ，费用为 1 + 3 = 4 。现在 sticks = [4,8,5]
# 2. 连接 4 和 5 ，费用为 4 + 5 = 9 。现在 sticks = [9,8]
# 3. 连接 9 和 8 ，费用为 9 + 8 = 17 。现在 sticks = [17]
# 所有木棍已经连成一根，总费用 4 + 9 + 17 = 30
# 示例 3：
#
# 输入：sticks = [5]
# 输出：0
# 解释：只有一根木棍，不必再连接。总费用 0
#
#
# 提示：
#
# 1 <= sticks.length <= 104
# 1 <= sticks[i] <= 104

from leetcode.allcode.competition.mypackage import *

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        ans = 0
        while len(sticks) > 1:
            x = heappop(sticks)
            y = heappop(sticks)
            ans += (x + y)
            heappush(sticks, x + y)
        return ans




so = Solution()
print(so.connectSticks([1,8,3,5]))
print(so.connectSticks([2,4,3]))

