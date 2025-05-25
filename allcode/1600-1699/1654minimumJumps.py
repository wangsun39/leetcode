# 有一只跳蚤的家在数轴上的位置 x 处。请你帮助它从位置 0 出发，到达它的家。
#
# 跳蚤跳跃的规则如下：
#
# 它可以 往前 跳恰好 a 个位置（即往右跳）。
# 它可以 往后 跳恰好 b 个位置（即往左跳）。
# 它不能 连续 往后跳 2 次。
# 它不能跳到任何 forbidden 数组中的位置。
# 跳蚤可以往前跳 超过 它的家的位置，但是它 不能跳到负整数 的位置。
#
# 给你一个整数数组 forbidden ，其中 forbidden[i] 是跳蚤不能跳到的位置，同时给你整数 a， b 和 x ，请你返回跳蚤到家的最少跳跃次数。如果没有恰好到达 x 的可行方案，请你返回 -1 。
#
#
#
# 示例 1：
#
# 输入：forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
# 输出：3
# 解释：往前跳 3 次（0 -> 3 -> 6 -> 9），跳蚤就到家了。
# 示例 2：
#
# 输入：forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
# 输出：-1
# 示例 3：
#
# 输入：forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
# 输出：2
# 解释：往前跳一次（0 -> 16），然后往回跳一次（16 -> 7），跳蚤就到家了。
#
#
# 提示：
#
# 1 <= forbidden.length <= 1000
# 1 <= a, b, forbidden[i] <= 2000
# 0 <= x <= 2000
# forbidden 中所有位置互不相同。
# 位置 x 不在 forbidden 中。
from leetcode.allcode.competition.mypackage import *


# Definition for a binary tree node.
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        if x == 0: return 0
        g = gcd(a, b)
        if x % g != 0:
            return -1
        vis = {}
        for y in forbidden:
            vis[y] = 2  # 1 表示之前是从dir == -1到达的之后还能往左走， 2表示之之前是从dir == 1到达的，之后不能再访问了
        dq1 = deque([[0, 0]])
        cnt = 1
        while dq1:
            dq2 = deque()
            while dq1:
                y, d = dq1.popleft()
                u, v = y + a, y - b
                if u == x:
                    return cnt
                if (u not in vis or vis[u] == 1) and u < 6000:
                    dq2.append([u, 1])
                    vis[u] = 2
                if d >= 0:
                    if v == x:
                        return cnt
                    if v > 0 and v not in vis:
                        dq2.append([v, -1])
                        vis[v] = 1
            cnt += 1
            dq1 = dq2
        return -1

so = Solution()
print(so.minimumJumps(forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11))   # -1
print(so.minimumJumps(forbidden = [162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98], a = 29, b = 98, x = 80))   # -1
print(so.minimumJumps(forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9))   # 3
print(so.minimumJumps(forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7))   # 2






