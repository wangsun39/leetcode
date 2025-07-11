# 在一根无限长的数轴上，你站在0的位置。终点在target的位置。
#
# 你可以做一些数量的移动 numMoves :
#
# 每次你可以选择向左或向右移动。
# 第 i 次移动（从  i == 1 开始，到 i == numMoves ），在选择的方向上走 i 步。
# 给定整数 target ，返回 到达目标所需的 最小 移动次数(即最小 numMoves ) 。
#
#
#
# 示例 1:
#
# 输入: target = 2
# 输出: 3
# 解释:
# 第一次移动，从 0 到 1 。
# 第二次移动，从 1 到 -1 。
# 第三次移动，从 -1 到 2 。
# 示例 2:
#
# 输入: target = 3
# 输出: 2
# 解释:
# 第一次移动，从 0 到 1 。
# 第二次移动，从 1 到 3 。
#
#
# 提示:
#
# -109 <= target <= 109
# target != 0




from leetcode.allcode.competition.mypackage import *
class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        def f(x):
            return x * (x + 1) // 2
        n = int((-1 + (1 + 8 * target) ** 0.5) // 2)
        # print(n)
        while True:
            y = f(n)
            if (y - target) & 1 == 0 and y >= target:
                return n
            n += 1

so = Solution()
print(so.reachNumber(-1))
print(so.reachNumber(2))
print(so.reachNumber(3))


