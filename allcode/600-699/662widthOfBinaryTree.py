# 给定一个二叉树，编写一个函数来获取这个树的最大宽度。树的宽度是所有层中的最大宽度。这个二叉树与满二叉树（full binary tree）结构相同，但一些节点为空。
#
# 每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的null节点也计入长度）之间的长度。
#
# 示例 1:
#
# 输入:
#
#            1
#          /   \
#         3     2
#        / \     \
#       5   3     9
#
# 输出: 4
# 解释: 最大值出现在树的第 3 层，宽度为 4 (5,3,null,9)。
# 示例 2:
#
# 输入:
#
#           1
#          /
#         3
#        / \
#       5   3
#
# 输出: 2
# 解释: 最大值出现在树的第 3 层，宽度为 2 (5,3)。
# 示例3:
#
# 输入:
#
#           1
#          / \
#         3   2
#        /
#       5
#
# 输出: 2
# 解释: 最大值出现在树的第 2 层，宽度为 2 (3,2)。
# 示例 4:
#
# 输入:
#
#           1
#          / \
#         3   2
#        /     \
#       5       9
#      /         \
#     6           7
# 输出: 8
# 解释: 最大值出现在树的第 4 层，宽度为 8 (6,null,null,null,null,null,null,7)。
# 注意: 答案在32位有符号整数的表示范围内。


from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        queue1 = [[root, 0]]
        maxWidth = 0
        while len(queue1) > 0:
            queue2 = []
            curWidth = queue1[-1][1] - queue1[0][1] + 1
            maxWidth = max(maxWidth, curWidth)
            while len(queue1) > 0:
                e = queue1.pop(0)
                if e[0].left:
                    queue2.append([e[0].left, e[1] * 2])
                if e[0].right:
                    queue2.append([e[0].right, e[1] * 2 + 1])
            queue1 = queue2
        return maxWidth





so = Solution()


