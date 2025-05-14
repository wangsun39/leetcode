# 给定两棵二叉树 tree1 和 tree2，判断 tree2 是否以 tree1 的某个节点为根的子树具有 相同的结构和节点值 。
# 注意，空树 不会是以 tree1 的某个节点为根的子树具有 相同的结构和节点值 。
#
#
#
# 示例 1：
#
#
#
#
#
#
#
# 输入：tree1 = [1,7,5], tree2 = [6,1]
# 输出：false
# 解释：tree2 与 tree1 的一个子树没有相同的结构和节点值。
# 示例 2：
#
#
#
# 输入：tree1 = [3,6,7,1,8], tree2 = [6,1]
# 输出：true
# 解释：tree2 与 tree1 的一个子树拥有相同的结构和节点值。即 6 - > 1。
#
#
# 提示：
#
# 0 <= 节点个数 <= 10000

from leetcode.allcode.competition.mypackage import *

class Solution:
    def isSubStructure(self, A: Optional[TreeNode], B: Optional[TreeNode]) -> bool:

        def check(n1, n2):
            if n1 is None: return n2 is None
            if n2 is None: return True
            if n1.val != n2.val: return False
            return check(n1.left, n2.left) and check(n1.right, n2.right)

        def check2(nd):
            if check(nd, B):
                return True
            return nd and (check2(nd.left) or check2(nd.right))

        if B is None: return False
        return check2(A)


so = Solution()




