

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
        return n


root = TreeNode(5)
root.left = TreeNode(1)
root.left.left = TreeNode(3)
root.right = TreeNode(2)
root.right.left = TreeNode(6)
root.right.right = TreeNode(4)

so = Solution()
print(so.getDirections(root, 3, 6))




