# 在 x 轴上有一个一维的花园。花园长度为 n，从点 0 开始，到点 n 结束。
#
# 花园里总共有 n + 1 个水龙头，分别位于 [0, 1, ..., n] 。
#
# 给你一个整数 n 和一个长度为 n + 1 的整数数组 ranges ，其中 ranges[i] （下标从 0 开始）表示：如果打开点 i 处的水龙头，可以灌溉的区域为 [i -  ranges[i], i + ranges[i]] 。
#
# 请你返回可以灌溉整个花园的 最少水龙头数目 。如果花园始终存在无法灌溉到的地方，请你返回 -1 。
#
#
#
# 示例 1：
#
#
#
# 输入：n = 5, ranges = [3,4,1,1,0,0]
# 输出：1
# 解释：
# 点 0 处的水龙头可以灌溉区间 [-3,3]
# 点 1 处的水龙头可以灌溉区间 [-3,5]
# 点 2 处的水龙头可以灌溉区间 [1,3]
# 点 3 处的水龙头可以灌溉区间 [2,4]
# 点 4 处的水龙头可以灌溉区间 [4,4]
# 点 5 处的水龙头可以灌溉区间 [5,5]
# 只需要打开点 1 处的水龙头即可灌溉整个花园 [0,5] 。
# 示例 2：
#
# 输入：n = 3, ranges = [0,0,0,0]
# 输出：-1
# 解释：即使打开所有水龙头，你也无法灌溉整个花园。
#
#
# 提示：
#
# 1 <= n <= 104
# ranges.length == n + 1
# 0 <= ranges[i] <= 100

from typing import List
from math import *

class Solution:
    def minTaps1(self, n: int, ranges: List[int]) -> int:
        # 贪心
        right = list(range(n + 1))
        for i, x in enumerate(ranges):
            left = max(0, i - x)
            right[left] = max(right[left], i + x)
        ans = 1
        l, r = 0, right[0]
        next = r
        while True:
            if r >= n:
                return ans
            while l <= r:
                next = max(next, right[l])
                l += 1
            if next == r:
                return -1
            ans += 1
            r = next

    def minTaps(self, n: int, ranges: List[int]) -> int:
        # 排序
        inv = [[max(0, i - x), min(n, i + x)] for i, x in enumerate(ranges)]
        inv.sort()
        # print(inv)
        dp = [inf] * (n + 1)
        dp[0] = 0  # 覆盖左边 i + 1 个点需要的最少数量
        right = 1
        for x, y in inv:
            if dp[x] == inf:
                return -1
            # 用 right 记录左右侧计算到那个点，避免对 [x, y] 整个区间遍历
            if y < right or x == y:
                continue
            dp[y] = min(dp[y], dp[x] + 1)
            while right <= y:
                dp[right] = dp[y]
                right += 1
        # print(dp)
        return dp[-1]



so = Solution()
print(so.minTaps(25, [3,0,1,5,4,1,4,2,4,4,3,3,3,0,3,2,5,1,5,5,2,3,1,0,2,4]))  # 4
print(so.minTaps(8, [4,0,0,0,0,0,0,0,4]))  # 2
print(so.minTaps(7, [1,2,1,0,2,1,0,1]))  # 3
print(so.minTaps(n = 5, ranges = [3,4,1,1,0,0]))  # 1
print(so.minTaps(n = 3, ranges = [0,0,0,0]))  # -1




