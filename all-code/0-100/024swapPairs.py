# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
#
#  
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
# 示例 2：
#
# 输入：head = []
# 输出：[]
# 示例 3：
#
# 输入：head = [1]
# 输出：[1]
#  
#
# 提示：
#
# 链表中节点的数目在范围 [0, 100] 内
# 0 <= Node.val <= 100

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        cur = head
        head = head.next
        while cur and cur.next:
            nncur = cur.next.next
            cur.next.next = cur
            if nncur is None or nncur.next is None:
                cur.next = nncur
                break
            cur.next = nncur.next
            cur = nncur
        return head






so = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
print(so.swapPairs(head))
