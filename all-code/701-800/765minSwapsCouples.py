# n 对情侣坐在连续排列的 2n 个座位上，想要牵到对方的手。
#
# 人和座位由一个整数数组 row 表示，其中 row[i] 是坐在第 i 个座位上的人的 ID。情侣们按顺序编号，第一对是 (0, 1)，第二对是 (2, 3)，以此类推，最后一对是 (2n-2, 2n-1)。
#
# 返回 最少交换座位的次数，以便每对情侣可以并肩坐在一起。 每次交换可选择任意两人，让他们站起来交换座位。
#
#
#
# 示例 1:
#
# 输入: row = [0,2,1,3]
# 输出: 1
# 解释: 只需要交换row[1]和row[2]的位置即可。
# 示例 2:
#
# 输入: row = [3,2,0,1]
# 输出: 0
# 解释: 无需交换座位，所有的情侣都已经可以手牵手了。
#
#
# 提示:
#
# 2n == row.length
# 2 <= n <= 30
# n 是偶数
# 0 <= row[i] < 2n
# row 中所有元素均无重复
from copy import deepcopy
from typing import List
from collections import Counter, defaultdict

class Solution:
    def minSwapsCouples1(self, row: List[int]) -> int:
        n = len(row)
        d = {x: i for i, x in enumerate(row)}
        def pair(x):
            if x & 1 == 0:
                return x + 1
            return x - 1

        ans = 0
        for i in range(0, n, 2):
            if row[i] < row[i + 1] and row[i] & 1 == 0 and row[i + 1] - row[i] == 1:
                continue
            if row[i] > row[i + 1] and row[i + 1] & 1 == 0 and row[i] - row[i + 1] == 1:
                continue
            p = pair(row[i])  # 对象下标
            pos_p = d[p]  # 对象的位置

            row[i + 1], row[pos_p] = p, row[i + 1]
            d[row[i + 1]], d[p] = pos_p, i + 1
            ans += 1

        return ans
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        fa = list(range(n // 2))
        def find(x):
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]
        def union(x, y):
            fa[find(y)] = find(x)

        for i in range(0, n, 2):
            union(row[i] // 2, row[i + 1] // 2)
        print(fa)
        for i in range(n // 2):
            fa[i] = find(i)
        counter = Counter(fa)
        ans = 0
        for x in counter.values():
            ans += (x - 1)

        # print(counter)
        return ans


so = Solution()
print(so.minSwapsCouples(row = [0,2,4,6,7,1,3,5]))  # 3
print(so.minSwapsCouples(row = [0,2,1,3]))  # 1
print(so.minSwapsCouples(row = [3,2,0,1]))  # 0

