# 在 "100 game" 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，累计整数和，先使得累计整数和 达到或超过  100 的玩家，即为胜者。
#
# 如果我们将游戏规则改为 “玩家 不能 重复使用整数” 呢？
#
# 例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 >= 100。
#
# 给定两个整数 maxChoosableInteger （整数池中可选择的最大数）和 desiredTotal（累计和），若先出手的玩家能稳赢则返回 true ，否则返回 false 。假设两位玩家游戏时都表现 最佳 。
#
#
#
# 示例 1：
#
# 输入：maxChoosableInteger = 10, desiredTotal = 11
# 输出：false
# 解释：
# 无论第一个玩家选择哪个整数，他都会失败。
# 第一个玩家可以选择从 1 到 10 的整数。
# 如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。
# 第二个玩家可以通过选择整数 10（那么累积和为 11 >= desiredTotal），从而取得胜利.
# 同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。
# 示例 2:
#
# 输入：maxChoosableInteger = 10, desiredTotal = 0
# 输出：true
# 示例 3:
#
# 输入：maxChoosableInteger = 10, desiredTotal = 1
# 输出：true
#
#
# 提示:
#
# 1 <= maxChoosableInteger <= 20
# 0 <= desiredTotal <= 300

from leetcode.allcode.competition.mypackage import *

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

    def canIWin2(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
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


    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # 2024/6/16 记忆化搜索，减少一个参数，但性能没有什么变化
        @cache
        def dfs(vis):
            used = 0
            for i in range(maxChoosableInteger):
                if (vis >> i) & 1:
                    used += i + 1
            left = desiredTotal - used
            if left <= 0:
                return False  # 输
            for i in range(maxChoosableInteger):
                if (vis >> i) & 1 == 0:
                    if not dfs(vis | (1 << i)):
                        return True
            return False
        if desiredTotal == 0: return True
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal: return False
        return dfs(0)

so = Solution()
print(so.canIWin(5, 50))  # F
print(so.canIWin(10, 0))  # T
print(so.canIWin(10, 11))  # F
print(so.canIWin(11, 25))  # T
print(so.canIWin(4, 6))  # T

