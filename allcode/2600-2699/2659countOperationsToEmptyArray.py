# 给你一个包含若干 互不相同 整数的数组 nums ，你需要执行以下操作 直到数组为空 ：
#
# 如果数组中第一个元素是当前数组中的 最小值 ，则删除它。
# 否则，将第一个元素移动到数组的 末尾 。
# 请你返回需要多少个操作使 nums 为空。
#
#
#
# 示例 1：
#
# 输入：nums = [3,4,-1]
# 输出：5
# Operation	Array
# 1	[4, -1, 3]
# 2	[-1, 3, 4]
# 3	[3, 4]
# 4	[4]
# 5	[]
#
#
# 示例 2：
#
# 输入：nums = [1,2,4,3]
# 输出：5
# Operation	Array
# 1	[2, 4, 3]
# 2	[4, 3]
# 3	[3, 4]
# 4	[4]
# 5	[]
#
#
# 示例 3：
#
# 输入：nums = [1,2,3]
# 输出：3
# Operation	Array
# 1	[2, 3]
# 2	[3]
# 3	[]
#
#
# 提示：
#
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums 中的元素 互不相同 。

from leetcode.allcode.competition.mypackage import *

class Fenwick:
    # 所有函数参数下标从1开始，可以传入使用者的数值x+1的值
    __slots__ = ['f', 'nums']

    def __init__(self, n: int):
        # n 是能调用下面函数的下标最大值
        self.f = [0] * (n + 1)  # 关键区间
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
    def countOperationsToEmptyArray1(self, nums: List[int]) -> int:
        n = len(nums)
        sl = SortedList()
        left = [0] * n  # 左侧比nums[i]大的数字个数
        right = [0] * n  # 右侧比nums[i]大的数字个数
        for i, x in enumerate(nums):
            p = sl.bisect_left(x)
            left[i] = len(sl) - p
            sl.add(x)
        sl = SortedList()
        for i in range(n - 1, -1, -1):
            x = nums[i]
            p = sl.bisect_left(x)
            right[i] = len(sl) - p
            sl.add(x)
        li = list([x, i] for i, x in enumerate(nums))
        li.sort()
        pre = [0] * n  # 前一个比nums[i]小的数字的下标
        for i in range(n - 1):
            pre[li[i + 1][1]] = li[i][1]
        ans = 0
        for i, x in sorted(enumerate(nums), key=lambda v: [v[1], v[0]]):
            if pre[i] > i:
                # 前一个删除的数在这个数之后，这个数，需要操作 i之前比它大的数+pre[i]之后比i大的数之和
                ans += left[i] + right[pre[i]] + 1
            else:
                # 前一个删除的数在这个数之前，这个数，需要操作在这两个数之间比它们的大的数的个数
                ans += left[i] - left[pre[i]] + 1
        return ans

    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        # 2025/1/18 树状树状解法
        i_nums = sorted(enumerate(nums), key=lambda x:x[1])
        j = 1
        for i, _ in i_nums:
            nums[i] = j
            j += 1
        mx = max(nums)
        fw = Fenwick(mx)
        for i in range(1, mx + 1):
            fw.update(i, 1)
        cur = 1
        ans = 0
        for i, _ in i_nums:
            if cur <= i + 1:
                ans += fw.query(cur, i + 1)
            else:
                ans += fw.pre(i + 1) + fw.query(cur, mx)
            fw.update(i + 1, 0)
            cur = i + 1
        return ans





so = Solution()
print(so.countOperationsToEmptyArray(nums = [-4,-13,-12]))
print(so.countOperationsToEmptyArray(nums = [3,4,-1]))
print(so.countOperationsToEmptyArray(nums = [1,2,4,3]))




