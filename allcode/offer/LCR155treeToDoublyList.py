# 将一个 二叉搜索树 就地转化为一个 已排序的双向循环链表 。
#
# 对于双向循环列表，你可以将左右孩子指针作为双向循环链表的前驱和后继指针，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。
#
# 特别地，我们希望可以 就地 完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中最小元素的指针。
#
#
#
# 示例 1：
#
# 输入：root = [4,2,5,1,3]
#
#
# 输出：[1,2,3,4,5]
#
# 解释：下图显示了转化后的二叉搜索树，实线表示后继关系，虚线表示前驱关系。
#
# 示例 2：
#
# 输入：root = [2,1,3]
# 输出：[1,2,3]
# 示例 3：
#
# 输入：root = []
# 输出：[]
# 解释：输入是空树，所以输出也是空链表。
# 示例 4：
#
# 输入：root = [1]
# 输出：[1]
#
#
# 提示：
#
# -1000 <= Node.val <= 1000
# Node.left.val < Node.val < Node.right.val
# Node.val 的所有值都是独一无二的
# 0 <= Number of Nodes <= 2000
# 注意：本题与主站 426 题相同： https://leetcode-cn.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

from leetcode.allcode.competition.mypackage import *

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None: return root
        pre, first = None, None

        def proc(node):
            nonlocal pre, first
            if pre is None:
                first = node
            else:
                pre.right = node
                node.left = pre
            pre = node

        def dfs(node):
            if node is None: return
            dfs(node.left)
            proc(node)
            dfs(node.right)

        dfs(root)
        first.left = pre
        pre.right = first
        return first

root = Node(2)
root.left = Node(1)
root.right = Node(3)
so = Solution()
x = so.treeToDoublyList(root)
print(x)




