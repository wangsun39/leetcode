# 在一个 m*n 的二维字符串数组中输出二叉树，并遵守以下规则：
#
# 行数 m 应当等于给定二叉树的高度。
# 列数 n 应当总是奇数。
# 根节点的值（以字符串格式给出）应当放在可放置的第一行正中间。根节点所在的行与列会将剩余空间划分为两部分（左下部分和右下部分）。你应该将左子树输出在左下部分，右子树输出在右下部分。左下和右下部分应当有相同的大小。即使一个子树为空而另一个非空，你不需要为空的子树输出任何东西，但仍需要为另一个子树留出足够的空间。然而，如果两个子树都为空则不需要为它们留出任何空间。
# 每个未使用的空间应包含一个空的字符串""。
# 使用相同的规则输出子树。
# 示例 1:
#
# 输入:
#      1
#     /
#    2
# 输出:
# [["", "1", ""],
#  ["2", "", ""]]
# 示例 2:
#
# 输入:
#      1
#     / \
#    2   3
#     \
#      4
# 输出:
# [["", "", "", "1", "", "", ""],
#  ["", "2", "", "", "", "3", ""],
#  ["", "", "4", "", "", "", ""]]
# 示例 3:
#
# 输入:
#       1
#      / \
#     2   5
#    /
#   3
#  /
# 4
# 输出:
# [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
#  ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
#  ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
#  ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
# 注意: 二叉树的高度在范围 [1, 10] 中。
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def getHeight(node):
            if node is None:
                return 0
            return max(getHeight(node.left), getHeight(node.right)) + 1
        height = getHeight(root)
        tree = [[''] * (2 ** height - 1) for _ in range(height)]
        def fillTree(node, row, column):
            if node is None:
                return
            tree[row - 1][column - 1] = str(node.val)
            fillTree(node.left, row + 1, column - 2 ** (height - 1 - row))
            fillTree(node.right, row + 1, column + 2 ** (height - 1 - row))
        fillTree(root, 1, 2 ** (height - 1))
        return tree



so = Solution()
# print(so.printTree(root))

