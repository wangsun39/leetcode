# 给你二叉树的根结点 root ，此外树的每个结点的值要么是 0 ，要么是 1 。
#
# 返回移除了所有不包含 1 的子树的原二叉树。
#
# 节点 node 的子树为 node 本身加上所有 node 的后代。
#
#  
#
# 示例 1：
#
#
# 输入：root = [1,null,0,0,1]
# 输出：[1,null,0,null,1]
# 解释：
# 只有红色节点满足条件“所有不包含 1 的子树”。 右图为返回的答案。
# 示例 2：
#
#
# 输入：root = [1,0,1,0,0,0,1]
# 输出：[1,null,1,null,1]
# 示例 3：
#
#
# 输入：root = [1,1,0,1,1,0,1,0]
# 输出：[1,1,0,1,1,null,1]
#  
#
# 提示：
#
# 树中节点的数目在范围 [1, 200] 内
# Node.val 为 0 或 1




from typing import List
from collections import Counter
from typing import Optional

# Definition for a binary tree node.
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1:-1]
        n = len(s)
        ans = []
        def count(s):
            res = []
            m = len(s)
            for i in range(m):
                s1, s2 = s[: i + 1], s[i + 1:]
                if len(s1) > 1 and s1[0] == '0':
                    continue
                if len(s2) > 0 and s2[-1] == '0':
                    continue
                if i < m - 1:
                    res.append(s1 + '.' + s2)
                else:
                    res.append(s1)
            return res
        for i in range(n - 1):
            t1, t2 = count(s[: i + 1]), count(s[i + 1:])
            for tt1 in t1:
                for tt2 in t2:
                    ans.append('(' + tt1 + ', ' + tt2 + ')')
        return ans



so = Solution()
print(so.ambiguousCoordinates("(123)"))
print(so.ambiguousCoordinates("(00011)"))


