# Alice 和 Bob 两个人轮流玩一个游戏，Alice 先手。
#
# 一开始，有 n 个石子堆在一起。每个人轮流操作，正在操作的玩家可以从石子堆里拿走 任意 非零 平方数 个石子。
#
# 如果石子堆里没有石子了，则无法操作的玩家输掉游戏。
#
# 给你正整数 n ，且已知两个人都采取最优策略。如果 Alice 会赢得比赛，那么返回 True ，否则返回 False 。
#
#
#
# 示例 1：
#
# 输入：n = 1
# 输出：true
# 解释：Alice 拿走 1 个石子并赢得胜利，因为 Bob 无法进行任何操作。
# 示例 2：
#
# 输入：n = 2
# 输出：false
# 解释：Alice 只能拿走 1 个石子，然后 Bob 拿走最后一个石子并赢得胜利（2 -> 1 -> 0）。
# 示例 3：
#
# 输入：n = 4
# 输出：true
# 解释：n 已经是一个平方数，Alice 可以一次全拿掉 4 个石子并赢得胜利（4 -> 0）。
# 示例 4：
#
# 输入：n = 7
# 输出：false
# 解释：当 Bob 采取最优策略时，Alice 无法赢得比赛。
# 如果 Alice 一开始拿走 4 个石子， Bob 会拿走 1 个石子，然后 Alice 只能拿走 1 个石子，Bob 拿走最后一个石子并赢得胜利（7 -> 3 -> 2 -> 1 -> 0）。
# 如果 Alice 一开始拿走 1 个石子， Bob 会拿走 4 个石子，然后 Alice 只能拿走 1 个石子，Bob 拿走最后一个石子并赢得胜利（7 -> 6 -> 2 -> 1 -> 0）。
# 示例 5：
#
# 输入：n = 17
# 输出：false
# 解释：如果 Bob 采取最优策略，Alice 无法赢得胜利。
#
#
# 提示：
#
# 1 <= n <= 10^5

from leetcode.allcode.competition.mypackage import *

class Solution:
    def winnerSquareGame1(self, n: int) -> bool:
        result = [0] * (n + 1)   # result[i] 表示剩余i个石头，轮到Alice时的结果，1表示胜利，-1表示失败
        dq = deque([x * x for x in range(1, isqrt(n) + 1)])
        cur = True  # 轮到 Alice
        vis = [0] * (n + 1)
        for x in dq:
            vis[x] = 1
            if x == n:
                return True
        while dq:
            dq2 = deque()
            while dq:
                x = dq.popleft()
                result[x] = cur
                for i in range(1, n):
                    v = i * i + x
                    if v == n:
                        return not cur
                    if v > n:
                        break
                    if vis[v] == 0:
                        dq2.append(v)
                        vis[v] = 1
            dq = dq2
            cur = not cur

    def winnerSquareGame(self, n: int) -> bool:
        sq = set(x * x for x in range(1, isqrt(n) + 1))
        @cache
        def dfs(x):
            if x in sq:
                return True
            for i in range(1, x):
                if x < i * i: break
                if not dfs(x - i * i):
                    return True
            return False
        return dfs(n)



so = Solution()
print(so.winnerSquareGame(12))
print(so.winnerSquareGame(17))
print(so.winnerSquareGame(3))
print(so.winnerSquareGame(1))
print(so.winnerSquareGame(2))
print(so.winnerSquareGame(4))
print(so.winnerSquareGame(7))




