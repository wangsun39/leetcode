class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        if p.val == q.val:
            return p
        if p.val > q.val:
            p, q = q, p
        while True:
            if p.val <= cur.val and q.val >= cur.val:
                return cur
            if p.val > cur.val:
                cur = cur.right
            else:
                cur = cur.left




