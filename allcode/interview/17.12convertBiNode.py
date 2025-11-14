# 二叉树数据结构TreeNode可用来表示单向链表（其中left置空，right为下一个链表节点）。实现一个方法，把二叉搜索树转换为单向链表，要求依然符合二叉搜索树的性质，转换操作应是原址的，也就是在原始的二叉搜索树上直接修改。
#
# 返回转换后的单向链表的头节点。
#
# 注意：本题相对原题稍作改动
#
#
#
# 示例：
#
# 输入： [4,2,5,1,3,null,6,0]
# 输出： [0,null,1,null,2,null,3,null,4,null,5,null,6]
# 提示：
#
# 节点数量不会超过 100000。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def convertBiNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: return None

        def dfs(node: TreeNode):
            head = node
            tail = node
            if node.left:
                head, t1 = dfs(node.left)
                t1.right = node
                node.left = None
            if node.right:
                h, tail = dfs(node.right)
                node.right = h
            return head, tail

        head, _ = dfs(root)
        return head

root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(5)

so = Solution()
print(so.convertBiNode(root))




