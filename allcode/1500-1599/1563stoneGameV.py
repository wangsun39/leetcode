# 几块石子 排成一行 ，每块石子都有一个关联值，关联值为整数，由数组 stoneValue 给出。
#
# 游戏中的每一轮：Alice 会将这行石子分成两个 非空行（即，左侧行和右侧行）；Bob 负责计算每一行的值，即此行中所有石子的值的总和。Bob 会丢弃值最大的行，Alice 的得分为剩下那行的值（每轮累加）。如果两行的值相等，Bob 让 Alice 决定丢弃哪一行。下一轮从剩下的那一行开始。
#
# 只 剩下一块石子 时，游戏结束。Alice 的分数最初为 0 。
#
# 返回 Alice 能够获得的最大分数 。
#
#
#
# 示例 1：
#
# 输入：stoneValue = [6,2,3,4,5,5]
# 输出：18
# 解释：在第一轮中，Alice 将行划分为 [6，2，3]，[4，5，5] 。左行的值是 11 ，右行的值是 14 。Bob 丢弃了右行，Alice 的分数现在是 11 。
# 在第二轮中，Alice 将行分成 [6]，[2，3] 。这一次 Bob 扔掉了左行，Alice 的分数变成了 16（11 + 5）。
# 最后一轮 Alice 只能将行分成 [2]，[3] 。Bob 扔掉右行，Alice 的分数现在是 18（16 + 2）。游戏结束，因为这行只剩下一块石头了。
# 示例 2：
#
# 输入：stoneValue = [7,7,7,7,7,7,7]
# 输出：28
# 示例 3：
#
# 输入：stoneValue = [4]
# 输出：0
#
#
# 提示：
#
# 1 <= stoneValue.length <= 500
# 1 <= stoneValue[i] <= 10^6

from leetcode.allcode.competition.mypackage import *

class Solution:
    def stoneGameV1(self, stoneValue: List[int]) -> int:
        # 此方法会超时 O(n^3)
        n = len(stoneValue)
        s = list(accumulate(stoneValue, initial=0))
        @cache
        def dfs(l, r):
            if l == r: return 0
            if r - l == 1: return min(stoneValue[l], stoneValue[r])
            res = 0
            for i in range(l, r):
                s1, s2 = s[i + 1] - s[l], s[r + 1] - s[i + 1]
                if s1 < s2:
                    res = max(res, s1 + dfs(l, i))
                elif s1 > s2:
                    res = max(res, s2 + dfs(i + 1, r))
                else:
                    res = max(res, s1 + dfs(l, i), s2 + dfs(i + 1, r))
            return res
        return dfs(0, n - 1)

    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        s = list(accumulate(stoneValue, initial=0))

        ml = [[0] * n for _ in range(n)]  # 记录区间[i, j]左侧区间一半的位置
        mr = [[0] * n for _ in range(n)]  # 记录区间[i, j]右侧区间一半的位置
        for i in range(n):
            mid = i  # [i, mid) 区间和 < [i, j] 区间和一半
            for j in range(i, n):
                if i == j:
                    continue
                ml[i][j] = ml[i][j - 1]
                while mid < n and (s[mid + 1] - s[i]) * 2 <= (s[j + 1] - s[i]):
                    mid += 1
                    ml[i][j] = mid
        for j in range(n - 1, -1, -1):
            mid = j  # (mid, j] 区间和 < [i, j] 区间和一半
            for i in range(j, -1, -1):
                mr[i][j] = j
                if i + 1 <= j:
                    mr[i][j] = mr[i + 1][j]
                while mid >= 0 and (s[j + 1] - s[mid]) * 2 <= (s[j + 1] - s[i]):
                    mid -= 1
                    mr[i][j] = mid

        @cache
        def f2(i, j):
            if i == j: return 0
            res = 0
            if i < j:
                res = f2(i, j - 1)
            r1 = ml[i][j - 1]
            r2 = ml[i][j]
            while r1 < r2:
                res = max(res, f1(i, r1) + s[r1 + 1] - s[i])
                r1 += 1
            return res

        @cache
        def f3(i, j):
            if i == j: return 0
            res = 0
            if i < j:
                res = f3(i + 1, j)
            l1 = mr[i + 1][j]
            l2 = mr[i][j]
            while l1 > l2:
                res = max(res, f1(l1, j) + s[j + 1] - s[l1])
                l1 -= 1
            return res

        # f1(i, j) 区间[i,j]上的目标值
        # f1(i,j)=max(f2(i,j),f3(i,j))
        # 设m1为满足区间[i,m)之和2倍不超过区间和[i,j]的最大m
        # 设m2为满足区间(m,j]之和2倍不超过区间和[i,j]的最小m
        # f2(i,j)=max(f1(i,k)+s([i,k]))  其中i<=k<m1
        # f3(i,j)=max(f1(k,j)+s([k,j]))  其中m2<k<=j
        # 转换后
        # f2(i,j)=max(f2(i,j-1),剩余未计算的f1(i,k)+s([i,k]))
        # f3(i,j)=max(f3(i+1,j),剩余未计算的f1(k,j)+s([k,j]))
        @cache
        def f1(i, j):
            if i == j: return 0
            return max(f2(i, j), f3(i, j))

        return f1(0, n - 1)

        # print(f)
        return f[0][n - 1]


so = Solution()
print(so.stoneGameV([6,12,2,44,51,96]))  # 96
print(so.stoneGameV([6,2,3,4,5,5]))  # 18
print(so.stoneGameV([44,51,96]))  # 139
print(so.stoneGameV([98,77,24,49,6,12,2,44,51,96]))   # 330
print(so.stoneGameV([7,7,7,7,7,7,7]))  # 28
print(so.stoneGameV([7,7,7]))  # 7
print(so.stoneGameV([4]))  # 0




