class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def kthSmallest(self, root, k):
        self.num = 0
        self.k = k
        self.calcNodeNum(root)
        return self.k_node.val
    def calcNodeNum(self, root):
        if self.num >= self.k:
            return
        if root.left is not None:
            self.calcNodeNum(root.left)
        if self.num == self.k:
            return
        self.num += 1
        if self.num == self.k:
            self.k_node = root
            return
        if root.right is not None:
            self.calcNodeNum(root.right)


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)

so = Solution()
print(so.kthSmallest(root, 3))


class Solution1:
    def kthSmallest(self, root, k):
        def gen(r):
            if r is not None:
                for x in gen(r.left):
                    yield x
                yield r
                for x in gen(r.right):
                    yield x
        it = gen(root)
        for _ in range(k):
            ans = next(it)
        return ans.val
