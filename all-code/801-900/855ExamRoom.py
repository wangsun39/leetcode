# 在考场里，一排有 N 个座位，分别编号为 0, 1, 2, ..., N-1 。
#
# 当学生进入考场后，他必须坐在能够使他与离他最近的人之间的距离达到最大化的座位上。如果有多个这样的座位，他会坐在编号最小的座位上。(另外，如果考场里没有人，那么学生就坐在 0 号座位上。)
#
# 返回 ExamRoom(int N) 类，它有两个公开的函数：其中，函数 ExamRoom.seat() 会返回一个 int （整型数据），代表学生坐的位置；函数 ExamRoom.leave(int p) 代表坐在座位 p 上的学生现在离开了考场。每次调用 ExamRoom.leave(p) 时都保证有学生坐在座位 p 上。
#
#
#
# 示例：
#
# 输入：["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
# 输出：[null,0,9,4,2,null,5]
# 解释：
# ExamRoom(10) -> null
# seat() -> 0，没有人在考场里，那么学生坐在 0 号座位上。
# seat() -> 9，学生最后坐在 9 号座位上。
# seat() -> 4，学生最后坐在 4 号座位上。
# seat() -> 2，学生最后坐在 2 号座位上。
# leave(4) -> null
# seat() -> 5，学生最后坐在 5 号座位上。
#
#
# 提示：
#
# 1 <= N <= 10^9
# 在所有的测试样例中 ExamRoom.seat() 和 ExamRoom.leave() 最多被调用 10^4 次。
# 保证在调用 ExamRoom.leave(p) 时有学生正坐在座位 p 上。
import bisect
from functools import lru_cache
import heapq

class ExamRoom:

    def __init__(self, n: int):
        # self.num = 0
        self.n = n
        self.arr = [[-n, 0, (n - 1)]]  # [-空闲区间长度，区间左端点，区间右端点] ,arr是有序的
        # 如果[0, x] 或 [x, n - 1]，第一个字段的值为整个空闲区间的长度，因为0 和 n - 1是最远的点，
        # 其他区间都是区间长度的一半是最远距离
        self.d = {}  # idx: [左边第一个非空闲点, 右边第一个非空闲点]


    def seat(self) -> int:
        l, r = self.arr[0][1], self.arr[0][2]
        if l == 0:
            new = [-r // 2, 1, r] if r < self.n - 1 else [-r, 1, r]
            self.arr = self.arr[1:]
            if new[0] < 0:  # 更新后的空闲区间长度为正
                bisect.insort_left(self.arr, new)
            self.d[0] = [-1, r + 1]
            if r + 1 < self.n:
                self.d[r + 1][0] = 0
            return 0
        if r == self.n - 1:
            new = [-(self.n - l - 1) // 2, l, self.n - 2] if l > 0 else [-(self.n - l - 1), l, self.n - 2]
            self.arr = self.arr[1:]
            if new[0] < 0:  # 更新后的空闲区间长度为正
                bisect.insort_left(self.arr, new)
            self.d[self.n - 1] = [l - 1, self.n]
            if l - 1 >= 0:
                self.d[l - 1][1] = self.n - 1
            return self.n - 1
        mid = (l + r) // 2
        if l == 0:
            n1 = [-(mid - l), l, mid - 1]
        else:
            n1 = [-(mid - l) // 2, l, mid - 1]
        if r == self.n - 1:
            n2 = [-(r - mid), mid + 1, r]
        else:
            n2 = [-(r - mid) // 2, mid + 1, r]
        self.arr = self.arr[1:]
        if n1[0] < 0:
            bisect.insort_left(self.arr, n1)
        if n2[0] < 0:
            bisect.insort_left(self.arr, n2)
        self.d[mid] = [l - 1, r + 1]
        if l - 1 >= 0:
            self.d[l - 1][1] = mid
        if r + 1 < self.n:
            self.d[r + 1][0] = mid
        return mid



    def leave(self, p: int) -> None:
        l, r = self.d[p]
        if l + 1 == 0:
            s1 = [-(p - 1 - l), l + 1, p - 1]
        else:
            s1 = [-(p - 1 - l) // 2, l + 1, p - 1]
        if r - 1 == self.n - 1:
            s2 = [-(r - 1 - p), p + 1, r - 1]
        else:
            s2 = [-(r - 1 - p) // 2, p + 1, r - 1]
        if s1[0] < 0 < p:
            p1 = bisect.bisect_left(self.arr, s1)
            self.arr = self.arr[:p1] + self.arr[p1 + 1:]
        if p < self.n and s2[0] < 0:
            p2 = bisect.bisect_left(self.arr, s2)
            self.arr = self.arr[:p2] + self.arr[p2 + 1:]
        new = [-(r - 1 - l), l + 1, r - 1] if l + 1 == 0 or r - 1 == self.n - 1 else [-(r - 1 - l) // 2, l + 1, r - 1]
        bisect.insort_left(self.arr, new)
        if l >= 0:
            self.d[l][1] = r
        if r < self.n:
            self.d[r][0] = l
        del(self.d[p])


so = ExamRoom(8)

print(so.seat())  # 0
print(so.seat())  # 7
print(so.seat())  # 3
print(so.leave(0))
print(so.leave(7))
print(so.d)
print(so.arr)
print(so.seat())  # 7
print(so.seat())  # 0
print(so.seat())  #
print(so.seat())  #
print(so.seat())  #
print(so.seat())  #
print(so.seat())  #
# print(so.seat())  #


# so = ExamRoom(10)
#
# print(so.seat())  # 0
# print(so.seat())  # 9
# print(so.seat())  # 4
# print(so.leave(0))
# print(so.leave(4))
# print(so.seat())  # 2
# print(so.d)
# print(so.arr)
# print(so.leave(4))
# print(so.d)
# print(so.arr)
# print(so.seat())  # 5



