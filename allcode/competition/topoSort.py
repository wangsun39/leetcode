
from leetcode.allcode.competition.mypackage import *


# conditions 中的节点 id 从 0 到 n - 1
# conditions 中每对 [x,y] 表示先x后y，顺序不能颠倒

# O(n + m)
# 有时要考虑将原图翻转
def buildTopo(conditions, n):
    g = defaultdict(set)
    pre_num = [0] * n
    for x, y in conditions:  # x 先于 y , 原图需要反转时，可以写成 for y, x in conditions:
        if y not in g[x]:
            g[x].add(y)
            pre_num[y] += 1
    queue = deque([i for i in range(n) if pre_num[i] == 0]) # deque 在操作大数组时，性能比 list 好很多
    ans = []
    while len(queue):
        q = queue.popleft()
        ans.append(q)
        for x in g[q]:
            pre_num[x] -= 1
            if pre_num[x] == 0:
                queue.append(x)
    if len(ans) != n:
        return []  # 存在圈
    return ans

# 另一种拓扑序
# 统计每个节点拓扑序小的点的某种属性的极值  (851)
def loudAndRich(richer: List[List[int]], quiet: List[int]) -> List[int]:
    n = len(quiet)
    g = defaultdict(set)
    ans = [i for i in range(n)]  # 比自己richer的最安静值对应的id
    preNum = [0] * n
    for x, y in richer:
        if y not in g[x]:
            g[x].add(y)
            preNum[y] += 1
    queue = deque([i for i in range(n) if preNum[i] == 0]) # deque 在操作大数组时，性能比 list 好很多
    while len(queue):
        q = queue.popleft()
        for x in g[q]:
            preNum[x] -= 1
            if quiet[ans[q]] < quiet[ans[x]]:
                ans[x] = ans[q]
            if preNum[x] == 0:
                queue.append(x)
    return ans





