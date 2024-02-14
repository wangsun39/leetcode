# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
#
#
#
# 示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]
# 示例 2：
#
# 输入：root = [1]
# 输出：[[1]]
# 示例 3：
#
# 输入：root = []
# 输出：[]
#
#
# 提示：
#
# 树中节点数目在范围 [0, 2000] 内
# -1000 <= Node.val <= 1000

from collections import deque
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode):
        que = []
        self.levList = [[]]
        if root is None:
            return []
        que.append(root)
        que.append('separation')
        self.makeLevList(que)
        return self.levList
    def makeLevList(self, que):
        while 1 != len(que):
            if 'separation' == que[0]:
                del(que[0])
                self.levList.append([])
                que.append('separation')
                continue
            self.levList[-1].append(que[0].val)
            if que[0].left is not None:
                que.append(que[0].left)
            if que[0].right is not None:
                que.append(que[0].right)
            del(que[0])

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 2024/2/14 BFS重写
        dq1 = deque([root])
        ans = []
        while dq1:
            dq2 = deque()
            lv = []
            while dq1:
                x = dq1.popleft()
                if x:
                    lv.append(x.val)
                    dq2.append(x.left)
                    dq2.append(x.right)
            dq1 = dq2
            if lv:
                ans.append(lv)
        return ans


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
so = Solution()
print(so.levelOrder(root))