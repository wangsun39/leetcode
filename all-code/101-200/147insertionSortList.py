# 对链表进行插入排序。
#
#
# 插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
# 每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。
#
#  
#
# 插入排序算法：
#
# 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
# 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
# 重复直到所有输入数据插入完为止。
#  
#
# 示例 1：
#
# 输入: 4->2->1->3
# 输出: 1->2->3->4
# 示例 2：
#
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5


from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        def findPos(node):
            cur = head
            while cur.next is not None:
                if cur.next.val < node.val:
                    cur = cur.next
                else:
                    break
            return cur

        if head is None or head.next is None:
            return head
        cur = head.next
        head.next = None
        while cur is not None:
            if cur.val < head.val:
                t1, t2 = head, cur.next
                head = cur
                head.next = t1
                cur = t2
                continue
            pos = findPos(cur)
            t1, t2 = pos.next, cur.next
            pos.next = cur
            cur.next = t1
            cur = t2
        return head




so = Solution()

z = ListNode(-1)
z.next = ListNode(5)
z.next.next = ListNode(3)
z.next.next.next = ListNode(4)
z.next.next.next.next = ListNode(0)
print(so.insertionSortList(z))

z = ListNode(4)
z.next = ListNode(2)
z.next.next = ListNode(1)
z.next.next.next = ListNode(3)
print(so.insertionSortList(z))
