from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(node: TreeNode):
            if node.left is None:
                return helper(node.right) if node.right is not None else node
            if node.right is None:
                node.right = node.left
                node.left = None
                return helper(node.right)
            left_last_leaf = helper(node.left)
            left_last_leaf.right = node.right
            node.right = node.left
            node.left = None
            return helper(left_last_leaf.right) # if left_last_leaf.right is not None else node
        if root is None:
            return
        helper(root)
        return


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
so = Solution()
print(so.flatten(root))

# root = TreeNode(10)
# root.left = TreeNode(5)
# root.left = TreeNode(15)
# root.left.left = TreeNode(6)
# root.left.left = TreeNode(20)
# so = Solution()
# print(so.flatten(root))

