class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node):
            if node is None:
                return True, None, None
            res, left_left, left_right = dfs(node.left)
            if not res:
                return False, None, None
            res, right_left, right_right = dfs(node.right)
            if not res:
                return False, None, None
            if (left_right is None or left_right < node.val) and (right_left is None or node.val < right_left):
                return True, node.val if left_left is None else left_left, node.val if right_right is None else right_right
            else:
                return False, None, None
        return dfs(root)[0]


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(6)
root.right.right = TreeNode(20)


so = Solution()

print(so.isValidBST(root))
