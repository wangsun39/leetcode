class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getDepthAndBal1(self, root, depth):
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

    def isBalanced1(self, root):
        if root is None:
            return True
        ret, depth = self.getDepthAndBal(root, 1)
        return ret

    def isBalanced(self, root):
        # 2025/5/30 简化写法
        def dfs(node):
            if node is None: return True, 0
            l, r = dfs(node.left), dfs(node.right)
            if not l[0] or not r[0] or abs(l[1] - r[1]) > 1: return False, 0
            return True, max(l[1], r[1]) + 1

        return dfs(root)[0]

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