from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal1(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(node: TreeNode):
            if node.left is not None:
                dfs(node.left)
            if node.right is not None:
                dfs(node.right)
            res.append(node.val)
        if root is not None:
            dfs(root)
        return res
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res = []
        stack = [[root, root.left is not None, root.right is not None]]  # 后面两个值分别表示此节点的左右子树是否遍历过
        while len(stack) > 0:
            e = stack.pop()
            if e[1]:
                stack.append([e[0], False, e[2]])
                stack.append([e[0].left, e[0].left.left is not None, e[0].left.right is not None])
            elif e[2]:
                stack.append([e[0], False, False])
                stack.append([e[0].right, e[0].right.left is not None, e[0].right.right is not None])
            else:
                res.append(e[0].val)
        return res

z = TreeNode(1)
z.left = TreeNode(2)
z.right = TreeNode(3)
so = Solution()
print(so.postorderTraversal(z))

