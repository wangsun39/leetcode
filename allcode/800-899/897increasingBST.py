# 给你一棵二叉搜索树的 root ，请你 按中序遍历 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。
#
#
#
# 示例 1：
#
#
# 输入：root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# 输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
# 示例 2：
#
#
# 输入：root = [5,1,7]
# 输出：[1,null,5,null,7]
#
#
# 提示：
#
# 树中节点数的取值范围是 [1, 100]
# 0 <= Node.val <= 1000


from leetcode.allcode.competition.mypackage import *

class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = TreeNode(-1)
        cur = ans

        def dfs(node):
            nonlocal cur
            if node.left:
                dfs(node.left)
            cur.right = TreeNode(node.val)
            cur = cur.right
            if node.right:
                dfs(node.right)
        dfs(root)
        return ans.right


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)


so = Solution()
print(so.increasingBST(root))

