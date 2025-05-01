# 有 n 个项目，每个项目或者不属于任何小组，或者属于 m 个小组之一。group[i] 表示第 i 个项目所属的小组，如果第 i 个项目不属于任何小组，则 group[i] 等于 -1。项目和小组都是从零开始编号的。可能存在小组不负责任何项目，即没有任何项目属于这个小组。
#
# 请你帮忙按要求安排这些项目的进度，并返回排序后的项目列表：
#
# 同一小组的项目，排序后在列表中彼此相邻。
# 项目之间存在一定的依赖关系，我们用一个列表 beforeItems 来表示，其中 beforeItems[i] 表示在进行第 i 个项目前（位于第 i 个项目左侧）应该完成的所有项目。
# 如果存在多个解决方案，只需要返回其中任意一个即可。如果没有合适的解决方案，就请返回一个 空列表 。
#
#
#
# 示例 1：
#
#
#
# 输入：n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
# 输出：[6,3,4,1,5,2,0,7]
# 示例 2：
#
# 输入：n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
# 输出：[]
# 解释：与示例 1 大致相同，但是在排序后的列表中，4 必须放在 6 的前面。
#
#
# 提示：
#
# 1 <= m <= n <= 3 * 104
# group.length == beforeItems.length == n
# -1 <= group[i] <= m - 1
# 0 <= beforeItems[i].length <= n - 1
# 0 <= beforeItems[i][j] <= n - 1
# i != beforeItems[i][j]
# beforeItems[i] 不含重复元素

from leetcode.allcode.competition.mypackage import *

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # 先将group数组离散化，所有组的编号都在[0,m-1]中，且连续
        number = sorted(list(set(x for x in group if x != -1)))
        mp = {x: i for i, x in enumerate(number) if x != -1}
        group = [mp[x] if x != -1 else -1 for x in group]
        m = max(group) + 1
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
        g_before = set()  # 组间关系
        g_to_t = defaultdict(list)
        for i in range(n):
            g_to_t[group[i]].append(i)
        inner = defaultdict(list)  # 每个组的组内关系
        for i, before in enumerate(beforeItems):
            for j in before:
                if group[i] == group[j]:
                    inner[group[i]].append([i, j])
                else:
                    g_before.add((group[i], group[j]))

        def buildTopo(conditions, idx):
            g = defaultdict(set)
            pre_num = defaultdict(int)
            for y, x in conditions:  # x 先于 y
                if y not in g[x]:
                    g[x].add(y)
                    pre_num[y] += 1
            queue = deque([i for i in idx if pre_num[i] == 0])  # deque 在操作大数组时，性能比 list 好很多
            ans = []
            while len(queue):
                q = queue.popleft()
                ans.append(q)
                for x in g[q]:
                    pre_num[x] -= 1
                    if pre_num[x] == 0:
                        queue.append(x)
            if len(ans) != len(idx):
                return []  # 存在圈
            return ans

        g_seq = buildTopo(g_before, list(range(m)))
        if len(g_seq) == 0: return []
        ans = []
        for gno in g_seq:
            res = buildTopo(inner[gno], g_to_t[gno])
            if len(res) == 0: return []
            ans += res
        return ans



so = Solution()
print(so.sortItems(n = 5, m = 3, group = [0,0,2,1,0], beforeItems = [[3],[],[],[],[1,3,2]]))
print(so.sortItems(n = 5, m = 5, group = [2,0,-1,3,0], beforeItems = [[2,1,3],[2,4],[],[],[]]))
print(so.sortItems(n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]))


