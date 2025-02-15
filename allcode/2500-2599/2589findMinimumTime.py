# 你有一台电脑，它可以 同时 运行无数个任务。给你一个二维整数数组 tasks ，其中 tasks[i] = [starti, endi, durationi] 表示第 i 个任务需要在 闭区间 时间段 [starti, endi] 内运行 durationi 个整数时间点（但不需要连续）。
#
# 当电脑需要运行任务时，你可以打开电脑，如果空闲时，你可以将电脑关闭。
#
# 请你返回完成所有任务的情况下，电脑最少需要运行多少秒。
#
#
#
# 示例 1：
#
# 输入：tasks = [[2,3,1],[4,5,1],[1,5,2]]
# 输出：2
# 解释：
# - 第一个任务在闭区间 [2, 2] 运行。
# - 第二个任务在闭区间 [5, 5] 运行。
# - 第三个任务在闭区间 [2, 2] 和 [5, 5] 运行。
# 电脑总共运行 2 个整数时间点。
# 示例 2：
#
# 输入：tasks = [[1,3,2],[2,5,3],[5,6,2]]
# 输出：4
# 解释：
# - 第一个任务在闭区间 [2, 3] 运行
# - 第二个任务在闭区间 [2, 3] 和 [5, 5] 运行。
# - 第三个任务在闭区间 [5, 6] 运行。
# 电脑总共运行 4 个整数时间点。
#
#
# 提示：
#
# 1 <= tasks.length <= 2000
# tasks[i].length == 3
# 1 <= starti, endi <= 2000
# 1 <= durationi <= endi - starti + 1

from leetcode.allcode.competition.mypackage import *

class Solution1:
    def findMinimumTime1(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1])
        vis = set()
        # print(tasks)
        for l, r, d in tasks:
            cand = []
            for i in range(l, r + 1):
                if i not in vis:
                    cand.append(i)
            need = d - (r - l + 1 - len(cand))
            for i in range(need):
                vis.add(cand[-i - 1])
        # print(vis)
        return len(vis)


    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        # 2024/5/15 扫描线，这个性能不如上面的
        ans = []
        n = len(tasks)
        mn, mx = min(x for x, _, _ in tasks), max(x for _, x, _ in tasks)
        for i in range(mn, mx + 1):
            for t1, t2, d in tasks:
                if d == 0 or i < t1 or i > t2: continue
                if d <= t2 - i: continue
                ans.append(i)
                for j in range(n):
                    if tasks[j][0] <= i <= tasks[j][1]:
                        if tasks[j][2]:
                            tasks[j][2] -= 1
                break
        return len(ans)


# 2025/2/15 lazy 线段树
class STree1:
    # Lazy 线段树
    def __init__(self, nums: List[int]):
        self.nums = nums
        n = len(nums)
        self.cnt = [0] * (4 * n)  # 记录区间1的个数
        self.todo = [False] * (4 * n)  # 特殊区间的lazy标记

    # 维护区间 1 的个数
    def maintain(self, o: int) -> None:
        self.cnt[o] = self.cnt[o * 2] + self.cnt[o * 2 + 1]

    # 执行区间反转
    def do(self, o: int, l: int, r: int) -> None:
        self.cnt[o] = r - l + 1
        self.todo[o] = True

    # 初始化线段树   o,l,r=1,1,n
    def build(self, o: int, l: int, r: int) -> None:
        if l == r:
            self.cnt[l] = self.nums[l - 1]
            return
        m = (l + r) // 2
        self.build(o * 2, l, m)
        self.build(o * 2 + 1, m + 1, r)
        self.maintain(o)

    # 尽可能更新后面的没有置为的0，共要更新v个
    def update(self, o: int, l: int, r: int, L: int, R: int, v) -> int:
        if self.todo[o] or self.cnt[o] == r - l + 1:  # 有 lazy tag的区间说明已经全覆盖了
            return 0
        if l == r:
            self.cnt[o] = 1
            return 1
        m = (l + r) // 2
        tl = v  # 左边最多要更新的数量
        vl = vr = 0  # 左右侧更新了的数量
        if m < R:
            vr = self.update(o * 2 + 1, m + 1, r, L, R, v)  # 右侧更新了的数量
            if vr >= v:
                self.maintain(o)
                return v
            tl = v - vr
        vl = self.update(o * 2, l, m, L, R, tl)
        self.maintain(o)
        return vl + vr


    def spread(self, o: int, l: int, m: int, r: int) -> None:
        if self.todo[o]:
            self.todo[0] = False
            self.do(o * 2, l, m)
            self.do(o * 2 + 1, m + 1, r)

    def query(self, o: int, l: int, r: int, L: int, R: int) -> int:
        if L <= l and r <= R: return self.cnt[o]
        m = (l + r) // 2
        self.spread(o, l, m, r)
        if m >= R: return self.query(o * 2, l, m, L, R)
        if m < L: return self.query(o * 2 + 1, m + 1, r, L, R)
        return self.query(o * 2, l, m, L, R) + self.query(o * 2 + 1, m + 1, r, L, R)



class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        # 线段树法
        tasks.sort(key=lambda x: x[1])  # 按结束时间排序
        m = tasks[-1][1] + 1  # m 是最晚会议结束时间 + 1
        st = STree1([0] * m)  # 维护区间上元素个数
        st.update(1, 1, m, tasks[0][0], tasks[0][1], tasks[0][2])
        ans = tasks[0][2]
        for start, end, duration in tasks[1:]:
            v = st.query(1, 1, m, start, end)
            if v >= duration: continue
            st.update(1, 1, m, start, end, duration - v)
            ans += duration - v
        return ans



so = Solution()
print(so.findMinimumTime([[1,3,2],[2,5,3],[5,6,2]]))   # 4
print(so.findMinimumTime([[3,15,3],[6,19,5],[1,19,10]]))   # 10
print(so.findMinimumTime([[1,10,7],[4,11,1],[3,19,7],[10,15,2]]))   # 8
print(so.findMinimumTime([[6,15,4],[3,7,1],[4,20,4]]))   # 4
print(so.findMinimumTime([[2,3,1],[4,5,1],[1,5,2]]))   # 2




