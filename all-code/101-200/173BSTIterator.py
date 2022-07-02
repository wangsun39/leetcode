import math
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        cur = root
        while cur is not None:
            self.stack.append(cur)
            cur = cur.left


    def next(self) -> int:
        """
        @return the next smallest number
        """
        res = self.stack.pop()
        cur = res.right
        while cur is not None:
            self.stack.append(cur)
            cur = cur.left
        return res.val


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return 0 != len(self.stack)

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(6)
root.right.right = TreeNode(20)
so = BSTIterator(root);
print(so.next())
print(so.next())
print(so.next())

