from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree1(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def recur(preorder, inorder):
            if 0 == len(preorder):
                return None
            root = TreeNode(preorder[0])
            idxIn = inorder.index(preorder[0])
            root.left = recur(preorder[1:1 + idxIn], inorder[:idxIn])
            root.right = recur(preorder[1 + idxIn:], inorder[idxIn + 1:])
            return root
        if 0 == len(preorder):
            return None

        return recur(preorder, inorder)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 2024/2/20  DFS 传递下标
        d = {x: i for i, x in enumerate(inorder)}
        n = len(preorder)

        def dfs(pi, pj, ii, ij):
            if pi > pj:
                return None
            root = TreeNode(preorder[pi])
            idx = d[preorder[pi]]
            left = idx - ii
            right = ij - idx
            root.left = dfs(pi + 1, pi + left, ii, idx - 1)
            root.right = dfs(pi + left + 1, pj, idx + 1, ij)
            return root
        return dfs(0, n - 1, 0, n - 1)


so = Solution()
print(so.buildTree([3,9,20,15,7], [9,3,15,20,7]))