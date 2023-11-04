from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect1(self, root):
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

    def connect(self, root: 'Node') -> 'Node':
        # 2023/10/3 update BFS
        q1, q2 = deque(), deque()
        if root:
            q1.append(root)
        while q1:
            while q1:
                x = q1.popleft()
                if q1:
                    x.next = q1[0]
                if x.left:
                    q2.append(x.left)
                if x.right:
                    q2.append(x.right)
            q1, q2 = q2, deque()
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

