

from leetcode.allcode.competition.mypackage import *

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        s_nodes = set()
        d_nodes = defaultdict(Node)
        if node is None:
            return None

        def dfs(x: Node):  # 找出所有点，复制所有点
            d_nodes[x.val] = Node(x.val)
            s_nodes.add(x.val)
            for y in x.neighbors:
                if y.val not in s_nodes:
                    dfs(y)
                d_nodes[x.val].neighbors.append(d_nodes[y.val])

        dfs(node)
        return d_nodes[node.val]





so = Solution()
print(so.cloneGraph())




