# 给你一个数组 rectangles ，其中 rectangles[i] = [xi, yi, ai, bi] 表示一个坐标轴平行的矩形。这个矩形的左下顶点是 (xi, yi) ，右上顶点是 (ai, bi) 。
#
# 如果所有矩形一起精确覆盖了某个矩形区域，则返回 true ；否则，返回 false 。
#
#
# 示例 1：
#
#
# 输入：rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
# 输出：true
# 解释：5 个矩形一起可以精确地覆盖一个矩形区域。
# 示例 2：
#
#
# 输入：rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
# 输出：false
# 解释：两个矩形之间有间隔，无法覆盖成一个矩形。
# 示例 3：
#
#
# 输入：rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
# 输出：false
# 解释：因为中间有相交区域，虽然形成了矩形，但不是精确覆盖。
#
#
# 提示：
#
# 1 <= rectangles.length <= 2 * 104
# rectangles[i].length == 4
# -105 <= xi < ai <= 105
# -105 <= yi < bi <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def isRectangleCover1(self, rectangles: List[List[int]]) -> bool:
        # 二维差分的正确性是可以的，但性能不行
        mn_x, mn_y = min(a for a, _, _, _ in rectangles), min(b for _, b, _, _ in rectangles)
        rectangles = [[a - mn_x, b - mn_y, c - mn_x, d - mn_y] for a, b, c, d in rectangles]

        r, c = max(a for _, _, a, _ in rectangles) + 1, max(b for _, _, _, b in rectangles) + 1
        # 二维差分模板
        diff = [[0] * (c + 1) for _ in range(r + 1)]
        for r1, c1, r2, c2 in rectangles:
            # 构造 左闭右开的区间
            if r2 + 1 < r:
                r2 -= 1
            if c2 + 1 < c:
                c2 -= 1
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1

        # 用二维前缀和复原原始二维数组s
        s = [[0] * (c + 1) for _ in range(r + 1)]
        for i in range(r):
            for j in range(c):
                s[i + 1][j + 1] += s[i + 1][j] + s[i][j + 1] - s[i][j] + diff[i][j]
                if s[i + 1][j + 1] != 1:
                    return False
        return True

    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        mn_x, mn_y = min(a for a, _, _, _ in rectangles), min(b for _, b, _, _ in rectangles)
        mx_x, mx_y = max(a for _, _, a, _ in rectangles), max(b for _, _, _, b in rectangles)
        s1 = (mx_y - mn_y) * (mx_x - mn_x)
        s2 = 0
        for a, b, c, d in rectangles:
            s2 += (d - b) * (c - a)
        if s1 != s2: return False
        rectangles.sort()  # 按矩形左侧x坐标排序
        que = SortedList()  # 按矩形上边缘y坐标排序
        def overlap1(n1, n2):  # 区间重叠
            if n1[0] >= n2[1] or n1[1] <= n2[0]: return False
            return True
        def overlap2(n1, n2):  # 矩形重叠
            return overlap1([n1[0], n1[2]], [n2[0], n2[2]]) and overlap1([n1[1], n1[3]], [n2[1], n2[3]])

        for i, [a, b, c, d] in enumerate(rectangles):
            # 有点类似从左到右一层层扫描，遇到在y轴上有重叠的部分，进行检查，如果两矩形重叠则返回，否则把左侧的矩形删除
            p = que.bisect_left([b, inf])
            while p < len(que) and overlap1([b, d], [rectangles[que[p][1]][1], rectangles[que[p][1]][3]]):
                if overlap2([a, b, c, d], rectangles[que[p][1]]):
                    return False
                else:
                    que.pop(p)
            que.add([d, i])
        return True


so = Solution()
print(so.isRectangleCover(rectangles = [[0,0,2,1],[0,1,2,2],[0,2,1,3],[1,0,2,1]]))  # False
print(so.isRectangleCover(rectangles = [[0,0,2,2],[1,1,3,3],[2,0,3,1],[0,3,3,4]]))  # False
print(so.isRectangleCover(rectangles = [[0,0,1,1],[0,1,3,2],[1,0,2,2]]))  # False
print(so.isRectangleCover(rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]))  # True

