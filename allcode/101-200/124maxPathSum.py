class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = root.val
        def dfs(node: TreeNode):
            nonlocal res
            if node is None:
                return 0
            leftSum, rightSum = dfs(node.left), dfs(node.right)
            maxWithNode = max(node.val, node.val + leftSum, node.val + rightSum) # 函数返回值，表示在以此节点为根的子树中，以此节点为起点的最大路径
            res = max(res, maxWithNode, node.val + leftSum + rightSum)
            return maxWithNode

        dfs(root)
        return res



z = TreeNode(1)
z.left = TreeNode(-2)
z.right = TreeNode(-3)
z.left.left = TreeNode(1)
z.left.right = TreeNode(3)
z.right.left = TreeNode(-2)
z.left.left.left = TreeNode(-2)
so = Solution()
print(so.maxPathSum(z))

z = TreeNode(1)
z.left = TreeNode(2)
z.right = TreeNode(3)
z.left.left = TreeNode(4)
z.left.right = TreeNode(5)
z.right.left = TreeNode(6)
z.right.right = TreeNode(7)
so = Solution()
print(so.maxPathSum(z))

