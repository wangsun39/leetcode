class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode):
        return self.maxDiffCycle(root, root.val, root.val)
    def maxDiffCycle(self, node, min_value, max_value):
        diff = max_value - min_value
        if node is None:
            return diff
        left_max, right_max = diff, diff
        if node.left is not None:
            # min_value = min(min_value, node.left.val)
            # max_value = max(max_value, node.left.val)
            left_max = self.maxDiffCycle(node.left, min(min_value, node.left.val), max(max_value, node.left.val))
        if node.right is not None:
            # min_value = min(min_value, node.right.val)
            # max_value = max(max_value, node.right.val)
            right_max = self.maxDiffCycle(node.right, min(min_value, node.right.val), max(max_value, node.right.val))
        return max(left_max, right_max)


root = TreeNode(8)
root.left = TreeNode(3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right = TreeNode(10)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)

obj = Solution()
print(obj.maxAncestorDiff(root))

