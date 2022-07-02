# 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
#
# 一般来说，删除节点可分为两个步骤：
#
# 首先找到需要删除的节点；
# 如果找到了，删除它。
# 说明： 要求算法时间复杂度为 O(h)，h 为树的高度。
#
# 示例:
#
# root = [5,3,6,2,4,null,7]
# key = 3
#
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# 给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
#
# 一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
#
#     5
#    / \
#   4   6
#  /     \
# 2       7
#
# 另一个正确答案是 [5,2,6,null,4,null,7]。
#
#     5
#    / \
#   2   6
#    \   \
#     4   7


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        cur, pre = root, None
        while True:  # 查找目标节点
            if cur is None:
                return root
            if cur.val == key:
                break
            elif cur.val > key:
                cur, pre, isLeft = cur.left, cur, True
            else:
                cur, pre, isLeft = cur.right, cur, False

        if cur.left is None:  # 将目标节点看作root的处理，得到一个新的root
            res = cur.right
        elif cur.right is None:
            res = cur.left
        else:
            res = cur.left
            next = cur.left
            while next.right is not None:
                next = next.right
            next.right = cur.right

        if pre is None:  # 目标节点是root
            return res

        if isLeft:
            pre.left = res
        else:
            pre.right = res

        return root




so = Solution()

root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(6)
root.right.right = TreeNode(7)
print(so.deleteNode(root, 5))


