# 请你设计一个队列，支持在前，中，后三个位置的 push 和 pop 操作。
#
# 请你完成 FrontMiddleBack 类：
#
# FrontMiddleBack() 初始化队列。
# void pushFront(int val) 将 val 添加到队列的 最前面 。
# void pushMiddle(int val) 将 val 添加到队列的 正中间 。
# void pushBack(int val) 将 val 添加到队里的 最后面 。
# int popFront() 将 最前面 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 -1 。
# int popMiddle() 将 正中间 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 -1 。
# int popBack() 将 最后面 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 -1 。
# 请注意当有 两个 中间位置的时候，选择靠前面的位置进行操作。比方说：
#
# 将 6 添加到 [1, 2, 3, 4, 5] 的中间位置，结果数组为 [1, 2, 6, 3, 4, 5] 。
# 从 [1, 2, 3, 4, 5, 6] 的中间位置弹出元素，返回 3 ，数组变为 [1, 2, 4, 5, 6] 。
#
#
# 示例 1：
#
# 输入：
# ["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
# [[], [1], [2], [3], [4], [], [], [], [], []]
# 输出：
# [null, null, null, null, null, 1, 3, 4, 2, -1]
#
# 解释：
# FrontMiddleBackQueue q = new FrontMiddleBackQueue();
# q.pushFront(1);   // [1]
# q.pushBack(2);    // [1, 2]
# q.pushMiddle(3);  // [1, 3, 2]
# q.pushMiddle(4);  // [1, 4, 3, 2]
# q.popFront();     // 返回 1 -> [4, 3, 2]
# q.popMiddle();    // 返回 3 -> [4, 2]
# q.popMiddle();    // 返回 4 -> [2]
# q.popBack();      // 返回 2 -> []
# q.popFront();     // 返回 -1 -> [] （队列为空）
#
#
# 提示：
#
# 1 <= val <= 109
# 最多调用 1000 次 pushFront， pushMiddle， pushBack， popFront， popMiddle 和 popBack 。





from leetcode.allcode.competition.mypackage import *


class Node:
    def __init__(self, val, next=None, pre=None):
        self.val = val
        self.next = next
        self.pre = pre


class FrontMiddleBackQueue:

    def __init__(self):
        self.cnt = 0
        self.head = None
        self.tail = None
        self.mid = None

    def pushFront(self, val: int) -> None:
        if self.cnt == 0:
            self.head = self.tail = self.mid = Node(val)
            self.cnt += 1
            return

        self.head.pre = Node(val, self.head)
        self.head = self.head.pre
        if self.cnt & 1:
            self.mid = self.mid.pre
        self.cnt += 1

    def pushMiddle(self, val: int) -> None:
        if self.cnt == 0:
            self.head = self.tail = self.mid = Node(val)
            self.cnt += 1
            return
        if self.cnt & 1:
            self.mid = Node(val, self.mid, self.mid.pre)
            self.mid.next.pre = self.mid
            if self.mid.pre:
                self.mid.pre.next = self.mid
            else:
                self.head = self.mid
        else:
            self.mid = Node(val, self.mid.next, self.mid)
            self.mid.next.pre = self.mid
            self.mid.pre.next = self.mid

        self.cnt += 1

    def pushBack(self, val: int) -> None:
        if self.cnt == 0:
            self.head = self.tail = self.mid = Node(val)
            self.cnt += 1
            return
        self.tail.next = Node(val, pre=self.tail)
        self.tail = self.tail.next
        if self.cnt & 1 == 0:
            self.mid = self.mid.next
        self.cnt += 1

    def popFront(self) -> int:
        if self.cnt == 0:
            return -1
        ans = self.head.val
        if self.cnt == 1:
            self.head = self.tail = self.mid = None
        else:
            self.head = self.head.next
            if self.cnt & 1 == 0:
                self.mid = self.mid.next
            self.head.pre = None
        self.cnt -= 1
        return ans

    def popMiddle(self) -> int:
        if self.cnt == 0:
            return -1
        ans = self.mid.val
        if self.cnt == 1:
            self.head = self.tail = self.mid = None
        else:
            if self.mid.pre:
                self.mid.next.pre, self.mid.pre.next = self.mid.pre, self.mid.next
            else:
                self.mid.next.pre = self.mid.pre
                self.head = self.mid.next
            if self.cnt & 1:
                self.mid = self.mid.pre
            else:
                self.mid = self.mid.next
        self.cnt -= 1
        return ans

    def popBack(self) -> int:
        if self.cnt == 0:
            return -1
        ans = self.tail.val
        if self.cnt == 1:
            self.head = self.tail = self.mid = None
        else:
            self.tail = self.tail.pre
            self.tail.next = None
            if self.cnt & 1:
                self.mid = self.mid.pre
        self.cnt -= 1
        return ans

so = FrontMiddleBackQueue()
so.popMiddle()
so.pushMiddle(1)   # [1]
so.pushMiddle(2)   # [1]
so.popBack()
so.pushMiddle(2)   # [1]
so.pushBack(2)
so.popFront()
so.popFront()

so = FrontMiddleBackQueue()
so.pushFront(1)   # [1]
so.pushBack(2)    # [1, 2]
so.pushMiddle(3)  # [1, 3, 2]
so.pushMiddle(4)  # [1, 4, 3, 2]
so.popFront()     # 返回 1 -> [4, 3, 2]
so.popMiddle()    # 返回 3 -> [4, 2]
so.popMiddle()    # 返回 4 -> [2]
so.popBack()      # 返回 2 -> []
so.popFront()     # 返回 -1 -> [] （队列为空）

