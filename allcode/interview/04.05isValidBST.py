# 实现一个函数，检查一棵二叉树是否为二叉搜索树。
#
# 示例 1：
# 输入：
#     2
#    / \
#   1   3
# 输出：true
# 示例 2：
# 输入：
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出：false
# 解释：输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。


from leetcode.allcode.competition.mypackage import *

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        def dfs(node):
            r1 = r2 = node.val
            if node.left:
                r, mn, mx = dfs(node.left)
                if not r or mx >= node.val:
                    return False, -1, -1
                r1 = mn
            if node.right:
                r, mn, mx = dfs(node.right)
                if not r or mn <= node.val:
                    return False, -1, -1
                r2 = mx
            return True, r1, r2
        return dfs(root)[0]



root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

so = Solution()
print(so.inorderSuccessor(root, root.left).val)




