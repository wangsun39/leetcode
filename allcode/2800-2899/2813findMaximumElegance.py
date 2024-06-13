# 给你一个长度为 n 的二维整数数组 items 和一个整数 k 。
#
# items[i] = [profiti, categoryi]，其中 profiti 和 categoryi 分别表示第 i 个项目的利润和类别。
#
# 现定义 items 的 子序列 的 优雅度 可以用 total_profit + distinct_categories2 计算，其中 total_profit 是子序列中所有项目的利润总和，distinct_categories 是所选子序列所含的所有类别中不同类别的数量。
#
# 你的任务是从 items 所有长度为 k 的子序列中，找出 最大优雅度 。
#
# 用整数形式表示并返回 items 中所有长度恰好为 k 的子序列的最大优雅度。
#
# 注意：数组的子序列是经由原数组删除一些元素（可能不删除）而产生的新数组，且删除不改变其余元素相对顺序。
#
#
#
# 示例 1：
#
# 输入：items = [[3,2],[5,1],[10,1]], k = 2
# 输出：17
# 解释：
# 在这个例子中，我们需要选出长度为 2 的子序列。
# 其中一种方案是 items[0] = [3,2] 和 items[2] = [10,1] 。
# 子序列的总利润为 3 + 10 = 13 ，子序列包含 2 种不同类别 [2,1] 。
# 因此，优雅度为 13 + 22 = 17 ，可以证明 17 是可以获得的最大优雅度。
# 示例 2：
#
# 输入：items = [[3,1],[3,1],[2,2],[5,3]], k = 3
# 输出：19
# 解释：
# 在这个例子中，我们需要选出长度为 3 的子序列。
# 其中一种方案是 items[0] = [3,1] ，items[2] = [2,2] 和 items[3] = [5,3] 。
# 子序列的总利润为 3 + 2 + 5 = 10 ，子序列包含 3 种不同类别 [1, 2, 3] 。
# 因此，优雅度为 10 + 32 = 19 ，可以证明 19 是可以获得的最大优雅度。
# 示例 3：
#
# 输入：items = [[1,1],[2,1],[3,1]], k = 3
# 输出：7
# 解释：
# 在这个例子中，我们需要选出长度为 3 的子序列。
# 我们需要选中所有项目。
# 子序列的总利润为 1 + 2 + 3 = 6，子序列包含 1 种不同类别 [1] 。
# 因此，最大优雅度为 6 + 12 = 7 。
#
#
# 提示：
#
# 1 <= items.length == n <= 105
# items[i].length == 2
# items[i][0] == profiti
# items[i][1] == categoryi
# 1 <= profiti <= 109
# 1 <= categoryi <= n
# 1 <= k <= n

from leetcode.allcode.competition.mypackage import *


class Solution:
    def findMaximumElegance1(self, items: List[List[int]], k: int) -> int:
        n = len(items)
        items.sort()
        items1, items2 = items[n - k:], items[:n - k][::-1]  # items1 顺序， items2 逆序
        n2 = len(items2)
        counter = Counter(it[1] for it in items1)
        j = 0  # 对应 items2 的下标
        cur = ans = sum(it[0] for it in items1) + len(counter) ** 2
        # 尝试类别的所有可能 (>=len(counter))， 计算其中的最大值
        for i in range(k):
            p1, c1 = items1[i]
            if counter[c1] == 1:
                continue
            while j < len(items2) and counter[items2[j][1]] > 0:
                j += 1
            if j >= n2:
                break
            # 尝试调换 items1[i] 和 items2[j]
            cnt = len(counter)
            p2, c2 = items2[j]
            items1[i] = items2[j]
            counter[c1] -= 1
            counter[c2] = 1
            cur += (p2 + cnt * 2 + 1 - p1)  # 计算差值
            ans = max(ans, cur)

        return ans

    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(key=lambda x: x[0], reverse=True)
        counter = Counter()
        hp = []
        ans = 0
        for pro, cat in items[:k]:
            counter[cat] += 1
            ans += pro
        ans += len(counter) ** 2
        cur = ans
        for pro, cat in items[:k]:
            if counter[cat] > 1:
                heappush(hp, [0, pro, cat])   # 0表示同一种cat有多个，1表示同一种cat只有一个
            else:
                heappush(hp, [1, pro, cat])
        for pro, cat in items[k:]:
            if cat in counter:
                continue
            if hp[0][0] == 1:
                break
            delta = pro - hp[0][1] + (len(counter) + 1) ** 2 - len(counter) ** 2
            # if delta > 0:
            _, p1, c1 = heappop(hp)
            counter[c1] -= 1
            heappush(hp, [1, pro, cat])
            cur += delta
            ans = max(ans, cur)
            counter[cat] += 1
            while hp[0][0] == 0 and counter[hp[0][2]] == 1:
                heapreplace(hp, [1, hp[0][1], hp[0][2]])

        return ans


so = Solution()
print(so.findMaximumElegance(items = [[10,1],[10,1],[10,1],[10,1],[10,1],[10,1],[10,1],[10,1],[10,1],[10,1],[3,2],[3,3],[3,4],[3,5],[3,6],[3,7],[3,8],[3,9],[3,10],[3,11]], k = 10))   # 137
print(so.findMaximumElegance(items = [[2,2],[8,6],[10,6],[2,4],[9,5],[4,5]], k = 4))   # 39
print(so.findMaximumElegance(items = [[1,4],[4,3],[9,2],[2,4],[5,5],[7,5]], k = 4))   # 38
print(so.findMaximumElegance(items = [[3,2],[5,1],[10,1]], k = 2))   # 17
print(so.findMaximumElegance(items = [[10,1],[10,1],[10,1],[10,1],[10,1],[10,1],[10,1],[10,1],[10,1],[10,1],[3,2],[3,3],[3,4],[3,5],[3,6],[3,7],[3,8],[3,9],[3,10],[3,11]], k = 10))
print(so.findMaximumElegance(items = [[3,4],[8,4],[2,2],[1,3]], k = 2))
print(so.findMaximumElegance(items = [[5,1],[6,1],[8,1]], k = 2))
print(so.findMaximumElegance(items = [[3,1],[3,1],[2,2],[5,3]], k = 3))
print(so.findMaximumElegance(items = [[1,1],[2,1],[3,1]], k = 3))




