from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        if None is root:
            return res
        stack = [root, '#']
        cur = []
        while ['#'] != stack:
            node = stack.pop(0)
            if '#' == node:
                res.insert(0, cur)
                stack.append('#')
                cur = []
                continue
            elif node is None:
                continue
            cur.append(node.val)
            stack.append(node.left)
            stack.append(node.right)

        return res


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

so = Solution()
print(so.levelOrderBottom(root))