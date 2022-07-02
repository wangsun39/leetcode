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



root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
so = Solution()
print(so.levelOrder(root))