# 给你二叉树的根结点root，此外树的每个结点的值要么是 0 ，要么是 1 。
#
# 返回移除了所有不包含 1 的子树的原二叉树。
#
# 节点 node 的子树为 node 本身加上所有 node 的后代。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,null,0,0,1]
# 输出：[1,null,0,null,1]
# 解释：
# 只有红色节点满足条件“所有不包含 1 的子树”。 右图为返回的答案。
# 示例 2：
#
#
# 输入：root = [1,0,1,0,0,0,1]
# 输出：[1,null,1,null,1]
# 示例 3：
#
#
# 输入：root = [1,1,0,1,1,0,1,0]
# 输出：[1,1,0,1,1,null,1]
#
#
# 提示：
#
# 树中节点的数目在范围 [1, 200] 内
# Node.val 为 0 或 1




from typing import List
from collections import Counter
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node: TreeNode):
            if node is None:
                return [0, node]
            l = helper(node.left)
            node.left = l[1] if l[0] == 1 else None
            r = helper(node.right)
            node.right = r[1] if r[0] == 1 else None
            if node.val == 0 and node.left is None and node.right is None:
                return [0, None]
            return [1, node]
        ans = helper(root)
        return ans[1]



so = Solution()


