# 给你一个整数数组 nums 和一个整数 k。
#
# 你可以对数组执行 至多 k 次交换操作。
#
# 在一次交换操作中，你可以选择任意两个下标 i 和 j 并交换 nums[i] 和 nums[j]。
#
# 返回一个整数，表示在执行交换后 可能的最大 子数组 和。
#
#
#
# 示例 1：
#
# 输入： nums = [1,-1,0,2], k = 1
#
# 输出： 3
#
# 解释：
#
# 我们可以交换下标 1 和 3，得到数组 [1, 2, 0, -1]。
# 子数组 [1, 2] 的和为 3，这是在至多 k = 1 次交换后可能的最大子数组和。
# 示例 2：
#
# 输入： nums = [4,3,2,4], k = 2
#
# 输出： 13
#
# 解释：
#
# 在至多 k = 2 次交换后，可能的最大子数组和是整个数组的和，即 13。
#
# 示例 3：
#
# 输入： nums = [-1,-2], k = 0
#
# 输出： -1
#
# 解释：
#
# 允许进行 k = 0 次交换。
# 可能的子数组为 [-1]、[-2] 和 [-1, -2]，其和分别为 -1、-2 和 -3。
# 在这些和中，最大值为 -1。
#
#
# 提示：
#
# 1 <= nums.length <= 1500
# -105 <= nums[i] <= 105
# 0 <= k <= nums.length

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Heap:
    __slots__ = ("_d", "_s", "_c", "_total", "_n")

    def __init__(self, items=None, max_heap=False):
        self._s = -1 if max_heap else 1
        self._c = defaultdict(int)
        if items is None:
            self._d = []
            self._total = 0
            self._n = 0
        else:
            items = list(items)
            self._d = [-x for x in items] if max_heap else items
            heapify(self._d)
            self._total = sum(items)
            self._n = len(items)

    @classmethod
    def heapify(cls, items, max_heap=False):
        items = list(items)
        h = cls.__new__(cls)
        h._s = -1 if max_heap else 1
        h._c = defaultdict(int)
        h._d = [-x for x in items] if max_heap else items
        heapify(h._d)
        h._total = sum(items)
        h._n = len(items)
        return h

    def heappush(self, x):
        heappush(self._d, x * self._s)
        self._total += x
        self._n += 1

    def predel(self, x):
        self._c[x * self._s] += 1
        self._total -= x
        self._n -= 1

    def _clean(self):
        while self._d and self._c[self._d[0]]:
            self._c[self._d[0]] -= 1
            if not self._c[self._d[0]]:
                del self._c[self._d[0]]
            heappop(self._d)          # 垃圾值，_total/_n 都已在 predel 减过

    def heappop(self):
        self._clean()
        if not self._d:
            raise IndexError("pop from empty heap")
        v = heappop(self._d) * self._s
        self._total -= v
        self._n -= 1
        return v

    def __getitem__(self, i):
        if i == 0:
            self._clean()
        return self._d[i] * self._s

    def __len__(self):
        return self._n

    def __bool__(self):
        return self._n > 0

    def sum(self):
        return self._total


class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = -inf
        for l in range(n):
            in_lo, in_hi = Heap(max_heap=True), Heap()  # in_hi 是窗口内保留的元素，in_lo 是窗口内要被替换出去的
            out_lo = Heap(nums, max_heap=True)  #  out_lo 是窗口外暂时没用的元素
            out_hi = Heap()  # out_hi 是可以被替换进去的

            # 约束: len(out_hi)==len(in_lo)<=k 这两个约束会对换
            #      out_hi[0] > -in_lo[0]

            for r in range(l, n):
                x = nums[r]  # 把 x 从 out 放入 in

                # 从 out 中删除 x
                out_hi._clean()
                if len(out_hi) and x >= out_hi[0]:
                    out_hi.predel(x)
                    y = in_lo.heappop()
                    in_hi.heappush(y)
                else:
                    out_lo.predel(x)

                # 把 x 放入 in 中
                in_lo._clean()
                if len(in_lo) and x <= in_lo[0]:
                    # 替换掉 in_lo 中的头，放入 x
                    y = in_lo.heappop()
                    in_hi.heappush(y)
                    in_lo.heappush(x)
                else:
                    in_hi.heappush(x)

                # 再尝试进行一次 in_lo 和 out_hi 之间的替换
                while len(in_lo) < k:
                    if len(in_hi) and len(out_lo) and in_hi[0] < out_lo[0]:
                        y = in_hi.heappop()
                        in_lo.heappush(y)
                        y = out_lo.heappop()
                        out_hi.heappush(y)
                    else:
                        break

                ans = MAX(ans, in_hi.sum() + out_hi.sum())

        return ans



so = Solution()
print(so.maxSum(nums = [4,3,2,4], k = 2))
print(so.maxSum(nums = [1,-1,0,2], k = 1))




