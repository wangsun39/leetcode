# 我们把无限数量 ∞ 的栈排成一行，按从左到右的次序从 0 开始编号。每个栈的的最大容量 capacity 都相同。
#
# 实现一个叫「餐盘」的类 DinnerPlates：
#
# DinnerPlates(int capacity) - 给出栈的最大容量 capacity。
# void push(int val) - 将给出的正整数 val 推入 从左往右第一个 没有满的栈。
# int pop() - 返回 从右往左第一个 非空栈顶部的值，并将其从栈中删除；如果所有的栈都是空的，请返回 -1。
# int popAtStack(int index) - 返回编号 index 的栈顶部的值，并将其从栈中删除；如果编号 index 的栈是空的，请返回 -1。
#
#
# 示例：
#
# 输入：
# ["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
# [[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
# 输出：
# [null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1]
#
# 解释：
# DinnerPlates D = DinnerPlates(2);  // 初始化，栈最大容量 capacity = 2
# D.push(1);
# D.push(2);
# D.push(3);
# D.push(4);
# D.push(5);         // 栈的现状为：    2  4
#                                     1  3  5
#                                     ﹈ ﹈ ﹈
# D.popAtStack(0);   // 返回 2。栈的现状为：      4
#                                           1  3  5
#                                           ﹈ ﹈ ﹈
# D.push(20);        // 栈的现状为：  20  4
#                                    1  3  5
#                                    ﹈ ﹈ ﹈
# D.push(21);        // 栈的现状为：  20  4 21
#                                    1  3  5
#                                    ﹈ ﹈ ﹈
# D.popAtStack(0);   // 返回 20。栈的现状为：       4 21
#                                             1  3  5
#                                             ﹈ ﹈ ﹈
# D.popAtStack(2);   // 返回 21。栈的现状为：       4
#                                             1  3  5
#                                             ﹈ ﹈ ﹈
# D.pop()            // 返回 5。栈的现状为：        4
#                                             1  3
#                                             ﹈ ﹈
# D.pop()            // 返回 4。栈的现状为：    1  3
#                                            ﹈ ﹈
# D.pop()            // 返回 3。栈的现状为：    1
#                                            ﹈
# D.pop()            // 返回 1。现在没有栈。
# D.pop()            // 返回 -1。仍然没有栈。
#
#
# 提示：
#
# 1 <= capacity <= 20000
# 1 <= val <= 20000
# 0 <= index <= 100000
# 最多会对 push，pop，和 popAtStack 进行 200000 次调用。




from typing import List, Optional
from collections import deque

from sortedcontainers import SortedList, SortedSet


class DinnerPlates:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.idle = SortedSet()  # 记录有空余空间的栈的位置
        self.busy = SortedSet()  # 记录有元素的栈的位置
        self.stack = []


    def push(self, val: int) -> None:
        if len(self.idle) == 0:
            idx = len(self.stack)
            self.idle.add(idx)
            self.stack.append([])
        else:
            idx = self.idle[0]

        self.stack[idx].append(val)
        if len(self.stack[idx]) >= self.cap:
            self.idle.remove(idx)

        self.busy.add(idx)
        return


    def pop(self) -> int:
        if len(self.busy) == 0: return -1
        idx = self.busy[-1]
        ans = self.stack[idx].pop()
        if len(self.stack[idx]) == 0:
            self.busy.remove(idx)
        self.idle.add(idx)
        return ans



    def popAtStack(self, index: int) -> int:
        if index >= len(self.stack) or len(self.stack[index]) == 0: return -1
        ans = self.stack[index].pop()
        if len(self.stack[index]) == 0:
            self.busy.remove(index)
        self.idle.add(index)
        return ans



# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)



obj = DinnerPlates(2)
print(obj.push(1))
print(obj.push(2))
print(obj.push(3))
print(obj.push(4))
print(obj.push(5))
print(obj.popAtStack(0))
print(obj.push(20))
print(obj.push(21))
print(obj.popAtStack(0))
print(obj.popAtStack(2))
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())


