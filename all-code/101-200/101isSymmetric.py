class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isSame(root.left, root.right)
    def isSame(self, left, right):
        if left is None and right is None:
            return True
        elif left is not None and right is not None:
            if left.val != right.val:
                return False
            return self.isSame(left.left, right.right) and self.isSame(left.right, right.left)
        else:
            return False



root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

so = Solution()
print(so.isBalanced(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.right.left = TreeNode(3)
root.right.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(4)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(4)
root.right.left.left = TreeNode(4)
root.right.left.right = TreeNode(4)
root.left.left.left.left = TreeNode(5)
root.left.left.left.right = TreeNode(5)
print(so.isBalanced(root))