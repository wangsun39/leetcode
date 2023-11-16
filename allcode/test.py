
from leetcode.allcode.competition.mypackage import *


infile = open('smf_tbl.h', 'r')
outfile = open('output.h', 'w', newline='\n')  # 防止windows下自动改变换行符

while True:
    line = infile.readline()
    if len(line) == 0:break
    if 'SMF_EC_ITEM(' in line:
        start, end = line.find('('), line.find(')')
        inner = line[start + 1: end].split(',')
        fail_enum = inner[0]
        inner[-1] = '"' + fail_enum.replace('_', ' ').lower() + '."'
        new_line = line[:start + 1] + ','.join(inner) + line[end:]
        outfile.write(new_line)
    else:
        outfile.write(line)
outfile.close()
infile.close()

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node: TreeNode):  # 返回以 node 为根的子树的节点上和硬币数
            nonlocal ans
            if node is None: return 0, 0
            l1, l2 = dfs(node.left)
            r1, r2 = dfs(node.right)
            ans += (abs(l1 - l2) + abs(r1 - r2))
            return l1 + r1 + 1, l2 + r2 + node.val

        dfs(root)
        return ans

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        vis = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    start = [i, j]
                    vis |= (1 << (i * c + j))
                elif grid[i][j] == 2:
                    end = [i, j]
                elif grid[i][j] == -1:
                    vis |= (1 << (i * c + j))

        @cache
        def dfs(i, j, vis):
            res = 0
            if i == end[0] and j == end[1]:
                return vis == (2 ** (r * c) - 1)
            for u, v in dir:
                x, y = i + u, j + v
                if 0 <= x < r and 0 <= y < c:
                    bit = x * c + y
                    if (1 << bit) & vis == 0:
                        res += dfs(x, y, vis | (1 << bit))
            return res
        return dfs(start[0], start[1], vis)




so = Solution()
print(so.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
print(so.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]]))
print(so.uniquePathsIII([[0,1],[2,0]]))


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        ans = []

        def dfs(node):
            if node is None:
                return
            cur = str(node.val) + ';'
            if node.left:
                cur += str(node.left.val)
            cur += ';'
            if node.right:
                cur += str(node.right.val)
            ans.append(cur)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        print(ans)
        return ','.join(ans)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if len(data) == 0: return None
        num = data.split(',')
        print(num)

        d = {}
        for x in num:
            print(x)
            pp = x.split(';')
            print(pp, len(pp), pp[0], pp[1])
            d[int(pp[0])] = [pp[1], pp[2]]
        n = len(num)
        if n == 0: return None
        print(123)

        p, _, _ = num[0].split(';')
        root = TreeNode(int(p))
        def dfs(node):
            v = node.val
            if len(d[v][0]):
                node.left = TreeNode(int(d[v][0]))
                dfs(node.left)
            if len(d[v][1]):
                node.right = TreeNode(int(d[v][1]))
                dfs(node.right)
            return
        dfs(root)
        return root


co = Codec()
co.deserialize('')
