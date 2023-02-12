# 你正在玩一个单人游戏，面前放置着大小分别为 a​​​​​​、b 和 c​​​​​​ 的 三堆 石子。
#
# 每回合你都要从两个 不同的非空堆 中取出一颗石子，并在得分上加 1 分。当存在 两个或更多 的空堆时，游戏停止。
#
# 给你三个整数 a 、b 和 c ，返回可以得到的 最大分数 。
#
#
# 示例 1：
#
# 输入：a = 2, b = 4, c = 6
# 输出：6
# 解释：石子起始状态是 (2, 4, 6) ，最优的一组操作是：
# - 从第一和第三堆取，石子状态现在是 (1, 4, 5)
# - 从第一和第三堆取，石子状态现在是 (0, 4, 4)
# - 从第二和第三堆取，石子状态现在是 (0, 3, 3)
# - 从第二和第三堆取，石子状态现在是 (0, 2, 2)
# - 从第二和第三堆取，石子状态现在是 (0, 1, 1)
# - 从第二和第三堆取，石子状态现在是 (0, 0, 0)
# 总分：6 分 。
# 示例 2：
#
# 输入：a = 4, b = 4, c = 6
# 输出：7
# 解释：石子起始状态是 (4, 4, 6) ，最优的一组操作是：
# - 从第一和第二堆取，石子状态现在是 (3, 3, 6)
# - 从第一和第三堆取，石子状态现在是 (2, 3, 5)
# - 从第一和第三堆取，石子状态现在是 (1, 3, 4)
# - 从第一和第三堆取，石子状态现在是 (0, 3, 3)
# - 从第二和第三堆取，石子状态现在是 (0, 2, 2)
# - 从第二和第三堆取，石子状态现在是 (0, 1, 1)
# - 从第二和第三堆取，石子状态现在是 (0, 0, 0)
# 总分：7 分 。
# 示例 3：
#
# 输入：a = 1, b = 8, c = 8
# 输出：8
# 解释：最优的一组操作是连续从第二和第三堆取 8 回合，直到将它们取空。
# 注意，由于第二和第三堆已经空了，游戏结束，不能继续从第一堆中取石子。
#
#
# 提示：
#
# 1 <= a, b, c <= 105



from typing import List


class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        a, b, c = sorted([a, b, c])
        if c >= a + b:
            return a + b
        # 从a , b 中多的那个和c配对，直至c取完
        # 这样剩下的a,b相差最多为1，那么剩余就是最多1，这样就是最大分数
        return (a + b - c) // 2 + c
        # x = (a - b + c) // 2
        # y = c - x
        # return c + min(a - x, b - y)




so = Solution()

print(so.maximumScore(a = 29, b = 30, c = 18))  # 38
print(so.maximumScore(a = 8, b = 16, c = 22))  # 23
print(so.maximumScore(a = 2, b = 4, c = 6))  # 6
print(so.maximumScore(a = 4, b = 4, c = 6))  # 7
print(so.maximumScore(a = 1, b = 8, c = 8))  # 8



