# 给你一个整数数组 instructions ，你需要根据 instructions 中的元素创建一个有序数组。一开始你有一个空的数组 nums ，你需要 从左到右 遍历 instructions 中的元素，将它们依次插入 nums 数组中。每一次插入操作的 代价 是以下两者的 较小值 ：
#
# nums 中 严格小于  instructions[i] 的数字数目。
# nums 中 严格大于  instructions[i] 的数字数目。
# 比方说，如果要将 3 插入到 nums = [1,2,3,5] ，那么插入操作的 代价 为 min(2, 1) (元素 1 和  2 小于 3 ，元素 5 大于 3 ），插入后 nums 变成 [1,2,3,3,5] 。
#
# 请你返回将 instructions 中所有元素依次插入 nums 后的 总最小代价 。由于答案会很大，请将它对 109 + 7 取余 后返回。
#
#
#
# 示例 1：
#
# 输入：instructions = [1,5,6,2]
# 输出：1
# 解释：一开始 nums = [] 。
# 插入 1 ，代价为 min(0, 0) = 0 ，现在 nums = [1] 。
# 插入 5 ，代价为 min(1, 0) = 0 ，现在 nums = [1,5] 。
# 插入 6 ，代价为 min(2, 0) = 0 ，现在 nums = [1,5,6] 。
# 插入 2 ，代价为 min(1, 2) = 1 ，现在 nums = [1,2,5,6] 。
# 总代价为 0 + 0 + 0 + 1 = 1 。
# 示例 2:
#
# 输入：instructions = [1,2,3,6,5,4]
# 输出：3
# 解释：一开始 nums = [] 。
# 插入 1 ，代价为 min(0, 0) = 0 ，现在 nums = [1] 。
# 插入 2 ，代价为 min(1, 0) = 0 ，现在 nums = [1,2] 。
# 插入 3 ，代价为 min(2, 0) = 0 ，现在 nums = [1,2,3] 。
# 插入 6 ，代价为 min(3, 0) = 0 ，现在 nums = [1,2,3,6] 。
# 插入 5 ，代价为 min(3, 1) = 1 ，现在 nums = [1,2,3,5,6] 。
# 插入 4 ，代价为 min(3, 2) = 2 ，现在 nums = [1,2,3,4,5,6] 。
# 总代价为 0 + 0 + 0 + 0 + 1 + 2 = 3 。
# 示例 3：
#
# 输入：instructions = [1,3,3,3,2,4,2,1,2]
# 输出：4
# 解释：一开始 nums = [] 。
# 插入 1 ，代价为 min(0, 0) = 0 ，现在 nums = [1] 。
# 插入 3 ，代价为 min(1, 0) = 0 ，现在 nums = [1,3] 。
# 插入 3 ，代价为 min(1, 0) = 0 ，现在 nums = [1,3,3] 。
# 插入 3 ，代价为 min(1, 0) = 0 ，现在 nums = [1,3,3,3] 。
# 插入 2 ，代价为 min(1, 3) = 1 ，现在 nums = [1,2,3,3,3] 。
# 插入 4 ，代价为 min(5, 0) = 0 ，现在 nums = [1,2,3,3,3,4] 。
# ​​​​​插入 2 ，代价为 min(1, 4) = 1 ，现在 nums = [1,2,2,3,3,3,4] 。
# 插入 1 ，代价为 min(0, 6) = 0 ，现在 nums = [1,1,2,2,3,3,3,4] 。
# 插入 2 ，代价为 min(2, 4) = 2 ，现在 nums = [1,1,2,2,2,3,3,3,4] 。
# 总代价为 0 + 0 + 0 + 0 + 1 + 0 + 1 + 0 + 2 = 4 。
#
#
# 提示：
#
# 1 <= instructions.length <= 105
# 1 <= instructions[i] <= 105

from leetcode.allcode.competition.mypackage import *

class Fenwick:
    # 所有函数参数下标从1开始
    __slots__ = ['f', 'nums']

    def __init__(self, n: int):
        self.f = [0] * (n + 1)
        self.nums = [0] * (n + 1)

    def add(self, i: int, val: int) -> None:  # nums[i] += val
        self.nums[i] += val
        while i < len(self.f):
            self.f[i] += val
            i += i & -i

    def update(self, i: int, val: int) -> None:  # nums[i] += val
        delta = val - self.nums[i]
        self.add(i, delta)

    def pre(self, i: int) -> int:  # 下标<=i的和
        res = 0
        while i > 0:
            res += self.f[i]
            i &= i - 1
        return res

    def query_one(self, idx: int):
        return self.nums[idx]

    def query(self, l: int, r: int) -> int:  # [l, r]  区间求和
        if r < l:
            return 0
        return self.pre(r) - self.pre(l - 1)

class Solution:
    def createSortedArray1(self, instructions: List[int]) -> int:
        sl = SortedList()
        ans = 0
        for x in instructions:
            m = len(sl)
            p1 = sl.bisect_left(x)
            p2 = sl.bisect_right(x)
            ans += min(p1, m - p2)
            sl.add(x)
        return ans % (10 ** 9 + 7)

    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10 ** 9 + 7
        mx = max(instructions) + 1
        fw = Fenwick(mx)
        ans = 0
        for x in instructions:
            less = fw.query(1, x - 1)
            more = fw.query(x + 1, mx)
            ans += min(less, more)
            ans %= MOD
            fw.add(x, 1)
        return ans


so = Solution()
print(so.createSortedArray(instructions = [1,5,6,2]))
print(so.createSortedArray(instructions = [1,2,3,6,5,4]))
print(so.createSortedArray(instructions = [1,3,3,3,2,4,2,1,2]))


