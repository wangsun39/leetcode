

from leetcode.allcode.competition.mypackage import *

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        simu = ListNode(-1)  # 哨兵
        simu.next = head
        cur = head
        pre = simu
        before = None
        idx = 1
        while True:
            if before is None:
                if idx == left:
                    before = pre
                pre = cur
                cur = cur.next
            else:
                if idx == right:
                    # before.next, before.next.next, cur.next = cur, cur.next, pre
                    before.next.next = cur.next
                    before.next = cur
                    cur.next = pre
                    break
                else:
                    # pre, cur, cur.next = cur, cur.next, pre
                    a, b, c = cur, cur.next, pre
                    pre, cur = a, b
                    pre.next = c
            idx += 1
        return simu.next



head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

so = Solution()
print(so.reverseBetween(head, 2, 4))




