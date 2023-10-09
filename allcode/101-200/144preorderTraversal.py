class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root):
        stack = []
        final = []
        if root is None:
            return final
        cur = root
        stack.append(cur)
        final.append(cur.val)
        while cur is not None:
            if cur.left is not None:
                stack.append(cur.left)
                final.append(cur.left.val)
                cur = cur.left
                continue
            cur = stack.pop()
            while cur is not None and cur.right is None:
                cur = stack.pop() if len(stack) > 0 else None
            if cur is None:
                return final
            stack.append(cur.right)
            final.append(cur.right.val)
            cur = cur.right

