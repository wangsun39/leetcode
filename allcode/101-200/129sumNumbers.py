class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = 0
        def dfs(node: TreeNode, curSum: int):
            nonlocal res
            if node is None:
                return
            newSum = curSum * 10 + node.val
            if node.left is None and node.right is None:
                res += newSum
                return
            dfs(node.left, newSum)
            dfs(node.right, newSum)
            return

        dfs(root, 0)
        return res


z = TreeNode(1)
z.left = TreeNode(2)
z.right = TreeNode(3)
so = Solution()
print(so.sumNumbers(z))

z = TreeNode(1)
z.left = TreeNode(-2)
z.right = TreeNode(-3)
z.left.left = TreeNode(1)
z.left.right = TreeNode(3)
z.right.left = TreeNode(-2)
z.left.left.left = TreeNode(-2)
so = Solution()
print(so.sumNumbers(z))


