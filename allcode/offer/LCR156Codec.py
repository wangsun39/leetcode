# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
#
# 请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
#
# 提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,2,3,null,null,4,5]
# 输出：[1,2,3,null,null,4,5]
# 示例 2：
#
# 输入：root = []
# 输出：[]
# 示例 3：
#
# 输入：root = [1]
# 输出：[1]
# 示例 4：
#
# 输入：root = [1,2]
# 输出：[1,2]
#
#
# 提示：
#
# 树中结点数在范围 [0, 104] 内
# -1000 <= Node.val <= 1000
# 注意：本题与主站 297 题相同： https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/

from leetcode.allcode.competition.mypackage import *

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




