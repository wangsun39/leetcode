from typing import List, Optional
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree1(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def recur(inorder, postorder):
            if 0 == len(postorder):
                return None
            root = TreeNode(postorder[-1])
            idxIn = inorder.index(postorder[-1])
            root.left = recur(inorder[:idxIn], postorder[:idxIn])
            root.right = recur(inorder[idxIn + 1:], postorder[idxIn:-1])
            return root
        if 0 == len(inorder):
            return None

        return recur(inorder, postorder)

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # 2024/2/21  DFS 传递下标
        d = {x: i for i, x in enumerate(inorder)}
        n = len(postorder)

        def dfs(ii, ij, pi, pj):
            if pi > pj:
                return None
            root = TreeNode(postorder[pj])
            idx = d[postorder[pj]]
            left = idx - ii
            right = ij - idx
            root.left = dfs(ii, idx - 1, pi, pi + left - 1)
            root.right = dfs(idx + 1, ij, pi + left, pj - 1)
            return root
        return dfs(0, n - 1, 0, n - 1)


so = Solution()
print(so.buildTree([9,3,15,20,7], [9,15,7,20,3]))