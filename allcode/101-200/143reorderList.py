# 给定一个单链表 L 的头节点 head ，单链表 L 表示为：
#
# L0 → L1 → … → Ln - 1 → Ln
# 请将其重新排列后变为：
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# 不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
# 示例 1：
#
#
#
# 输入：head = [1,2,3,4]
# 输出：[1,4,2,3]
# 示例 2：
#
#
#
# 输入：head = [1,2,3,4,5]
# 输出：[1,5,2,4,3]
#
#
# 提示：
#
# 链表的长度范围为 [1, 5 * 104]
# 1 <= node.val <= 1000



from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l = []
        cur = head
        while cur:
            l.append(cur)
            cur = cur.next
        n = len(l)
        i, j = 0, n - 1
        cur = ListNode(0)
        head = cur
        while i < j:
            cur.next = l[i]
            cur = cur.next
            cur.next = l[j]
            cur = cur.next
            i += 1
            j -= 1
        if i == j:
            cur.next = l[i]
            cur = cur.next
        cur.next = None
        head = head.next
        return

h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)
h.next.next.next.next = ListNode(5)
so = Solution()
so.reorderList(h)


