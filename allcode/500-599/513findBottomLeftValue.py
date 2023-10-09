class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        self.maxLevel = 1
        self.node = root
        self.findOneNode(root, 1)
        return self.node.val

    def findOneNode(self, node, level):
        if node.left is None and node.right is None:
            if self.maxLevel < level:
                self.maxLevel = level
                self.node = node
            return
        if node.left is not None:
            self.findOneNode(node.left, level + 1)
        if node.right is not None:
            self.findOneNode(node.right, level + 1)


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)

so = Solution()
print(so.kthSmallest(root, 3))

