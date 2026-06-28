# 城堡守卫游戏的胜利条件为使恶魔无法从出生点到达城堡。游戏地图可视作 2*N 的方格图，记作字符串数组 grid，其中：
#
# "." 表示恶魔可随意通行的平地；
# "#" 表示恶魔不可通过的障碍物，玩家可通过在 平地 上设置障碍物，即将 "." 变为 "#" 以阻挡恶魔前进；
# "S" 表示恶魔出生点，将有大量的恶魔该点生成，恶魔可向上/向下/向左/向右移动，且无法移动至地图外；
# "P" 表示瞬移点，移动到 "P" 点的恶魔可被传送至任意一个 "P" 点，也可选择不传送；
# "C" 表示城堡。
# 然而在游戏中用于建造障碍物的金钱是有限的，请返回玩家最少需要放置几个障碍物才能获得胜利。若无论怎样放置障碍物均无法获胜，请返回 -1。
#
# 注意：
#
# 地图上可能有一个或多个出生点
# 地图上有且只有一个城堡
# 示例 1
#
# 输入：grid = ["S.C.P#P.", ".....#.S"]
#
# 输出：3
#
# 解释：至少需要放置三个障碍物image.png
#
# 示例 2：
#
# 输入：grid = ["SP#P..P#PC#.S", "..#P..P####.#"]
#
# 输出：-1
#
# 解释：无论怎样修筑障碍物，均无法阻挡最左侧出生的恶魔到达城堡位置image.png
#
# 示例 3：
#
# 输入：grid = ["SP#.C.#PS", "P.#...#.P"]
#
# 输出：0
#
# 解释：无需放置障碍物即可获得胜利image.png
#
# 示例 4：
#
# 输入：grid = ["CP.#.P.", "...S..S"]
#
# 输出：4
#
# 解释：至少需要放置 4 个障碍物，示意图为放置方法之一image.png
#
# 提示：
#
# grid.length == 2
# 2 <= grid[0].length == grid[1].length <= 10^4
# grid[i][j] 仅包含字符 "."、"#"、"C"、"P"、"S"

from leetcode.allcode.competition.mypackage import *

MAX = lambda a, b: b if b > a else a
MIN = lambda a, b: b if b < a else a

class Solution:
    def guardCastle(self, grid: List[str]) -> int:
        n = len(grid[0])
        for i in range(2):
            grid[i] = list(grid[i])
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for i in range(2):
            for j in range(n):
                if grid[i][j] == '.':
                    grid[i][j] = 0
                elif grid[i][j] == 'S':
                    grid[i][j] = 1
                elif grid[i][j] == 'C':
                    grid[i][j] = 2
                elif grid[i][j] == '#':
                    grid[i][j] = 3
                elif grid[i][j] == 'P':
                    grid[i][j] = 4

        def calc(g):
            def update(i, s1, s2, t1, t2, extra):
                # 第i-2列的状态是s1/s2，目标的状态为t1/t2时，对dp数组进行更新，额外的增量是extra
                if s1 in [1, 2]:
                    if s1 + t1 == 3: return  # 「恶魔」和「城堡」相邻是不允许的
                    if t1 == 0:
                        t1 = s1  # 「空地」的状态直接被更新为前面的状态，状态0的优先级是低于状态1，2的
                if s2 in [1, 2]:
                    if s2 + t2 == 3: return  # 「恶魔」和「城堡」相邻是不允许的
                    if t2 == 0:
                        t2 = s2  # 「空地」的状态直接被更新为前面的状态
                if t1 in [1, 2] and t1 + t2 == 3: return   # 「恶魔」和「城堡」相邻是不允许的
                if t1 in [1, 2] and t2 == 0:
                    t2 = t1  # 「空地」的状态被更新为周围的状态
                if t2 in [1, 2] and t1 == 0:
                    t1 = t2  # 「空地」的状态被更新为周围的状态
                # print(s1,s2,t1,t2,i)
                dp[i][t1][t2] = MIN(dp[i][t1][t2], dp[i - 1][s1][s2] + extra)



            for i in range(2):
                for j in range(n):
                    for di, dj in dir:
                        u, v = i + di, j + dj
                        if 0 <= u < 2 and 0 <= v < n:
                            if {g[i][j], g[u][v]} == {1, 2}:
                                return inf
            dp = [[[inf] * 4 for _ in range(4)] for _ in range(n + 1)]
            dp[0][0][0] = 0
            # dp[i][j][k]  表示当前处理到第 i-1 列，并且第 i-1 列的两个格子的状态分别是 s1和s2时 ，最小需要将「空地」放上「障碍物」的操作次数
            # 注意，dp[i]对应g[i-1]列
            # 4种状态：
            # 0 表示「空地」
            # 1 表示「城堡」或者之前的列存在「城堡」可以到达此位置
            # 2 表示「恶魔」或者之前的列存在「恶魔」可以到达此位置
            # 3 表示「障碍物」
            # 任意两种状态之间都是相互独立的。
            for i in range(1, n + 1):  # 枚举每一列
                # 枚举第i-2列的两个格子共计4*4种状态，计算这两个状态对i-1列两个实际值的可能影响
                for s1 in range(4):
                    for s2 in range(4):
                        update(i, s1, s2, g[0][i - 1], g[1][i - 1], 0)  # 不放置任何障碍，状态直接从左侧转移过来
                        if g[0][i - 1] == 0:
                            update(i, s1, s2, 3, g[1][i - 1], 1)
                        if g[1][i - 1] == 0:
                            update(i, s1, s2, g[0][i - 1], 3, 1)
                        if g[0][i - 1] == 0 and g[1][i - 1] == 0:
                            update(i, s1, s2, 3, 3, 2)
            # print(dp)
            return min(min(x) for x in dp[n])


        # 下面这个思路很关键：
        # 我们可以考虑两种情况：即允许「恶魔」走到「传送门」，或者不允许「恶魔」走到「传送门」
        # 对于第一种情况，我们可以将所有的「传送门」全部看成「恶魔」；  这种情况比较容易理解
        # 对于第二种情况，我们可以将所有的「传送门」全部看成「城堡」。  这种情况就不是这么显然，
        #     可以这么考虑：在不增加任何障碍的前提下，1）「恶魔」和 「城堡」本来就是隔离的，答案为0
        #                                     2）「传送门」和「恶魔」，「传送门」和「城堡」 本来都是隔离的，答案和把「传送门」替换成什么并无关系
        #                 这两种情况的解，用上面两种替换依然是能得到正确答案的
        #                 那么剩下的情况只有：「恶魔」，「传送门」和「城堡」这三者本身都是可以互相到达，那么用上述两种替换方法，一种相当于把「恶魔」隔离出去，另一种相当于把「城堡」隔离出去
        #

        g1 = [r[:] for r in grid]
        for i in range(2):
            for j in range(n):
                if g1[i][j] == 4:  # 将 瞬移点 改为 恶魔
                    g1[i][j] = 1
        ans = calc(g1)

        g1 = [r[:] for r in grid]
        for i in range(2):
            for j in range(n):
                if g1[i][j] == 4:  # 将 瞬移点 改为 城堡
                    g1[i][j] = 2
        ans = min(ans, calc(g1))
        if ans == inf: return -1

        return ans





so = Solution()
print(so.guardCastle(grid = ["SP#P..P#PC#.S", "..#P..P####.#"]))
print(so.guardCastle(grid = ["S.C.P#P.", ".....#.S"]))




