class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cur = head
        res = 0
        while cur is not None:
            res *= 2
            res += cur.val
            cur = cur.next
        return res



node = ListNode(1)
node.next = ListNode(0)
node.next.next = ListNode(0)
obj = Solution()
print(obj.getDecimalValue( node))

