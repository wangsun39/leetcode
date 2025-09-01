# 给定一棵二叉树，设计一个算法，创建含有某一深度上所有节点的链表（比如，若一棵树的深度为 D，则会创建出 D 个链表）。返回一个包含所有深度的链表的数组。
#
#
#
# 示例：
#
# 输入：[1,2,3,4,5,null,7,8]
#
#         1
#        /  \
#       2    3
#      / \    \
#     4   5    7
#    /
#   8
#
# 输出：[[1],[2,3],[4,5,7],[8]]


from leetcode.allcode.competition.mypackage import *

class Solution:
    def listOfDepth(self, tree: Optional[TreeNode]) -> List[Optional[ListNode]]:
        ans = []
        lev = []
        def dfs(node, dep):
            if node is None:
                return 0
            if len(ans) < dep:
                ans.append([ListNode(node.val)])
                lev.append(ans[-1])
            else:
                lev[dep].next = ListNode(node.val)
                lev[dep] = lev[dep].next
            dfs(node.left, dep + 1)
            dfs(node.right, dep + 1)
        dfs(tree, 0)
        return ans



so = Solution()




