# 在无限平面上有 n 个点。给定两个整数数组 xCoord 和 yCoord，其中 (xCoord[i], yCoord[i]) 表示第 i 个点的坐标。
#
# 你的任务是找出满足以下条件的矩形可能的 最大 面积：
#
# 矩形的四个顶点必须是数组中的 四个 点。
# 矩形的内部或边界上 不能 包含任何其他点。
# 矩形的边与坐标轴 平行 。
# 返回可以获得的 最大面积 ，如果无法形成这样的矩形，则返回 -1。
#
#
#
# 示例 1：
#
# 输入： xCoord = [1,1,3,3], yCoord = [1,3,1,3]
#
# 输出： 4
#
# 解释：
#
# 示例 1 图示
#
# 我们可以用这 4 个点作为顶点构成一个矩形，并且矩形内部或边界上没有其他点。因此，最大面积为 4 。
#
# 示例 2：
#
# 输入： xCoord = [1,1,3,3,2], yCoord = [1,3,1,3,2]
#
# 输出： -1
#
# 解释：
#
# 示例 2 图示
#
# 唯一一组可能构成矩形的点为 [1,1], [1,3], [3,1] 和 [3,3]，但点 [2,2] 总是位于矩形内部。因此，返回 -1 。
#
# 示例 3：
#
# 输入： xCoord = [1,1,3,3,1,3], yCoord = [1,3,1,3,2,2]
#
# 输出： 2
#
# 解释：
#
# 示例 3 图示
#
# 点 [1,3], [1,2], [3,2], [3,3] 可以构成面积最大的矩形，面积为 2。此外，点 [1,1], [1,2], [3,1], [3,2] 也可以构成一个符合题目要求的矩形，面积相同。
#
#
#
# 提示：
#
# 1 <= xCoord.length == yCoord.length <= 2 * 105
# 0 <= xCoord[i], yCoord[i] <= 8 * 107
# 给定的所有点都是 唯一 的。

from leetcode.allcode.competition.mypackage import *

class Fenwick:
    def __init__(self, n: int):
        self.tree = [0] * (n + 1)

    def add(self, i: int) -> None:
        while i < len(self.tree):
            self.tree[i] += 1
            i += i & -i

    # [1,i] 中的元素和
    def pre(self, i: int) -> int:
        res = 0
        while i > 0:
            res += self.tree[i]
            i &= i - 1
        return res

    # [l,r] 中的元素和
    def query(self, l: int, r: int) -> int:
        return self.pre(r) - self.pre(l - 1)


class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        # 离散化
        X = set(xCoord) | set(yCoord)
        dis = {x: i + 1 for i, x in enumerate(sorted(list(X)))}
        rev = {i + 1: x for i, x in enumerate(sorted(list(X)))}
        xCoord = [dis[x] for x in xCoord]
        yCoord = [dis[x] for x in yCoord]
        n = len(xCoord)
        left = defaultdict(lambda: defaultdict(lambda: -inf))  # (x,y) 左侧最近的点
        down = defaultdict(lambda: defaultdict(lambda: -inf))  # (x,y) 下侧最近的点
        rows, cols = defaultdict(list), defaultdict(list)
        for i in range(n):
            x, y = xCoord[i], yCoord[i]
            cols[x].append((x, y))
            rows[y].append((x, y))
        print(rows, cols)
        for row in rows.values():
            row.sort()
            for i in range(1, len(row)):
                left[row[i]] = row[i - 1]
        for col in cols.values():
            col.sort()
            for i in range(1, len(col)):
                down[col[i]] = col[i - 1]
        print(left, down)
        ps = [(xCoord[i], yCoord[i]) for i in range(n)]
        ps.sort()
        fw = Fenwick(len(rev))
        ans = -inf
        right = defaultdict(int)  # 以[x,y1] 和[x,y2]为右边界，[0,y1] 和[0,y2]为左边界的区域内的所有点数
        for x, y in ps:
            # 枚举每个可能的矩形右边
            fw.add(y)
            if (x, y) in down:
                _, y2 = down[(x, y)]
                v = fw.query(y2, y)
                right[(x, y2, y)] = v
        for x, y in ps:
            # 枚举矩形右上角
            if (x, y) not in left: continue
            x1, _ = left[(x, y)]
            if (x, y) in down:
                _, y2 = down[(x, y)]
                if (x1, y) in down and down[(x1, y)] == (x1, y2) and (x, y2) in left and left[(x, y2)] == (x1, y2):
                    if right[(x, y2, y)] - right[(x1, y2, y)] == 2:
                        ans = max(ans, (rev[y] - rev[y2]) * (rev[x] - rev[x1]))
        return ans

so = Solution()
print(so.maxRectangleArea(xCoord = [1,1,3,3], yCoord = [1,3,1,3]))
print(so.maxRectangleArea(xCoord = [89,55,89,55,0,34,17,71,98,90,63,49,76,72,4,46,67,94,52,6], yCoord = [58,69,69,58,100,36,14,40,13,41,29,23,47,52,95,49,37,77,54,59]))
print(so.maxRectangleArea(xCoord = [1,1,3,3,2], yCoord = [1,3,1,3,2]))




