# 给定单链表的头节点 head ，将所有索引为奇数的节点和索引为偶数的节点分别组合在一起，然后返回重新排序的列表。
#
# 第一个节点的索引被认为是 奇数 ， 第二个节点的索引为 偶数 ，以此类推。
#
# 请注意，偶数组和奇数组内部的相对顺序应该与输入时保持一致。
#
# 你必须在 O(1) 的额外空间复杂度和 O(n) 的时间复杂度下解决这个问题。
#
#
#
# 示例 1:
#
#
#
# 输入: head = [1,2,3,4,5]
# 输出: [1,3,5,2,4]
# 示例 2:
#
#
#
# 输入: head = [2,1,3,5,6,4,7]
# 输出: [2,3,6,7,1,5,4]
#
#
# 提示:
#
# n ==  链表中的节点数
# 0 <= n <= 104
# -106 <= Node.val <= 106

from leetcode.allcode.competition.mypackage import *

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        o1 = head
        e1 = head.next
        o2 = head
        e2 = head.next
        cur = head.next.next
        o_flg = True
        while cur:
            if o_flg:
                o2.next = cur
                o2 = o2.next
            else:
                e2.next = cur
                e2 = e2.next
            o_flg = not o_flg
            cur = cur.next
        o2.next = e1
        e2.next = None
        return o1

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

so = Solution()
print(so.oddEvenList(head))
