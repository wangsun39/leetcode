from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        if root.left is not None and self.hasPathSum(root.left, sum - root.val):
            return True
        if root.right is not None and self.hasPathSum(root.right, sum - root.val):
            return True
        return root.left is None and root.right is None and sum == root.val

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(6)
root.right.right = TreeNode(20)
so = Solution()
print(so.hasPathSum(root, 31))
print(so.hasPathSum(root, 30))

root = TreeNode(1)
root.left = TreeNode(2)
print(so.hasPathSum(root, 1))

