# 给你一棵 二叉树 的根节点 root ，这棵二叉树总共有 n 个节点。每个节点的值为 1 到 n 中的一个整数，且互不相同。给你一个整数 startValue ，表示起点节点 s 的值，和另一个不同的整数 destValue ，表示终点节点 t 的值。
#
# 请找到从节点 s 到节点 t 的 最短路径 ，并以字符串的形式返回每一步的方向。每一步用 大写 字母 'L' ，'R' 和 'U' 分别表示一种方向：
#
# 'L' 表示从一个节点前往它的 左孩子 节点。
# 'R' 表示从一个节点前往它的 右孩子 节点。
# 'U' 表示从一个节点前往它的 父 节点。
# 请你返回从 s 到 t 最短路径 每一步的方向。
#
#
#
# 示例 1：
#
#
#
# 输入：root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
# 输出："UURL"
# 解释：最短路径为：3 → 1 → 5 → 2 → 6 。
# 示例 2：
#
#
#
# 输入：root = [2,1], startValue = 2, destValue = 1
# 输出："L"
# 解释：最短路径为：2 → 1 。
#
#
# 提示：
#
# 树中节点数目为 n 。
# 2 <= n <= 105
# 1 <= Node.val <= n
# 树中所有节点的值 互不相同 。
# 1 <= startValue, destValue <= n
# startValue != destValue

from leetcode.allcode.competition.mypackage import *

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        g = defaultdict(list)
        dir = defaultdict(dict)
        def dfs(node):
            if node.left:
                g[node.val].append([node.left.val, 1])
                g[node.left.val].append([node.val, 1])
                dir[node.val][node.left.val] = 'L'
                dir[node.left.val][node.val] = 'U'
                dfs(node.left)
            if node.right:
                g[node.val].append([node.right.val, 1])
                g[node.right.val].append([node.val, 1])
                dir[node.val][node.right.val] = 'R'
                dir[node.right.val][node.val] = 'U'
                dfs(node.right)
        dfs(root)

        def dijkstra(g: List[List[Tuple[int]]], start: int) -> List[int]:
            dist = [inf] * (len(g) + 1)  # 注意这个地方可能要替换成 n
            dist[start] = 0
            pre = [0] * (len(g) + 1)
            h = [(0, start)]
            while h:
                d, x = heappop(h)
                if d > dist[x]:
                    continue
                for y, wt in g[x]:
                    new_d = dist[x] + wt
                    if new_d < dist[y]:
                        dist[y] = new_d
                        pre[y] = x
                        heappush(h, (new_d, y))
            return pre

        pr = dijkstra(g, startValue)
        ans = []
        cur = destValue
        while cur != startValue:
            ans.insert(0, dir[pr[cur]][cur])
            cur = pr[cur]
        return ''.join(ans)


root = TreeNode(5)
root.left = TreeNode(1)
root.left.left = TreeNode(3)
root.right = TreeNode(2)
root.right.left = TreeNode(6)
root.right.right = TreeNode(4)

so = Solution()
print(so.getDirections(root, 3, 6))




