# 当 k 个日程安排有一些时间上的交叉时（例如 k 个日程安排都在同一时间内），就会产生 k 次预订。
#
# 给你一些日程安排 [start, end) ，请你在每个日程安排添加后，返回一个整数 k ，表示所有先前日程安排会产生的最大 k 次预订。
#
# 实现一个 MyCalendarThree 类来存放你的日程安排，你可以一直添加新的日程安排。
#
# MyCalendarThree() 初始化对象。
# int book(int start, int end) 返回一个整数 k ，表示日历中存在的 k 次预订的最大值。
# 
#
# 示例：
#
# 输入：
# ["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
# [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
# 输出：
# [null, 1, 1, 2, 3, 3, 3]
#
# 解释：
# MyCalendarThree myCalendarThree = new MyCalendarThree();
# myCalendarThree.book(10, 20); // 返回 1 ，第一个日程安排可以预订并且不存在相交，所以最大 k 次预订是 1 次预订。
# myCalendarThree.book(50, 60); // 返回 1 ，第二个日程安排可以预订并且不存在相交，所以最大 k 次预订是 1 次预订。
# myCalendarThree.book(10, 40); // 返回 2 ，第三个日程安排 [10, 40) 与第一个日程安排相交，所以最大 k 次预订是 2 次预订。
# myCalendarThree.book(5, 15); // 返回 3 ，剩下的日程安排的最大 k 次预订是 3 次预订。
# myCalendarThree.book(5, 10); // 返回 3
# myCalendarThree.book(25, 55); // 返回 3
# 
#
# 提示：
#
# 0 <= start < end <= 109
# 每个测试用例，调用 book函数最多不超过400次


from typing import List
class MyCalendarThree:

    def __init__(self):
        self.sections = []
        self.max_num = 0


    def book(self, start: int, end: int) -> int:
        print(self.sections)
        if len(self.sections) == 0:
            self.sections.append([start, end, 1])
            self.max_num += 1
            return self.max_num
        idx = 0
        while idx < len(self.sections):
            if end <= self.sections[idx][0]:
                self.sections.insert(idx, [start, end, 1])
                return self.max_num
            if start >= self.sections[idx][1]:
                idx += 1
                if idx >= len(self.sections):
                    self.sections.append([start, end, 1])
                    return self.max_num
                continue
            [left, right, high] = self.sections[idx]
            del self.sections[idx]
            if start <= left:
                if start < left:
                    self.sections.insert(idx, [start, left, 1])
                    idx += 1
                if end <= right:
                    self.sections.insert(idx, [left, end, high + 1])
                    idx += 1
                    if end < right:
                        self.sections.insert(idx, [end, right, high])
                    self.max_num = max(self.max_num, high + 1)
                    return self.max_num
                else:
                    self.sections.insert(idx, [left, right, high + 1])
                    # self.sections.insert(idx + 2, [right, end, 1])
                    idx += 1
                    self.max_num = max(self.max_num, high + 1)
                    start = right
            else:
                self.sections.insert(idx, [left, start, high])
                idx += 1
                if end <= right:
                    self.sections.insert(idx, [start, end, high + 1])
                    idx += 1
                    if end < right:
                        self.sections.insert(idx, [end, right, high])
                    self.max_num = max(self.max_num, high + 1)
                    return self.max_num
                else:
                    self.sections.insert(idx, [start, right, high + 1])
                    # self.sections.insert(idx + 2, [right, end, 1])
                    idx += 1
                    self.max_num = max(self.max_num, high + 1)
                    start = right
            if idx >= len(self.sections):
                self.sections.insert(idx, [start, end, 1])
                break
        return self.max_num




so = MyCalendarThree()
print(so.book(1, 13))
print(so.book(59,71))
print(so.book(31,42))
print(so.book(2,21))
print(so.book(51,63))
print(so.book(79,89))
print(so.book(5,18))
print(so.book(83,100))
print(so.book(33,49))
print(so.book(77,94))
print(so.book(89,99))
print(so.book(19,31))
print(so.book(29,45))
print(so.book(18,35))
print(so.book(62,74))
print(so.book(35,51))
print(so.book(11,27))
print(so.book(95,100))
print(so.book(95,100))
print(so.book(71,87))
print(so.book(25,44))
print(so.book(51,62))
print(so.book(88,100))
print(so.book(53,67))
print(so.book(17,27))
print(so.book(95,100))

# print(so.book(98,100))


so = MyCalendarThree()
print(so.book(10, 20))
print(so.book(50, 60))
print(so.book(10, 40))
print(so.book(5, 15))
print(so.book(5, 10))
print(so.book(25, 55))

