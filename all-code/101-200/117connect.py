class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        if root is None:
            return None
        queue = [root, None]
        while len(queue) > 1:
            cur = queue.pop(0)
            if cur is None:
                queue.append(None)
                continue
            cur.next = queue[0]
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)
        return root


z = Node(1)
z.left = Node(2)
z.right = Node(3)
z.left.left = Node(4)
z.left.right = Node(5)
z.right.left = Node(6)
z.right.right = Node(7)
so = Solution()
print(so.connect(z))

