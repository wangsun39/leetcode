from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack =[]
        res = []
        cur = root
        while True:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            else:
                if 0 == len(stack):
                    break
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return res


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(6)
root.right.right = TreeNode(20)


so = Solution()

print(so.inorderTraversal(root))
