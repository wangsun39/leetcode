# 监狱中 8 间牢房排成一排，每间牢房可能被占用或空置。
#
# 每天，无论牢房是被占用或空置，都会根据以下规则进行变更：
#
# 如果一间牢房的两个相邻的房间都被占用或都是空的，那么该牢房就会被占用。
# 否则，它就会被空置。
# 注意：由于监狱中的牢房排成一行，所以行中的第一个和最后一个牢房不存在两个相邻的房间。
#
# 给你一个整数数组 cells ，用于表示牢房的初始状态：如果第 i 间牢房被占用，则 cell[i]==1，否则 cell[i]==0 。另给你一个整数 n 。
#
# 请你返回 n 天后监狱的状况（即，按上文描述进行 n 次变更）。
#
#
#
# 示例 1：
#
# 输入：cells = [0,1,0,1,1,0,0,1], n = 7
# 输出：[0,0,1,1,0,0,0,0]
# 解释：下表总结了监狱每天的状况：
# Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
# Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
# Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
# Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
# Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
# Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
# Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
# Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
# 示例 2：
#
# 输入：cells = [1,0,0,1,0,0,1,0], n = 1000000000
# 输出：[0,0,1,1,1,1,1,0]
#
#
# 提示：
#
# cells.length == 8
# cells[i] 为 0 或 1
# 1 <= n <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        t2d = {}
        d2l = {}
        i = 0
        cur = cells[:]
        while tuple(cur) not in t2d:
            nxt = [0] * 8
            t2d[tuple(cur)] = i
            d2l[i] = cur
            for j in range(1, 7):
                nxt[j] = 0 if cur[j - 1] != cur[j + 1] else 1
            i += 1
            cur = nxt[:]
            if i == n:
                return cur
        start = t2d[tuple(cur)]  # 周期性开始的第一天
        T = i - start
        n -= start
        q, r = divmod(n, T)
        return d2l[start + r]




so = Solution()
print(so.prisonAfterNDays(cells = [0,1,0,1,1,0,0,1], n = 7))
print(so.prisonAfterNDays(cells = [1,0,0,1,0,0,1,0], n = 1000000000))




