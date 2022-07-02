# 序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。
#
# 设计一个算法来序列化和反序列化二叉搜索树。 对序列化/反序列化算法的工作方式没有限制。 您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树。
#
# 编码的字符串应尽可能紧凑。
#
# 注意：不要使用类成员/全局/静态变量来存储状态。 你的序列化和反序列化算法应该是无状态的。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        stack = []
        cur = root
        res = ''
        while True:
            if cur is not None:
                res += (',' + str(cur.val))
                if cur.left is not None:
                    stack.append(cur)
                    cur = cur.left
                    continue
                cur = cur.right
            elif len(stack) > 0:
                cur = stack.pop()
                cur = cur.right
            else:
                break
        return res[1:] if len(res) > 0 else ''

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if 0 == len(data):
            return None
        queue = data.split(',')
        root = TreeNode(int(queue[0]))
        cur, i = root, 1
        stack = [cur]
        while i < len(queue):
            if cur.val > int(queue[i]):  # 'N' != queue[i]:
                cur.left = TreeNode(int(queue[i]))
                cur = cur.left
                stack.append(cur)
                i += 1
                continue
            while i < len(queue) and len(stack) > 0 and stack[-1].val < int(queue[i]):
                cur = stack.pop()
            if i == len(queue):
                break
            cur.right = TreeNode(int(queue[i]))
            cur = cur.right
            stack.append(cur)
            i += 1
        return root



so = Codec()

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(so.serialize(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(7)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)
print(so.serialize(root))

node = so.deserialize('2,1,3')


class Codec1:
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        """

        def postorder(root):
            return [root.val] + postorder(root.left) + postorder(root.right) if root else []
        print('this:', ' '.join(map(str, postorder(root))))
        return ' '.join(map(str, postorder(root)))

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        """

        def helper(lower=float('-inf'), upper=float('inf')):
            if not data or data[0] < lower or data[0] > upper:
                return None

            val = data.pop(0)
            root = TreeNode(val)
            root.left = helper(lower, val)
            root.right = helper(val, upper)
            return root

        data = [int(x) for x in data.split(' ') if x]
        return helper()

so = Codec1()
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(so.serialize(root))
node = so.deserialize(so.serialize(root))
