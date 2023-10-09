# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.allPaths = []
    def binaryTreePaths(self, root):
        def recursiveFind(pre, node):
            pre = pre + str(node.val)
            if node.left is None and node.right is None:
                self.allPaths.append(pre)
                return
            pre += '->'
            if node.left is not None:
                recursiveFind(pre, node.left)
            if node.right is not None:
                recursiveFind(pre, node.right)
        if root is None:
            return []
        recursiveFind('', root)
        return self.allPaths

class Solution1:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def construct_paths(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:  # 当前节点是叶子节点
                    paths.append(path)  # 把路径加入到答案中
                else:
                    path += '->'  # 当前节点不是叶子节点，继续递归遍历
                    construct_paths(root.left, path)
                    construct_paths(root.right, path)

        paths = []
        construct_paths(root, '')
        return paths



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

so = Solution()
print(so.binaryTreePaths(root))


