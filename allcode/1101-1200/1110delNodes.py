# 给出二叉树的根节点 root，树上每个节点都有一个不同的值。
#
# 如果节点值在 to_delete 中出现，我们就把该节点从树上删去，最后得到一个森林（一些不相交的树构成的集合）。
#
# 返回森林中的每棵树。你可以按任意顺序组织答案。
#
#
#
# 示例 1：
#
#
#
# 输入：root = [1,2,3,4,5,6,7], to_delete = [3,5]
# 输出：[[1,2,null,4],[6],[7]]
# 示例 2：
#
# 输入：root = [1,2,4,null,3], to_delete = [3]
# 输出：[[1,2,4]]
#
#
# 提示：
#
# 树中的节点数最大为 1000。
# 每个节点都有一个介于 1 到 1000 之间的值，且各不相同。
# to_delete.length <= 1000
# to_delete 包含一些从 1 到 1000、各不相同的值。


from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        to_delete = set(to_delete)
        def dfs(node, fa_del):   # fa_del 表示 node de fu节点是否删除
            if node is None: return 0
            del_self = False
            if node.val in to_delete:
                del_self = True
            l = dfs(node.left, del_self)
            r = dfs(node.right, del_self)
            if l == 1:
                node.left = None
            if r == 1:
                node.right = None

            if fa_del and not del_self:
                ans.append(node)

            return del_self
        dfs(root, True)
        return ans




obj = Solution()


