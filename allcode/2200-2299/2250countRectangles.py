# 给你一个二维整数数组 rectangles ，其中 rectangles[i] = [li, hi] 表示第 i 个矩形长为 li 高为 hi 。给你一个二维整数数组 points ，其中 points[j] = [xj, yj] 是坐标为 (xj, yj) 的一个点。
#
# 第 i 个矩形的 左下角 在 (0, 0) 处，右上角 在 (li, hi) 。
#
# 请你返回一个整数数组 count ，长度为 points.length，其中 count[j]是 包含 第 j 个点的矩形数目。
#
# 如果 0 <= xj <= li 且 0 <= yj <= hi ，那么我们说第 i 个矩形包含第 j 个点。如果一个点刚好在矩形的 边上 ，这个点也被视为被矩形包含。
#
#
#
# 示例 1：
#
#
#
# 输入：rectangles = [[1,2],[2,3],[2,5]], points = [[2,1],[1,4]]
# 输出：[2,1]
# 解释：
# 第一个矩形不包含任何点。
# 第二个矩形只包含一个点 (2, 1) 。
# 第三个矩形包含点 (2, 1) 和 (1, 4) 。
# 包含点 (2, 1) 的矩形数目为 2 。
# 包含点 (1, 4) 的矩形数目为 1 。
# 所以，我们返回 [2, 1] 。
# 示例 2：
#
#
#
# 输入：rectangles = [[1,1],[2,2],[3,3]], points = [[1,3],[1,1]]
# 输出：[1,3]
# 解释：
# 第一个矩形只包含点 (1, 1) 。
# 第二个矩形只包含点 (1, 1) 。
# 第三个矩形包含点 (1, 3) 和 (1, 1) 。
# 包含点 (1, 3) 的矩形数目为 1 。
# 包含点 (1, 1) 的矩形数目为 3 。
# 所以，我们返回 [1, 3] 。
#
#
# 提示：
#
# 1 <= rectangles.length, points.length <= 5 * 104
# rectangles[i].length == points[j].length == 2
# 1 <= li, xj <= 109
# 1 <= hi, yj <= 100
# 所有 rectangles 互不相同 。
# 所有 points 互不相同 。

from leetcode.allcode.competition.mypackage import *

class Solution1:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        # 二分的解法很简洁
        row = defaultdict(list)
        for x, y in rectangles:
            row[y].append(x)
        for l in row.values():
            l.sort()
        ans = []
        for x, y in points:
            res = 0
            for k, l in row.items():
                if k >= y:
                    p = bisect_left(l, x)
                    res += (len(l) - p)
            ans.append(res)
        return ans

class Fenwick:
    # 所有函数参数下标从1开始，可以传入使用者的数值x+1的值
    __slots__ = ['f', 'nums']

    def __init__(self, n: int):
        # n 是能调用下面函数的下标最大值
        self.f = [0] * (n + 1)  # 关键区间
        self.nums = [0] * (n + 1)

    def add(self, i: int, val: int) -> None:  # nums[i] += val
        self.nums[i] += val
        while i < len(self.f):
            self.f[i] += val
            i += i & -i

    def update(self, i: int, val: int) -> None:  # nums[i] += val
        delta = val - self.nums[i]
        self.add(i, delta)

    def pre(self, i: int) -> int:  # 下标<=i的和
        res = 0
        while i > 0:
            res += self.f[i]
            i &= i - 1
        return res

    def query_one(self, idx: int):
        return self.nums[idx]

    def query(self, l: int, r: int) -> int:  # [l, r]  区间求和
        if r < l:
            return 0
        return self.pre(r) - self.pre(l - 1)


class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        n = len(points)
        ans = [0] * n
        array = []
        for x, y in rectangles:
            array.append([x, y, -1])
        for i, [x, y] in enumerate(points):
            array.append([x, y, i])
        array.sort(key=lambda x: [-x[0], -x[1], x[2]])  # 把矩形和点放在一个数组中排序，按x坐标排序，相同的点矩形放在前面
        # 按x轴排序，按y轴构造树状数组，
        fw = Fenwick(100)  # y坐标的长度
        for x, y, idx in array:
            if idx == -1:
                fw.add(y, 1)
            else:
                v = fw.query(y, 100)  # 查询后缀和
                ans[idx] = v
        return ans

so = Solution()
print(so.countRectangles(rectangles = [[1,2],[2,3],[2,5]], points = [[2,1],[1,4]]))
print(so.countRectangles([[1,1],[2,2],[3,3]], points = [[1,3],[1,1]]))




