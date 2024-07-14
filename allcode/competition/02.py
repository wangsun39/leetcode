

from leetcode.allcode.competition.mypackage import *

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        l1 = []
        cur = head
        while cur:
            if cur.val not in nums:
                l1.append(cur)
            cur = cur.next
        if len(l1) == 0:
            return None
        head = l1[0]
        cur = head
        for x in l1[1:]:
            cur.next = x
            cur = cur.next
        return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

so = Solution()
print(so.modifiedList([1,2,3], head))




