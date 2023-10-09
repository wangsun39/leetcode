from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        min_level = None
        def helper(node, level):
            nonlocal min_level
            if node is None:
                return
            if min_level is not None and level >= min_level:
                return
            if node.left is None and node.right is None:
                min_level = level
                return
            helper(node.left, level+1)
            helper(node.right, level+1)
        helper(root, 1)
        return min_level if min_level is not None else 0

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(6)
root.right.right = TreeNode(20)
so = Solution()
print(so.minDepth(root))
