# 设计一个最大栈数据结构，既支持栈操作，又支持查找栈中最大元素。
#
# 实现 MaxStack 类：
#
# MaxStack() 初始化栈对象
# void push(int x) 将元素 x 压入栈中。
# int pop() 移除栈顶元素并返回这个元素。
# int top() 返回栈顶元素，无需移除。
# int peekMax() 检索并返回栈中最大元素，无需移除。
# int popMax() 检索并返回栈中最大元素，并将其移除。如果有多个最大元素，只要移除 最靠近栈顶 的那个。
#
#
# 示例：
#
# 输入
# ["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
# [[], [5], [1], [5], [], [], [], [], [], []]
# 输出
# [null, null, null, null, 5, 5, 1, 5, 1, 5]
#
# 解释
# MaxStack stk = new MaxStack();
# stk.push(5);   // [5] - 5 既是栈顶元素，也是最大元素
# stk.push(1);   // [5, 1] - 栈顶元素是 1，最大元素是 5
# stk.push(5);   // [5, 1, 5] - 5 既是栈顶元素，也是最大元素
# stk.top();     // 返回 5，[5, 1, 5] - 栈没有改变
# stk.popMax();  // 返回 5，[5, 1] - 栈发生改变，栈顶元素不再是最大元素
# stk.top();     // 返回 1，[5, 1] - 栈没有改变
# stk.peekMax(); // 返回 5，[5, 1] - 栈没有改变
# stk.pop();     // 返回 1，[5] - 此操作后，5 既是栈顶元素，也是最大元素
# stk.top();     // 返回 5，[5] - 栈没有改变
#
#
# 提示：
#
# -107 <= x <= 107
# 最多调用 104 次 push、pop、top、peekMax 和 popMax
# 调用 pop、top、peekMax 或 popMax 时，栈中 至少存在一个元素
#
#
# 进阶：
#
# 试着设计解决方案：调用 top 方法的时间复杂度为 O(1) ，调用其他方法的时间复杂度为 O(logn) 。

from leetcode.allcode.competition.mypackage import *

class MaxStack:

    def __init__(self):
        self.stack = []
        self.hp = []
        self.del_st = defaultdict(list)  # 延迟删除标记，记录一个元素删除的时间
        self.del_hp = defaultdict(list)  # 延迟删除标记，记录一个元素删除的时间
        self.time = 0


    def push(self, x: int) -> None:
        self.stack.append([x, self.time])
        heappush(self.hp, [-x, -self.time])  # 注意这个地方两个都是负值很关键
        self.time += 1


    def pop(self) -> int:
        while len(self.del_st[self.stack[-1][0]]) > 0:
            x, t = self.stack[-1]
            if self.del_st[x][-1] >= t:
                self.del_st[x].pop()
                self.stack.pop()
            else:
                break
        x, _ = self.stack.pop()
        self.del_hp[x].append(self.time)
        self.time += 1
        return x


    def top(self) -> int:
        while len(self.del_st[self.stack[-1][0]]) > 0:
            x, t = self.stack[-1]
            if self.del_st[x][-1] >= t:
                self.del_st[x].pop()
                self.stack.pop()
            else:
                break
        return self.stack[-1][0]


    def peekMax(self) -> int:
        while len(self.del_hp[-self.hp[0][0]]) > 0:
            x, t = self.hp[0]
            if self.del_hp[-x][-1] >= -t:
                self.del_hp[-x].pop()
                heappop(self.hp)
            else:
                break
        return -self.hp[0][0]


    def popMax(self) -> int:
        while len(self.del_hp[-self.hp[0][0]]) > 0:
            x, t = self.hp[0]
            if self.del_hp[-x][-1] >= -t:
                self.del_hp[-x].pop()
                heappop(self.hp)
            else:
                break
        x, t = heappop(self.hp)
        self.del_st[-x].append(self.time)
        self.time += 1
        return -x

so = MaxStack()
print(so.push(69))
print(so.popMax())
print(so.push(-92))
print(so.pop())
print(so.push(-83))
print(so.push(-26))
print(so.pop())
print(so.push(69))
print(so.pop())
print(so.pop())


so = MaxStack()
print(so.push(5))
print(so.push(1))
print(so.push(5))
print(so.top())
print(so.popMax())
print(so.top())
print(so.peekMax())




