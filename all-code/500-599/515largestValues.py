class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestValues(self, root: TreeNode):
        def transTree2List(root):
            que = []
            que.append(root)
            que.append('|')
            nodes = []
            while len(que) > 1:
                t = que.pop(0)
                if '|' == t:
                    nodes.append('|')
                    que.append('|')
                else:
                    nodes.append(t.val)
                    if t.left is not None:
                        que.append(t.left)
                    if t.right is not None:
                        que.append(t.right)
            return nodes

        if root is None:
            return []
        nodes = transTree2List(root)
        print(nodes)
        res = []
        cur = nodes[0]
        for i, node in enumerate(nodes):
            if '|' == node:
                res.append(cur)
                cur = nodes[i+1]
            else:
                cur = max(cur, node)
        res.append(cur)
        print(res)
        return res


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)

so = Solution()
print(so.largestValues(root))

