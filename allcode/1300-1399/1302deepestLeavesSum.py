# 给你一棵二叉树的根节点 root ，请你返回 层数最深的叶子节点的和 。
#
#
#
# 示例 1：
#
#
#
# 输入：root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# 输出：15
# 示例 2：
#
# 输入：root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# 输出：19
#
#
# 提示：
#
# 树中节点数目在范围 [1, 104]之间。
# 1 <= Node.val <= 100



from typing import List,Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        maxDepth = 1
        ans = 0
        def dfs(node, depth):
            nonlocal ans, maxDepth
            if depth > maxDepth:
                ans = node.val
                maxDepth = depth
            elif depth == maxDepth:
                ans += node.val
            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)
        dfs(root, 1)
        return ans



#
# so = Solution()
# root1 = TreeNode(2)
# root1.left = TreeNode(1)
# root1.right = TreeNode(4)
# root2 = TreeNode(1)
# root2.left = TreeNode(0)
# root2.right = TreeNode(3)
# print(so.getAllElements(root1, root2))




