class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getDepthAndBal(self, root, depth):
        if root.left is None:
            depth_l = depth
        else:
            ret, depth_l = self.getDepthAndBal(root.left, depth + 1)
            if not ret:
                return False, 0
        if root.right is None:
            depth_r = depth
        else:
            ret, depth_r = self.getDepthAndBal(root.right, depth + 1)
            if not ret:
                return False, 0
        return (abs(depth_l - depth_r) <= 1), max(depth_l, depth_r)

    def isBalanced(self, root):
        if root is None:
            return True
        ret, depth = self.getDepthAndBal(root, 1)
        return ret



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