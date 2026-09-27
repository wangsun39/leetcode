# 给你一个整数数组 colors 和一个二维整数数组 queries 。colors表示一个由红色和蓝色瓷砖组成的环，第 i 块瓷砖的颜色为 colors[i] ：
#
# colors[i] == 0 表示第 i 块瓷砖的颜色是 红色 。
# colors[i] == 1 表示第 i 块瓷砖的颜色是 蓝色 。
# 环中连续若干块瓷砖的颜色如果是 交替 颜色（也就是说这组瓷砖中除了第一块和最后一块瓷砖以外，中间瓷砖的颜色与它 左边 和 右边 的颜色都不同），那么它被称为一个 交替组。
#
# 你需要处理两种类型的查询：
#
# queries[i] = [1, sizei]，确定大小为sizei的 交替组 的数量。
# queries[i] = [2, indexi, colori]，将colors[indexi]更改为colori。
# 返回数组 answer，数组中按顺序包含第一种类型查询的结果。
#
# 注意 ，由于 colors 表示一个 环 ，第一块 瓷砖和 最后一块 瓷砖是相邻的。
#
#
#
# 示例 1：
#
# 输入：colors = [0,1,1,0,1], queries = [[2,1,0],[1,4]]
#
# 输出：[2]
#
# 解释：
#
# 第一次查询：
#
# 将 colors[1] 改为 0。
#
#
#
# 第二次查询：
#
# 统计大小为 4 的交替组的数量：
#
#
#
# 示例 2：
#
# 输入：colors = [0,0,1,0,1,1], queries = [[1,3],[2,3,0],[1,5]]
#
# 输出：[2,0]
#
# 解释：
#
#
#
# 第一次查询：
#
# 统计大小为 3 的交替组的数量。
#
#
#
# 第二次查询：colors不变。
#
# 第三次查询：不存在大小为 5 的交替组。
#
#
#
# 提示：
#
# 4 <= colors.length <= 5 * 104
# 0 <= colors[i] <= 1
# 1 <= queries.length <= 5 * 104
# queries[i][0] == 1 或 queries[i][0] == 2
# 对于所有的i：
# queries[i][0] == 1： queries[i].length == 2, 3 <= queries[i][1] <= colors.length - 1
# queries[i][0] == 2： queries[i].length == 3, 0 <= queries[i][1] <= colors.length - 1, 0 <= queries[i][2] <= 1

from leetcode.allcode.competition.mypackage import *

class Fenwick1:
    def __init__(self, n: int):
        self.tree = [[0] * 2 for _ in range(n + 1)]  #  树状数组维护两个值，[a, b]  某个值x出现的次数a，某个值x出现的总和b
        self.n = n

    def add(self, i: int) -> None:  # + 1
        x = i
        while i < self.n + 1:
            self.tree[i][0] += 1
            self.tree[i][1] += x
            i += i & -i

    def sub(self, i: int) -> None:  # - 1
        x = i
        while i < self.n + 1:
            self.tree[i][0] -= 1
            self.tree[i][1] -= x
            i += i & -i

    # [1,i] 中的元素和
    def pre(self, i: int) -> List[int]:
        res = [0] * 2
        while i > 0:
            res[0] += self.tree[i][0]
            res[1] += self.tree[i][1]
            i &= i - 1
        return res

    # >= x 中的元素和
    def query(self, x: int) -> List[int]:
        a, b =  self.pre(self.n), self.pre(x - 1)
        return [a[0] - b[0], a[1] - b[1]]


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        sl = SortedList()  # 记录每个交替组的右边界
        n = len(colors)
        fw = Fenwick1(n)
        for i, x in enumerate(colors[1:], 1):
            if x == colors[i - 1]:
                sl.add(i)
        for i, x in enumerate(sl[1:], 1):
            d = sl[i] - sl[i - 1]
            fw.add(d)
        if colors[0] == colors[-1]:
            sl.add(0)
        if sl:
            fw.add(sl[0] + n - sl[-1])  # 首尾相连
        # else:
        #     fw.add(n)

        def update(idx, add_flg):
            p = sl.bisect_left(idx)
            pre = sl[p - 1]
            nxt = sl[(p + 1) % len(sl)]

            if add_flg:
                if pre == nxt:
                    fw.sub(n)
                else:
                    fw.sub((nxt - pre) % n)
                # 以上 if else 可以写成
                # fw.sub((nxt - pre - 1) % n + 1)
                fw.add(idx - pre)
                fw.add((nxt - idx) % n)
            else:
                fw.sub(idx - pre)
                fw.sub((nxt - idx) % n)
                if pre == nxt:
                    fw.add(n)
                else:
                    fw.add((nxt - pre) % n)


        def remove(idx):
            # 删除位置在idx的分界点，对应更新 fw 和 sl
            sl.remove(idx)
            if len(sl):
                update(idx, 0)
            else:
                fw.sub(n)

        def add(idx):
            # 增加位置在idx的分界点，对应更新 fw 和 sl
            if len(sl):
                update(idx, 1)
            else:
                fw.add(n)
            sl.add(idx)


        ans = []
        for i in range(len(queries)):
            if queries[i][0] == 1:
                sz = queries[i][1]
                if len(sl) == 0:
                    ans.append(n)
                else:
                    a, b = fw.query(sz)
                    ans.append(b - a * (sz - 1))
            else:
                j, x = queries[i][1:]
                if colors[j] == x: continue
                if colors[j] == colors[(j + 1) % n]:
                    remove((j + 1) % n)
                if colors[(j - 1) % n] == colors[j]:
                    remove(j)
                colors[j] = x
                if colors[j] == colors[(j + 1) % n]:
                    add((j + 1) % n)
                if colors[(j - 1) % n] == colors[j]:
                    add(j)
        return ans





so = Solution()
print(so.numberOfAlternatingGroups(colors = [0,0,0,1], queries = [[2,1,1],[1,3],[2,1,1],[2,0,1]]))
print(so.numberOfAlternatingGroups(colors = [0,0,1,0,1,1], queries = [[1,3],[2,3,0],[1,5]]))
print(so.numberOfAlternatingGroups(colors = [0,1,1,0,1], queries = [[2,1,0],[1,4]]))




