class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        def getLeaves(root):
            if root is None:
                return []
            if root.left is None and root.right is None:
                return [root.val]
            return getLeaves(root.left) + getLeaves(root.right)
        return getLeaves(root1) == getLeaves(root2)


so = Solution()


