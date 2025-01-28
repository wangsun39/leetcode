# 给你二叉搜索树的根节点 root ，同时给定最小边界low 和最大边界 high。通过修剪二叉搜索树，使得所有节点的值在[low, high]中。修剪树不应该改变保留在树中的元素的相对结构（即，如果没有被移除，原有的父代子代关系都应当保留）。 可以证明，存在唯一的答案。
#
# 所以结果应当返回修剪好的二叉搜索树的新的根节点。注意，根节点可能会根据给定的边界发生改变。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,0,2], low = 1, high = 2
# 输出：[1,null,2]
# 示例 2：
#
#
# 输入：root = [3,0,4,null,2,null,null,1], low = 1, high = 3
# 输出：[3,2,null,1]
# 示例 3：
#
# 输入：root = [1], low = 1, high = 2
# 输出：[1]
# 示例 4：
#
# 输入：root = [1,null,2], low = 1, high = 3
# 输出：[1,null,2]
# 示例 5：
#
# 输入：root = [1,null,2], low = 2, high = 4
# 输出：[2]
#
#
# 提示：
#
# 树中节点数在范围 [1, 104] 内
# 0 <= Node.val <= 104
# 树中每个节点的值都是唯一的
# 题目数据保证输入是一棵有效的二叉搜索树
# 0 <= low <= high <= 104




from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def findLargerThanLowNode(root):
            cur = root
            while cur.val < low:
                cur = cur.right
                if cur is None:
                    return None
            return cur
        def findLessThanHighNode(root):
            cur = root
            while cur.val > high:
                cur = cur.left
                if cur is None:
                    return None
            return cur
        newRoot = root
        while newRoot.val < low or newRoot.val > high:  # 找到一个根节点，使得此节点的val介于low和high之间
            if newRoot.val < low:
                newRoot = findLargerThanLowNode(newRoot)
                if newRoot is None:
                    return None
            if newRoot.val > high:
                newRoot = findLessThanHighNode(newRoot)
                if newRoot is None:
                    return None
        pre, cur = newRoot, newRoot.left
        while cur:
            if cur.val >= low:
                pre, cur = cur, cur.left
            else:
                pre.left = cur.right
                cur = cur.right
        pre, cur = newRoot, newRoot.right
        while cur:
            if cur.val <= high:
                pre, cur = cur, cur.right
            else:
                pre.right = cur.left
                cur = cur.left
        return newRoot


root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(2)


so = Solution()
# so.trimBST(root, 1, 2)

root = TreeNode(45)
root.left = TreeNode(30)
root.left.left = TreeNode(10)
root.left.right = TreeNode(36)
root.right = TreeNode(46)

so.trimBST(root, 32, 44)

