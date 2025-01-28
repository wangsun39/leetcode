# 病毒扩散得很快，现在你的任务是尽可能地通过安装防火墙来隔离病毒。
#
# 假设世界由m x n的二维矩阵isInfected组成，isInfected[i][j] == 0表示该区域未感染病毒，而 isInfected[i][j] == 1表示该区域已感染病毒。可以在任意 2 个相邻单元之间的共享边界上安装一个防火墙（并且只有一个防火墙）。
#
# 每天晚上，病毒会从被感染区域向相邻未感染区域扩散，除非被防火墙隔离。现由于资源有限，每天你只能安装一系列防火墙来隔离其中一个被病毒感染的区域（一个区域或连续的一片区域），且该感染区域对未感染区域的威胁最大且 保证唯一。
#
# 你需要努力使得最后有部分区域不被病毒感染，如果可以成功，那么返回需要使用的防火墙个数; 如果无法实现，则返回在世界被病毒全部感染时已安装的防火墙个数。
#
#
#
# 示例 1：
#
#
#
# 输入: isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
# 输出: 10
# 解释:一共有两块被病毒感染的区域。
# 在第一天，添加 5 墙隔离病毒区域的左侧。病毒传播后的状态是:
#
# 第二天，在右侧添加 5 个墙来隔离病毒区域。此时病毒已经被完全控制住了。
#
# 示例 2：
#
#
#
# 输入: isInfected = [[1,1,1],[1,0,1],[1,1,1]]
# 输出: 4
# 解释: 虽然只保存了一个小区域，但却有四面墙。
# 注意，防火墙只建立在两个不同区域的共享边界上。
# 示例3:
#
# 输入: isInfected = [[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]
# 输出: 13
# 解释: 在隔离右边感染区域后，隔离左边病毒区域只需要 2 个防火墙。
#
#
# 提示:
#
# m ==isInfected.length
# n ==isInfected[i].length
# 1 <= m, n <= 50
# isInfected[i][j]is either0or1
# 在整个描述的过程中，总有一个相邻的病毒区域，它将在下一轮 严格地感染更多未受污染的方块



from typing import List
from collections import deque
class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        m, n = len(isInfected), len(isInfected[0])
        def update():
            ss = []
            isCalc = [[False for _ in range(n)] for _ in range(m)]
            def bfs(i, j, s):
                dq = deque()
                dq.append((i, j))
                s.add((i, j))
                isCalc[i][j] = True
                numOfWalls = 0
                threaten = set()
                while len(dq):
                    (x, y) = dq.popleft()
                    for dir in dirs:
                        xx, yy = x + dir[0], y + dir[1]
                        if 0 <= xx < m and 0 <= yy < n:
                            if isCalc[xx][yy]:
                                continue
                            if 1 == isInfected[xx][yy]:
                                dq.append((xx, yy))
                                s.add((xx, yy))
                                isCalc[xx][yy] = True
                            elif 0 == isInfected[xx][yy]:
                                numOfWalls += 1
                                threaten.add((xx, yy))
                return numOfWalls, threaten

            all = True
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 0:
                        all = False
                    if isInfected[i][j] == 1 and not isCalc[i][j]:
                        s = set()
                        numOfWalls, threaten = bfs(i, j, s)
                        ss.append([numOfWalls, s, threaten])

            ss.sort(key=lambda x: len(x[2]))
            if len(ss) == 0 or all:
                return 0
            for (i, j) in ss[-1][1]:
                isInfected[i][j] = 2  # 隔离区
            def extent(s):
                for (i, j) in s:
                    for dir in dirs:
                        ii, jj = i + dir[0], j + dir[1]
                        if 0 <= ii < m and 0 <= jj < n:
                            if isInfected[ii][jj] == 0:
                                isInfected[ii][jj] = 1
            for s in ss[:-1]:
                extent(s[1])
            print(ss)
            print(isInfected)
            return ss[-1][0]

        ans = 0
        while True:
            cur = update()
            if cur == 0:
                return ans
            ans += cur
    def containVirus1(self, isInfected: List[List[int]]) -> int:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        m, n = len(isInfected), len(isInfected[0])
        ans = 0

        while True:
            neighbors, firewalls = list(), list()
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1:
                        q = deque([(i, j)])
                        neighbor = set()
                        firewall, idx = 0, len(neighbors) + 1
                        isInfected[i][j] = -idx

                        while q:
                            x, y = q.popleft()
                            for d in range(4):
                                nx, ny = x + dirs[d][0], y + dirs[d][1]
                                if 0 <= nx < m and 0 <= ny < n:
                                    if isInfected[nx][ny] == 1:
                                        q.append((nx, ny))
                                        isInfected[nx][ny] = -idx
                                    elif isInfected[nx][ny] == 0:
                                        firewall += 1
                                        neighbor.add((nx, ny))

                        neighbors.append(neighbor)
                        firewalls.append(firewall)

            if not neighbors:
                break

            idx = 0
            for i in range(1, len(neighbors)):
                if len(neighbors[i]) > len(neighbors[idx]):
                    idx = i

            ans += firewalls[idx]
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] < 0:
                        if isInfected[i][j] != -idx - 1:
                            isInfected[i][j] = 1
                        else:
                            isInfected[i][j] = 2

            for i, neighbor in enumerate(neighbors):
                if i != idx:
                    for x, y in neighbor:
                        isInfected[x][y] = 1
            print(isInfected)
            if len(neighbors) == 1:
                break

        return ans




so = Solution()
print(so.containVirus([[0,1,0,1,1,1,1,1,1,0],[0,0,0,1,0,0,0,0,0,0],[0,0,1,1,1,0,0,0,1,0],[0,0,0,1,1,0,0,1,1,0],[0,1,0,0,1,0,1,1,0,1],[0,0,0,1,0,1,0,1,1,1],[0,1,0,0,1,0,0,1,1,0],[0,1,0,1,0,0,0,1,1,0],[0,1,1,0,0,1,1,0,0,1],[1,0,1,1,0,1,0,1,0,1]]))
print(so.containVirus([[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]))
print(so.containVirus([[1,1,1],[1,0,1],[1,1,1]]))
print(so.containVirus([[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]))


