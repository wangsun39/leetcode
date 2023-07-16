# 设计一个类似堆栈的数据结构，将元素推入堆栈，并从堆栈中弹出出现频率最高的元素。
#
# 实现 FreqStack 类:
#
# FreqStack() 构造一个空的堆栈。
# void push(int val) 将一个整数 val 压入栈顶。
# int pop() 删除并返回堆栈中出现频率最高的元素。
# 如果出现频率最高的元素不只一个，则移除并返回最接近栈顶的元素。
#
#
# 示例 1：
#
# 输入：
# ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
# [[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
# 输出：[null,null,null,null,null,null,null,5,7,5,4]
# 解释：
# FreqStack = new FreqStack();
# freqStack.push (5);//堆栈为 [5]
# freqStack.push (7);//堆栈是 [5,7]
# freqStack.push (5);//堆栈是 [5,7,5]
# freqStack.push (7);//堆栈是 [5,7,5,7]
# freqStack.push (4);//堆栈是 [5,7,5,7,4]
# freqStack.push (5);//堆栈是 [5,7,5,7,4,5]
# freqStack.pop ();//返回 5 ，因为 5 出现频率最高。堆栈变成 [5,7,5,7,4]。
# freqStack.pop ();//返回 7 ，因为 5 和 7 出现频率最高，但7最接近顶部。堆栈变成 [5,7,5,4]。
# freqStack.pop ();//返回 5 ，因为 5 出现频率最高。堆栈变成 [5,7,4]。
# freqStack.pop ();//返回 4 ，因为 4, 5 和 7 出现频率最高，但 4 是最接近顶部的。堆栈变成 [5,7]。
#
#
# 提示：
#
# 0 <= val <= 109
# push 和 pop 的操作数不大于 2 * 104。
# 输入保证在调用 pop 之前堆栈中至少有一个元素。


from typing import List
from collections import defaultdict
import bisect

class FreqStack:

    def __init__(self):
        self.l = []  # [time, idx]
        self.d1 = defaultdict(list)  # {num: [i1, i2,...]}  记录一个元素出现的下标
        self.cnt = 0  # push 的次数
        self.q = []

    def push(self, val: int) -> None:
        if len(self.d1[val]):
            t, i = len(self.d1[val]), self.d1[val][-1]
            pos = bisect.bisect_left(self.l, [t, i])
            del self.l[pos]
            self.d1[val].append(self.cnt)
            bisect.insort_left(self.l, [t + 1, self.cnt])
        else:
            self.d1[val].append(self.cnt)
            bisect.insort_left(self.l, [1, self.cnt])
        self.q.append(val)
        self.cnt += 1

    def pop(self) -> int:
        t, i = self.l[-1]
        num = self.q[i]
        pos = bisect.bisect_left(self.l, [t, i])
        del self.l[pos]
        self.d1[num].pop()
        if t > 1:
            bisect.insort_left(self.l, [t - 1, self.d1[num][-1]])
        return num



so = FreqStack()
so.push(5)
so.push(7)
so.push(5)
so.push(7)
so.push(4)
so.push(5)
print(so.pop())
print(so.pop())
print(so.pop())
print(so.pop())

