# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
#
# 请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
#
# 示例:
#
# 你可以将以下二叉树：
#
#     1
#    / \
#   2   3
#      / \
#     4   5
#
# 序列化为 "[1,2,3,null,null,4,5]"
# 提示:这与 LeetCode 目前使用的方式一致，详情请参阅LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。
#
# 说明:不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
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
                res += ',N'
                cur = cur.right
            elif len(stack) > 0:
                res += ',N'
                cur = stack.pop()
                cur = cur.right
            else:
                break
        return res[1:] if len(res) > 0 else ''

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if 0 == len(data):
            return None
        queue = data.split(',')
        root = TreeNode(int(queue[0]))
        cur, i = root, 1
        stack = [cur]
        while i < len(queue):
            if 'N' != queue[i]:
                cur.left = TreeNode(int(queue[i]))
                cur = cur.left
                stack.append(cur)
                i += 1
                continue
            while i < len(queue) and 'N' == queue[i]:
                cur = stack.pop()
                i += 1
            if i == len(queue):
                break
            cur.right = TreeNode(int(queue[i]))
            cur = cur.right
            stack.append(cur)
            i += 1
        return root





so = Codec()

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
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

node = so.deserialize('3,5,6,N,N,2,7,N,N,4,N,N,1,0,N,N,8,N')
