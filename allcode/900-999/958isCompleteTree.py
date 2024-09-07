# 给你一棵二叉树的根节点 root ，请你判断这棵树是否是一棵 完全二叉树 。
#
# 在一棵 完全二叉树 中，除了最后一层外，所有层都被完全填满，并且最后一层中的所有节点都尽可能靠左。最后一层（第 h 层）中可以包含 1 到 2h 个节点。
#
#
#
# 示例 1：
#
#
#
# 输入：root = [1,2,3,4,5,6]
# 输出：true
# 解释：最后一层前的每一层都是满的（即，节点值为 {1} 和 {2,3} 的两层），且最后一层中的所有节点（{4,5,6}）尽可能靠左。
# 示例 2：
#
#
#
# 输入：root = [1,2,3,4,5,null,7]
# 输出：false
# 解释：值为 7 的节点不满足条件「节点尽可能靠左」。
#
#
# 提示：
#
# 树中节点数目在范围 [1, 100] 内
# 1 <= Node.val <= 1000

from leetcode.allcode.competition.mypackage import *

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if node is None:
                return True, 0, 0  # bool, depth, num
            b1, d1, n1 = dfs(node.left)
            b2, d2, n2 = dfs(node.right)
            if not b1 or not b2:
                return False, 0, 0
            if d1 < d2 or d1 > d2 + 1: return False, 0, 0
            if d1 == d2:
                if 2 ** d1 - 1 != n1 and n2 > 0:
                    return False, 0, 0
                return True, d1 + 1, n1 + n2 + 1
            else:
                if 2 ** d2 - 1 != n2:
                    return False, 0, 0
                return True, d1 + 1, n1 + n2 + 1

        return dfs(root)[0]



so = Solution()
print(so.isCompleteTree())




