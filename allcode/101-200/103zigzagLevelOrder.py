class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        que_cur = []
        self.levList = [[]] #最终的list
        if root is None:
            return []
        que_cur.append(root)
        que_next = [] #下一层的队列
        loop = 0
        while 0 != len(que_cur) or 0 != len(que_next):
            if 0 == len(que_cur):
                que_cur, que_next = que_next, []
                t = que_cur.pop()
                self.levList.append([t.val])
                loop += 1
            else:
                t = que_cur.pop()
                self.levList[-1].append(t.val)
            if loop % 2 == 0:
                if t.left is not None:
                    que_next.append((t.left))
                if t.right is not None:
                    que_next.append((t.right))
            else:
                if t.right is not None:
                    que_next.append((t.right))
                if t.left is not None:
                    que_next.append((t.left))
        return self.levList




root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
so = Solution()
print(so.levelOrder(root))