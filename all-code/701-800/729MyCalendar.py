# 实现一个 MyCalendar 类来存放你的日程安排。如果要添加的日程安排不会造成 重复预订 ，则可以存储这个新的日程安排。
#
# 当两个日程安排有一些时间上的交叉时（例如两个日程安排都在同一时间内），就会产生 重复预订 。
#
# 日程可以用一对整数 start 和 end 表示，这里的时间是半开区间，即 [start, end), 实数 x 的范围为，  start <= x < end 。
#
# 实现 MyCalendar 类：
#
# MyCalendar() 初始化日历对象。
# boolean book(int start, int end) 如果可以将日程安排成功添加到日历中而不会导致重复预订，返回 true 。否则，返回 false 并且不要将该日程安排添加到日历中。
#  
#
# 示例：
#
# 输入：
# ["MyCalendar", "book", "book", "book"]
# [[], [10, 20], [15, 25], [20, 30]]
# 输出：
# [null, true, false, true]
#
# 解释：
# MyCalendar myCalendar = new MyCalendar();
# myCalendar.book(10, 20); // return True
# myCalendar.book(15, 25); // return False ，这个日程安排不能添加到日历中，因为时间 15 已经被另一个日程安排预订了。
# myCalendar.book(20, 30); // return True ，这个日程安排可以添加到日历中，因为第一个日程安排预订的每个时间都小于 20 ，且不包含时间 20 。
#  
#
# 提示：
#
# 0 <= start < end <= 109
# 每个测试用例，调用 book 方法的次数最多不超过 1000 次。


from typing import List
import bisect
class MyCalendar1:

    def __init__(self):
        self.starts = []
        self.ends = []


    def book(self, start: int, end: int) -> bool:
        pos = bisect.bisect_right(self.ends, start)
        if pos >= len(self.starts):
            self.starts.append(start)
            self.ends.append(end)
            return True
        if self.starts[pos] >= end:
            self.starts.insert(pos, start)
            self.ends.insert(pos, end)
            return True
        return False

from collections import defaultdict

class MyCalendar:
    def __init__(self):
        self.tree = defaultdict(int)  # 此区间是否有点被预定
        self.lazy = defaultdict(int)  # 此区间是否所有点都被预定了

    def update(self, id: int, start: int, end: int, l: int, r: int):
        if start > r or end < l:
            return
        if start >= l and end <= r:
            self.lazy[id] = 1
            return
        self.tree[id] = 1
        mid = (start + end) >> 1
        self.update(id << 1, start, mid, l, r)
        self.update((id << 1) | 1, mid + 1, end, l, r)

    def query(self, id: int, start: int, end: int, l: int, r: int):
        if start > r or end < l:
            return True
        if self.lazy[id] == 1:
            return False
        if start >= l and end <= r:
            if self.tree[id] == 1 or self.lazy[id] == 1:
                return False
            return True
        mid = (start + end) >> 1
        left = self.query(id << 1, start, mid, l, r)
        if not left:
            return False
        return self.query((id << 1) | 1, mid + 1, end, l, r)


    def book(self, left: int, right: int) -> bool:
        if self.query(1, 1, 10 ** 9, left, right - 1):
            self.update(1, 1, 10 ** 9, left, right - 1)
            return True
        return False
    # def book(self, left: int, right: int) -> bool:
    #     if self.query(1, 1, 100000, left, right - 1):
    #         self.update(1, 1, 100000, left, right - 1)
    #         return True
    #     return False


so = MyCalendar()
print(so.book(20, 29))
print(so.book(13, 22))

so = MyCalendar()
print(so.book(47, 50))
print(so.book(33, 41))
print(so.book(39, 45))

so = MyCalendar()
print(so.book(10, 20))
print(so.book(15, 25))
print(so.book(20, 30))

