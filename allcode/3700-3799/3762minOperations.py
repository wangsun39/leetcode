# 给你一个整数数组 nums 和一个整数 k。
#
# 在一次操作中，你可以恰好将 nums 中的某个元素 增加或减少 k 。
#
# 还给定一个二维整数数组 queries，其中每个 queries[i] = [li, ri]。
#
# 对于每个查询，找到将 子数组 nums[li..ri] 中的 所有 元素变为相等所需的 最小 操作次数。如果无法实现，返回 -1。
#
# 返回一个数组 ans，其中 ans[i] 是第 i 个查询的答案。
#
# 子数组 是数组中一个连续、非空 的元素序列。
#
#
#
# 示例 1：
#
# 输入： nums = [1,4,7], k = 3, queries = [[0,1],[0,2]]
#
# 输出： [1,2]
#
# 解释：
#
# 一种最优操作方式：
#
# i	[li, ri]	nums[li..ri]	可行性	操作	最终
# nums[li..ri]	ans[i]
# 0	[0, 1]	[1, 4]	是	nums[0] + k = 1 + 3 = 4 = nums[1]	[4, 4]	1
# 1	[0, 2]	[1, 4, 7]	是	nums[0] + k = 1 + 3 = 4 = nums[1]
# nums[2] - k = 7 - 3 = 4 = nums[1]	[4, 4, 4]	2
# 因此，ans = [1, 2]。
#
# 示例 2：
#
# 输入： nums = [1,2,4], k = 2, queries = [[0,2],[0,0],[1,2]]
#
# 输出： [-1,0,1]
#
# 解释：
#
# 一种最优操作方式：
#
# i	[li, ri]	nums[li..ri]	可行性	操作	最终
# nums[li..ri]	ans[i]
# 0	[0, 2]	[1, 2, 4]	否	-	[1, 2, 4]	-1
# 1	[0, 0]	[1]	是	已相等	[1]	0
# 2	[1, 2]	[2, 4]	是	nums[1] + k = 2 + 2 = 4 = nums[2]	[4, 4]	1
# 因此，ans = [-1, 0, 1]。
#
#
#
# 提示：
#
# 1 <= n == nums.length <= 4 × 104
# 1 <= nums[i] <= 109
# 1 <= k <= 109
# 1 <= queries.length <= 4 × 104
# queries[i] = [li, ri]
# 0 <= li <= ri <= n - 1

from leetcode.allcode.competition.mypackage import *

class Node:
    __slots__ = 'l', 'r', 'lo', 'ro', 'cnt', 'sum'

    def __init__(self, l: int, r: int, lo=None, ro=None, cnt=0, sum=0):
        self.l = l
        self.r = r
        self.lo = lo
        self.ro = ro
        self.cnt = cnt  # 维护区间内数字个数
        self.sum = sum  # 维护区间内数字之和

    def maintain(self):
        self.cnt = self.lo.cnt + self.ro.cnt
        self.sum = self.lo.sum + self.ro.sum

    @staticmethod
    def build(l: int, r: int) -> 'Node':
        o = Node(l, r)
        if l == r:
            return o
        mid = (l + r) // 2
        o.lo = Node.build(l, mid)
        o.ro = Node.build(mid + 1, r)
        return o

    # 在线段树的位置 i 添加 val
    def add(self, i: int, val: int) -> 'Node':
        # 复制一份当前节点
        o = Node(self.l, self.r, self.lo, self.ro, self.cnt, self.sum)
        if o.l == o.r:
            o.cnt += 1
            o.sum += val
            return o
        mid = (o.l + o.r) // 2
        if i <= mid:
            o.lo = o.lo.add(i, val)
        else:
            o.ro = o.ro.add(i, val)
        o.maintain()
        return o

    # 查询 old 和 self 对应子数组的第 k 小，k 从 1 开始
    def kth(self, old: 'Node', k: int) -> int:
        if self.l == self.r:
            return self.l
        cnt_l = self.lo.cnt - old.lo.cnt
        if k <= cnt_l:  # 答案在左子树中
            return self.lo.kth(old.lo, k)
        return self.ro.kth(old.ro, k - cnt_l)  # 答案在右子树中

    # 查询 old 和 self 对应子数组，有多少个数的下标 <= i，这些数的元素和是多少
    def query(self, old: 'Node', i: int) -> Tuple[int, int]:
        if self.r <= i:
            return self.cnt - old.cnt, self.sum - old.sum
        cnt, sum_ = self.lo.query(old.lo, i)
        mid = (self.l + self.r) // 2
        if i > mid:
            c, s = self.ro.query(old.ro, i)
            cnt += c
            sum_ += s
        return cnt, sum_


class Solution:
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        left = list(range(n))  # 一段连续的模k同余的左端点
        for i in range(1, n):
            if nums[i] % k == nums[i - 1] % k:
                left[i] = left[i - 1]

        sorted_nums = sorted(list(set(nums)))
        mp = {x: i for i, x in enumerate(sorted_nums)}

        # 构建可持久化线段树
        t = [None] * (n + 1)  # 构造 n 个线段树，它们之间是有关联的
        t[0] = Node.build(0, len(sorted_nums) - 1)
        for i, x in enumerate(nums):
            j = mp[x]  # 离散化
            t[i + 1] = t[i].add(j, x)

        ans = []
        for l, r in queries:
            if left[r] > l:
                ans.append(-1)
                continue

            m = r - l + 1
            # t[l] 与 t[r + 1] 两个线段树的差值，在这个差值中线段树中找第 (m + 1)//2 大的位置，即中位数的位置
            idx = t[r + 1].kth(t[l], (m + 1) // 2)
            x = sorted_nums[idx]  # 对应到原数组中的值

            c1, s1 = t[r + 1].query(t[l], idx)  # 区间中，中位数以下的元素个数，元素和
            total = t[r + 1].sum - t[l].sum  # 区间中元素和
            s2 = total - s1
            c2 = m - c1
            v = s2 - x * c2 + x * c1 - s1
            ans.append(v // k)

        # for l, r in queries:
        #     if left[r] > l:  # 无解
        #         ans.append(-1)
        #         continue
        #
        #     r += 1  # 改成左闭右开，方便计算
        #
        #     # 计算区间中位数
        #     sz = r - l
        #     i = t[r].kth(t[l], sz // 2 + 1)
        #     median = sorted_nums[i]  # 离散化后的值 -> 原始值
        #
        #     # 计算区间所有元素到中位数的距离和
        #     total = t[r].sum - t[l].sum  # 区间元素和
        #     cnt_left, sum_left = t[r].query(t[l], i)
        #     s = median * cnt_left - sum_left  # 蓝色面积
        #     s += total - sum_left - median * (sz - cnt_left)  # 绿色面积
        #     ans.append(s // k)  # 操作次数 = 距离和 / k


        return ans




so = Solution()
print(so.minOperations(nums = [1,4,7], k = 3, queries = [[0,1],[0,2]]))




