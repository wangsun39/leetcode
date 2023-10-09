class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteNode(self, node):
        print(id(node))
        # node = node.next
        print(id(node))
        node.val = node.next.val
        node.next = node.next.next
        print(id(node))



head = ListNode(5)
head.next = ListNode(3)
print(id(head))
so = Solution()
print(so.deleteNode(head))
print(head.val)

a = 1
print(10, id(a))
def f(a):
    print(id(a))
    print(a)
    a = 2
    print(id(a))
f(a)
print(a)
