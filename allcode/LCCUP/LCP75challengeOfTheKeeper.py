# 随着不断的深入，小扣来到了守护者之森寻找的魔法水晶。首先，他必须先通过守护者的考验。
#
# 考验的区域是一个正方形的迷宫，maze[i][j] 表示在迷宫 i 行 j 列的地形：
#
# 若为 . ，表示可以到达的空地；
# 若为 # ，表示不可到达的墙壁；
# 若为 S ，表示小扣的初始位置；
# 若为 T ，表示魔法水晶的位置。
# 小扣每次可以向 上、下、左、右 相邻的位置移动一格。而守护者拥有一份「传送魔法卷轴」，使用规则如下：
#
# 魔法需要在小扣位于 空地 时才能释放，发动后卷轴消失；；
# 发动后，小扣会被传送到水平或者竖直的镜像位置，且目标位置不得为墙壁(如下图所示)；image.png
# 在使用卷轴后，小扣将被「附加负面效果」，因此小扣需要尽可能缩短传送后到达魔法水晶的距离。而守护者的目标是阻止小扣到达魔法水晶的位置；如果无法阻止，则尽可能 增加 小扣传送后到达魔法水晶的距离。 假设小扣和守护者都按最优策略行事，返回小扣需要在 「附加负面效果」的情况下 最少 移动多少次才能到达魔法水晶。如果无法到达，返回 -1。
#
# 注意：
#
# 守护者可以不使用卷轴；
# 传送后的镜像位置可能与原位置相同。
# 示例 1：
#
# 输入：maze = [".....","##S..","...#.","T.#..","###.."]
#
# 输出：7
#
# 解释：如下图所示： 守护者释放魔法的两个最佳的位置为 [2,0] 或 [3,1]： 若小扣经过 [2,0]，守护者在该位置释放魔法， 小扣被传送至 [2,4] 处且加上负面效果，此时小扣还需要移动 7 次才能到达魔法水晶； 若小扣经过 [3,1]，守护者在该位置释放魔法， 小扣被传送至 [3,3] 处且加上负面效果，此时小扣还需要移动 9 次才能到达魔法水晶； 因此小扣负面效果下最少需要移动 7 次才能到达魔法水晶。image.png
#
# 示例 2：
#
# 输入：maze = [".#..","..##",".#S.",".#.T"]
#
# 输出：-1
#
# 解释：如下图所示。 若小扣向下移动至 [3,2]，守护者使其传送至 [0,2]，小扣将无法到达魔法水晶； 若小扣向右移动至 [2,3]，守护者使其传送至 [2,0]，小扣将无法到达魔法水晶；image.png
#
# 示例 3：
#
# 输入：maze = ["S###.","..###","#..##","##..#","###.T"]
#
# 输出：5
#
# 解释：如下图所示： 守护者需要小扣在空地才能释放，因此初始无法将其从 [0,0] 传送至 [0,4]; 当小扣移动至 [2,1] 时，释放卷轴将其传送至水平方向的镜像位置 [2,1]（为原位置） 而后小扣需要移动 5 次到达魔法水晶image.png
#
# 提示：
#
# 4 <= maze.length == maze[i].length <= 200
# maze[i][j] 仅包含 "."、"#"、"S"、"T"

from leetcode.allcode.competition.mypackage import *

class Solution:
    def challengeOfTheKeeper(self, maze: List[str]) -> int:
        n = len(maze)
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        s, t = [-1, -1], [-1, -1]
        for i in range(n):
            for j in range(n):
                if maze[i][j] == 'S':
                    s = (i, j)
                elif maze[i][j] == 'T':
                    t = (i, j)
        dis = [[inf] * n for _ in range(n)]  # (i,j) 到达T的最小距离，不考虑传送
        dis[t[0]][t[1]] = 0

        vis = set()
        vis.add(t)

        dq1 = deque()
        dq1.append(t)
        d = 1
        while dq1:
            dq2 = deque()
            while dq1:
                x, y = dq1.popleft()
                for dx, dy in dir:
                    u, v = x + dx, y + dy
                    if 0 <= u < n and 0 <= v < n and maze[u][v] != '#' and (u, v) not in vis:
                        dq2.append((u, v))
                        vis.add((u, v))
                        dis[u][v] = d

            d += 1
            dq1 = dq2

        # print(dis)
        if s not in vis:
            return -1

        def check(val):  # 从S出发，能否不经过任何dis大于val的点到T
            vis = set()
            dq1 = deque()
            dq1.append(s)
            vis.add(s)
            while dq1:
                x, y = dq1.popleft()
                for dx, dy in dir:
                    u, v = x + dx, y + dy
                    if 0 <= u < n and 0 <= v < n and (u, v) not in vis and maze[u][v] != '#':
                        if (u, v) == t:
                            return True
                        pu, pv = n - 1 - u, n - 1 - v  # 对称点的下标
                        if (maze[pu][v] == '#' or dis[pu][v] <= val) and (maze[u][pv] == '#' or dis[u][pv] <= val):
                            # 2个对称点都是石头或距离t超过val
                            dq1.append((u, v))
                            vis.add((u, v))
            return False

        if not check(n * n):
            return -1

        lo, hi = -1, n * n
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid
        return hi


so = Solution()
print(so.challengeOfTheKeeper(maze = [".#..","..##",".#S.",".#.T"]))
print(so.challengeOfTheKeeper(maze = ["S###.","..###","#..##","##..#","###.T"]))
print(so.challengeOfTheKeeper(maze = [".....","##S..","...#.","T.#..","###.."]))




