# 实现一个 MyCalendar 类来存放你的日程安排。如果要添加的时间内不会导致三重预订时，则可以存储这个新的日程安排。
#
# MyCalendar 有一个 book(int start, int end)方法。它意味着在 start 到 end 时间内增加一个日程安排，注意，这里的时间是半开区间，即 [start, end), 实数 x 的范围为，  start <= x < end。
#
# 当三个日程安排有一些时间上的交叉时（例如三个日程安排都在同一时间内），就会产生三重预订。
#
# 每次调用 MyCalendar.book方法时，如果可以将日程安排成功添加到日历中而不会导致三重预订，返回 true。否则，返回 false 并且不要将该日程安排添加到日历中。
#
# 请按照以下步骤调用MyCalendar 类: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
#
#  
#
# 示例：
#
# MyCalendar();
# MyCalendar.book(10, 20); // returns true
# MyCalendar.book(50, 60); // returns true
# MyCalendar.book(10, 40); // returns true
# MyCalendar.book(5, 15); // returns false
# MyCalendar.book(5, 10); // returns true
# MyCalendar.book(25, 55); // returns true
# 解释：
# 前两个日程安排可以添加至日历中。 第三个日程安排会导致双重预订，但可以添加至日历中。
# 第四个日程安排活动（5,15）不能添加至日历中，因为它会导致三重预订。
# 第五个日程安排（5,10）可以添加至日历中，因为它未使用已经双重预订的时间10。
# 第六个日程安排（25,55）可以添加至日历中，因为时间 [25,40] 将和第三个日程安排双重预订；
# 时间 [40,50] 将单独预订，时间 [50,55）将和第二个日程安排双重预订。
#  
#
# 提示：
#
# 每个测试用例，调用 MyCalendar.book 函数最多不超过 1000次。
# 调用函数 MyCalendar.book(start, end)时， start 和 end 的取值范围为 [0, 10^9]。



from typing import List
from collections import defaultdict

class MyCalendarTwo:

    def __init__(self):
        self.tree = defaultdict(int)  # 区间上最大的重复预定次数
        self.lazy = defaultdict(int)  # 区间上需要向下传递但没有传递的“全区间”预定次数

    def pushup(self, id: int):
        self.tree[id] = max(self.tree[id << 1], self.tree[(id << 1) | 1])

    def pushdown(self, id: int):
        if 0 == self.lazy[id]:
            return
        left, right = id << 1, (id << 1) | 1
        self.tree[left] += self.lazy[id]
        self.tree[right] += self.lazy[id]
        self.lazy[left] += self.lazy[id]
        self.lazy[right] += self.lazy[id]
        self.lazy[id] = 0


    def update(self, id: int, start: int, end: int, l: int, r: int):
        if start > r or end < l:
            return
        if start >= l and end <= r:
            self.tree[id] += 1
            # self.lazy[id] = self.tree[id]
            self.lazy[id] += 1
            return
        mid = (start + end) >> 1
        self.pushdown(id)
        self.update(id << 1, start, mid, l, r)
        self.update((id << 1) | 1, mid + 1, end, l, r)
        self.pushup(id)

    def check(self, id: int, start: int, end: int, l: int, r: int):
        if start > r or end < l:
            return True
        if start >= l and end <= r:
            return self.tree[id] < 2
        mid = (start + end) >> 1
        self.pushdown(id)
        left = self.check(id << 1, start, mid, l, r)
        if not left:
            return False
        return self.check((id << 1) | 1, mid + 1, end, l, r)


    def book(self, start: int, end: int) -> bool:
        if self.check(1, 0, int(1e9), start, end - 1):
            self.update(1, 0, int(1e9), start, end - 1)
            return True
        return False


so = MyCalendarTwo()
print(so.book(10,20))
# print(so.book(50,60))
print(so.book(10,40))
print(so.book(5, 15))
print(so.book(25, 55))

so = MyCalendarTwo()
print(so.book(42,50))
print(so.book(38,43))
print(so.book(41, 49))

so = MyCalendarTwo()
print(so.book(10, 20))
print(so.book(50, 60))
print(so.book(10, 40))
print(so.book(5, 15))
print(so.book(5, 10))
print(so.book(25, 55))


# print(so.book(98,100))


