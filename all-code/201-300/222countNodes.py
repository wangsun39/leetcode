class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        max_layer, node_num = 0, 0 # 层数和最下层的节点数,root是第一层
        def dfs(node, layer):
            nonlocal node_num, max_layer
            if layer > max_layer:
                max_layer = layer
                node_num = 1
            elif layer == max_layer:
                node_num += 1
            if node.left is not None:
                dfs(node.left, layer+1)
            if node.right is not None:
                dfs(node.right, layer+1)
        dfs(root, 1)
        return 2 ** (max_layer-1) - 1 + node_num

    def countNodes1(self, root: TreeNode) -> int:
        if root is None:
            return 0
        def getDepth():
            cur, depth = root, 0
            while cur is not None:
                cur = cur.left
                depth += 1
            return depth - 1
        treeDepth = getDepth()
        def ifExist(num):
            node, n = root, treeDepth - 1
            while n >= 0:
                if num & (1 << n):
                    node = node.right
                else:
                    node = node.left
                if node is None:
                    return False
                n -= 1
            return True

        left, right = 0, 2 ** (treeDepth + 1) - 1
        if ifExist(right):
            return 2 ** (treeDepth + 1) - 1
        while left < right - 1:
            mid = (left + right) // 2
            if ifExist(mid):
                left = mid
            else:
                right = mid

        return (2 ** treeDepth - 1) + left + 1



so = Solution()
root = TreeNode(1)
print(so.countNodes1(root))
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
print(so.countNodes1(root))

