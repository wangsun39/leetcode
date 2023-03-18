# 给你一个奇怪的打印机，它有如下两个特殊的打印规则：
#
# 每一次操作时，打印机会用同一种颜色打印一个矩形的形状，每次打印会覆盖矩形对应格子里原本的颜色。
# 一旦矩形根据上面的规则使用了一种颜色，那么 相同的颜色不能再被使用 。
# 给你一个初始没有颜色的 m x n 的矩形 targetGrid ，其中 targetGrid[row][col] 是位置 (row, col) 的颜色。
#
# 如果你能按照上述规则打印出矩形 targetGrid ，请你返回 true ，否则返回 false 。
#
#
#
# 示例 1：
#
#
#
# 输入：targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]
# 输出：true
# 示例 2：
#
#
#
# 输入：targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]
# 输出：true
# 示例 3：
#
# 输入：targetGrid = [[1,2,1],[2,1,2],[1,2,1]]
# 输出：false
# 解释：没有办法得到 targetGrid ，因为每一轮操作使用的颜色互不相同。
# 示例 4：
#
# 输入：targetGrid = [[1,1,1],[3,1,3]]
# 输出：false
#
#
# 提示：
#
# m == targetGrid.length
# n == targetGrid[i].length
# 1 <= m, n <= 60
# 1 <= targetGrid[row][col] <= 60




from typing import Optional
from collections import deque
# Definition for a binary tree node.
from typing import List
from itertools import accumulate
from collections import defaultdict
from bisect import *

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        rec = {}  # 每种颜色对应的矩形区域
        r, c = len(targetGrid), len(targetGrid[0])
        for i in range(r):
            for j in range(c):
                k = targetGrid[i][j]
                if k in rec:
                    rec[k][0] = min(rec[k][0], i)
                    rec[k][1] = max(rec[k][1], i)
                    rec[k][2] = min(rec[k][2], j)
                    rec[k][3] = max(rec[k][3], j)
                else:
                    rec[k] = [i, i, j, j]
        color = list(rec.keys())
        n = len(color)
        def check(x, y):
            x1, x2, y1, y2 = rec[x]
            x3, x4, y3, y4 = rec[y]
            if x1 > x4 or x3 > x2 or y1 > y4 or y3 > y2:
                return 0  # 不相交
            u1, u2 = max(x1, x3), min(x2, x4)
            v1, v2 = max(y1, y3), min(y2, y4)
            res = 0
            for i in range(u1, u2 + 1):
                for j in range(v1, v2 + 1):
                    if targetGrid[i][j] == x:
                        res |= 1  # x 在上
                    elif targetGrid[i][j] == y:
                        res |= 2  # y 在上
                    if res == 3:
                        return -1  # 不可打印
            return res
        g = defaultdict(set)
        pre_num = {k: 0 for k in rec.keys()}
        for i in range(n):
            for j in range(i + 1, n):
                x, y = color[i], color[j]
                res = check(x, y)
                if res == -1: return False
                if res == 1:
                    g[y].add(x)
                    pre_num[x] += 1
                elif res == 2:
                    g[x].add(y)
                    pre_num[y] += 1
        queue = deque([i for i in pre_num if pre_num[i] == 0])  # deque 在操作大数组时，性能比 list 好很多
        ans = []
        while len(queue):
            q = queue.popleft()
            ans.append(q)
            for x in g[q]:
                pre_num[x] -= 1
                if pre_num[x] == 0:
                    queue.append(x)
        # print(ans)
        if len(ans) != len(color):
            return False  # 存在圈
        return True



so = Solution()
print(so.isPrintable([[1,1,1,1,1,29,29,29,29,29,29,2,1,25,25],[1,1,1,1,1,1,1,1,1,1,1,2,1,25,25],[1,1,1,26,26,26,26,26,26,26,26,26,26,25,25],[1,1,1,26,26,26,26,26,26,26,26,26,26,25,25],[1,1,1,26,26,26,26,26,26,26,26,26,26,7,1],[1,1,1,26,26,26,26,26,26,26,26,26,26,7,1],[1,1,23,26,26,26,26,26,26,26,26,26,26,20,1],[1,1,23,23,10,22,22,22,22,22,22,22,22,20,17],[1,18,23,23,18,18,18,18,16,20,20,20,20,20,15],[1,18,18,18,31,31,31,31,31,31,20,20,20,20,15],[1,11,11,11,31,31,31,31,31,31,20,20,20,20,15],[1,1,1,4,27,27,27,27,30,30,30,27,27,27,27],[1,1,1,1,27,27,27,27,30,30,30,28,28,27,27],[1,1,1,1,27,27,27,27,30,30,30,27,27,27,27]]))  # T
print(so.isPrintable([[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]))  # T
print(so.isPrintable([[5,1,5,3,5],[4,4,4,3,4],[5,1,5,3,5],[2,1,2,2,2],[5,1,5,3,5]]))  # F
print(so.isPrintable([[1,1,1],[3,1,3]]))  # F
print(so.isPrintable([[1,2,1],[2,1,2],[1,2,1]]))  # F
print(so.isPrintable([[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]))  # T





