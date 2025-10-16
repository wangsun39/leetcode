# 给你一棵 完美 二叉树的根节点 root ，请你反转这棵树中每个 奇数 层的节点值。
#
# 例如，假设第 3 层的节点值是 [2,1,3,4,7,11,29,18] ，那么反转后它应该变成 [18,29,11,7,4,3,1,2] 。
# 反转后，返回树的根节点。
#
# 完美 二叉树需满足：二叉树的所有父节点都有两个子节点，且所有叶子节点都在同一层。
#
# 节点的 层数 等于该节点到根节点之间的边数。
#
#
#
# 示例 1：
#
#
# 输入：root = [2,3,5,8,13,21,34]
# 输出：[2,5,3,8,13,21,34]
# 解释：
# 这棵树只有一个奇数层。
# 在第 1 层的节点分别是 3、5 ，反转后为 5、3 。
# 示例 2：
#
#
# 输入：root = [7,13,11]
# 输出：[7,11,13]
# 解释：
# 在第 1 层的节点分别是 13、11 ，反转后为 11、13 。
# 示例 3：
#
# 输入：root = [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]
# 输出：[0,2,1,0,0,0,0,2,2,2,2,1,1,1,1]
# 解释：奇数层由非零值组成。
# 在第 1 层的节点分别是 1、2 ，反转后为 2、1 。
# 在第 3 层的节点分别是 1、1、1、1、2、2、2、2 ，反转后为 2、2、2、2、1、1、1、1 。
#
#
# 提示：
#
# 树中的节点数目在范围 [1, 214] 内
# 0 <= Node.val <= 105
# root 是一棵 完美 二叉树


from leetcode.allcode.competition.mypackage import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def reverseOddLevels1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        lev = 0
        # cur = root
        queue = [root]
        def proc(q):
            n = len(q)
            for i in range(n // 2):
                q[i].val, q[n - i - 1].val = q[n - i - 1].val, q[i].val
            return
            # return q

        while True:
            if lev % 2 == 0:
                pass
            else:
                # queue = proc(queue)
                proc(queue)
            if queue[0].left is None:
                break
            que = []
            for node in queue:
                que.append(node.left)
                que.append(node.right)
            lev += 1
            queue = que

        return root

    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 2023/12/15 DFS写法
        def dfs(r1, r2, isOdd):
            if r1 is None: return
            if isOdd:
                r1.val, r2.val = r2.val, r1.val
            dfs(r1.left, r2.right, not isOdd)
            dfs(r1.right, r2.left, not isOdd)
        dfs(root.left, root.right, True)
        return root

root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(4)
so = Solution()
print(so.reverseOddLevels(root))




