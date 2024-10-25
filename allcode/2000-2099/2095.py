

from leetcode.allcode.competition.mypackage import *

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        cur = head
        while cur:
            l.append(cur.val)
            cur = cur.next
        n = len(l)
        if n == 1: return None
        if n == 2: return ListNode(l[1])
        ans = cur = ListNode(l[0])
        for i in range(1, n):
            if i == n // 2: continue
            cur.next = ListNode(l[i])
            cur = cur.next
        return ans



so = Solution()
print(so.deleteMiddle())




