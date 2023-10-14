# 你有两个果篮，每个果篮中有 n 个水果。给你两个下标从 0 开始的整数数组 basket1 和 basket2 ，用以表示两个果篮中每个水果的成本。
#
# 你希望两个果篮相等。为此，可以根据需要多次执行下述操作：
#
# 选中两个下标 i 和 j ，并交换 basket1 中的第 i 个水果和 basket2 中的第 j 个水果。
# 交换的成本是 min(basket1i,basket2j) 。
# 根据果篮中水果的成本进行排序，如果排序后结果完全相同，则认为两个果篮相等。
#
# 返回使两个果篮相等的最小交换成本，如果无法使两个果篮相等，则返回 -1 。
#
#
#
# 示例 1：
#
# 输入：basket1 = [4,2,2,2], basket2 = [1,4,1,2]
# 输出：1
# 解释：交换 basket1 中下标为 1 的水果和 basket2 中下标为 0 的水果，交换的成本为 1 。此时，basket1 = [4,1,2,2] 且 basket2 = [2,4,1,2] 。重排两个数组，发现二者相等。
# 示例 2：
#
# 输入：basket1 = [2,3,4,1], basket2 = [3,2,5,1]
# 输出：-1
# 解释：可以证明无法使两个果篮相等。
#
#
# 提示：
#
# basket1.length == bakste2.length
# 1 <= basket1.length <= 105
# 1 <= basket1i,basket2i <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        c1, c2 = Counter(basket1), Counter(basket2)
        c = c1 + c2
        for v in c.values():
            if v & 1:
                return -1
        mn = min(c)
        d1, d2 =[], []
        for k, v in c1.items():
            if v <= c[k] // 2:
                continue
            d1.extend([k] * (v - c[k] // 2))
        for k, v in c2.items():
            if v <= c[k] // 2:
                continue
            d2.extend([k] * (v - c[k] // 2))
        d1.sort()
        d2.sort(reverse=True)
        ans = 0
        for i in range(len(d1)):
            ans += min(d1[i], d2[i], mn * 2)
        return ans







so = Solution()
print(so.minCost([4,4,4,4,4,4], [1,1,5,5,2,2]))
print(so.minCost([84,80,43,8,80,88,43,14,100,88], [32,32,42,68,68,100,42,84,14,8]))
print(so.minCost([5,8,15,7], [5,7,8,15]))
print(so.minCost(basket1 = [4,2,2,2], basket2 = [1,4,1,2]))
print(so.minCost(basket1 = [2,3,4,1], basket2 = [3,2,5,1]))




