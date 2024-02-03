# 给你一棵二叉树的根 root ，请你将每个节点的值替换成该节点的所有 堂兄弟节点值的和 。
#
# 如果两个节点在树中有相同的深度且它们的父节点不同，那么它们互为 堂兄弟 。
#
# 请你返回修改值之后，树的根 root 。
#
# 注意，一个节点的深度指的是从树根节点到这个节点经过的边数。
#
#
#
# 示例 1：
#
#
#
# 输入：root = [5,4,9,1,10,null,7]
# 输出：[0,0,0,7,7,null,11]
# 解释：上图展示了初始的二叉树和修改每个节点的值之后的二叉树。
# - 值为 5 的节点没有堂兄弟，所以值修改为 0 。
# - 值为 4 的节点没有堂兄弟，所以值修改为 0 。
# - 值为 9 的节点没有堂兄弟，所以值修改为 0 。
# - 值为 1 的节点有一个堂兄弟，值为 7 ，所以值修改为 7 。
# - 值为 10 的节点有一个堂兄弟，值为 7 ，所以值修改为 7 。
# - 值为 7 的节点有两个堂兄弟，值分别为 1 和 10 ，所以值修改为 11 。
# 示例 2：
#
#
#
# 输入：root = [3,1,2]
# 输出：[0,0,0]
# 解释：上图展示了初始的二叉树和修改每个节点的值之后的二叉树。
# - 值为 3 的节点没有堂兄弟，所以值修改为 0 。
# - 值为 1 的节点没有堂兄弟，所以值修改为 0 。
# - 值为 2 的节点没有堂兄弟，所以值修改为 0 。
#
#
# 提示：
#
# 树中节点数目的范围是 [1, 105] 。
# 1 <= Node.val <= 104

from leetcode.allcode.competition.mypackage import *

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def copy(old):
            if old is None:
                return None
            new = TreeNode(old.val)
            new.left = copy(old.left)
            new.right = copy(old.right)
            return new
        ans = copy(root)
        lev = [0] * 100001
        def sumT(node):
            if node is None:
                return 0
            res = 0
            if node.left:
                res += node.left.val
            if node.right:
                res += node.right.val
            return res
        def dfs1(node, lv):  # 计算每层的和
            if node is None:
                return
            lev[lv] += node.val
            dfs1(node.left, lv + 1)
            dfs1(node.right, lv + 1)

        def dfs2(node, old, fa, lv):
            if node is None:
                return
            if fa is None:
                node.val = 0
            else:
                node.val = lev[lv] - sumT(fa)
            dfs2(node.left, old.left, old, lv + 1)
            dfs2(node.right, old.right, old, lv + 1)
        dfs1(root, 0)
        print(lev)
        dfs2(ans, root, None, 0)
        return ans


root = TreeNode(5)
root.left = TreeNode(5)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(10)
root.right.right = TreeNode(7)
so = Solution()
print(so.replaceValueInTree(root))




