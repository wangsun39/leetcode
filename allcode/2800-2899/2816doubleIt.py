

from leetcode.allcode.competition.mypackage import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def trans(node):
            l = []
            while node:
                l.append(node.val)
                node = node.next
            return l
        ll = trans(head)[::-1]
        carry = 0
        for i, x in enumerate(ll):
            y = x * 2 + carry
            ll[i] = y % 10
            if y > 9:
                carry = 1
            else:
                carry = 0
        if carry > 0:
            ll.append(1)
        ll = ll[::-1]
        cur = head = ListNode(ll[0])
        for x in ll[1:]:
            cur.next = ListNode(x)
            cur = cur.next
        return head


t = ListNode(9)
t.next = ListNode(9)
t.next.next = ListNode(9)
so = Solution()
print(so.doubleIt(t))




