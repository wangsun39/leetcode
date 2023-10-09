# 在 "100 game" 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，累计整数和，先使得累计整数和达到或超过 100 的玩家，即为胜者。
#
# 如果我们将游戏规则改为 “玩家不能重复使用整数” 呢？
#
# 例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 >= 100。
#
# 给定一个整数 maxChoosableInteger （整数池中可选择的最大数）和另一个整数 desiredTotal（累计和），判断先出手的玩家是否能稳赢（假设两位玩家游戏时都表现最佳）？
#
# 你可以假设 maxChoosableInteger 不会大于 20， desiredTotal 不会大于 300。
#
# 示例：
#
# 输入：
# maxChoosableInteger = 10
# desiredTotal = 11
#
# 输出：
# false
#
# 解释：
# 无论第一个玩家选择哪个整数，他都会失败。
# 第一个玩家可以选择从 1 到 10 的整数。
# 如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。
# 第二个玩家可以通过选择整数 10（那么累积和为 11 >= desiredTotal），从而取得胜利.
# 同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。

from functools import lru_cache

class Solution:
    def canIWin1(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @lru_cache(None)
        def getAnswer(state, distance):  # state是没有选择的数转成二进制数，distance是剩余到目标数字的距离
            if state >= (1 << (distance - 1)):
                print(bin(state), distance, True)
                return True
            for i in range(21):
                idx = (1 << i)
                if state & idx:
                    if not getAnswer(state - idx, distance - (i + 1)):
                        print(bin(state), distance, True)
                        return True
            print(bin(state), distance, False)
            return False
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False
        if desiredTotal <= maxChoosableInteger:
            return True
        state = 2 ** maxChoosableInteger - 1
        return getAnswer(state, desiredTotal)

    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False
        @lru_cache(None)
        def helper(state, step):
            for i in range(maxChoosableInteger):
                if not ((1 << i) & state):
                    continue
                if i + 1 >= step:
                    return True
                new = state & ~(1 << i)
                if not helper(new, step - i - 1):
                    return True
            return False
        state = 2 ** maxChoosableInteger - 1
        return helper(state, desiredTotal)


so = Solution()
print(so.canIWin(5, 50))  # F
print(so.canIWin(11, 25))  # T
print(so.canIWin(4, 6))  # T
print(so.canIWin(10, 0))  # T
print(so.canIWin(10, 11))  # F

