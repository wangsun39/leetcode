# 数组 arr 中 大于 前面和后面相邻元素的元素被称为 峰值 元素。
#
# 给你一个整数数组 nums 和一个二维整数数组 queries 。
#
# 你需要处理以下两种类型的操作：
#
# queries[i] = [1, li, ri] ，求出子数组 nums[li..ri] 中 峰值 元素的数目。
# queries[i] = [2, indexi, vali] ，将 nums[indexi] 变为 vali 。
# 请你返回一个数组 answer ，它依次包含每一个第一种操作的答案。
#
# 注意：
#
# 子数组中 第一个 和 最后一个 元素都 不是 峰值元素。
#
#
# 示例 1：
#
# 输入：nums = [3,1,4,2,5], queries = [[2,3,4],[1,0,4]]
#
# 输出：[0]
#
# 解释：
#
# 第一个操作：我们将 nums[3] 变为 4 ，nums 变为 [3,1,4,4,5] 。
#
# 第二个操作：[3,1,4,4,5] 中峰值元素的数目为 0 。
#
# 示例 2：
#
# 输入：nums = [4,1,4,2,1,5], queries = [[2,2,4],[1,0,2],[1,0,4]]
#
# 输出：[0,1]
#
# 解释：
#
# 第一个操作：nums[2] 变为 4 ，它已经是 4 了，所以保持不变。
#
# 第二个操作：[4,1,4] 中峰值元素的数目为 0 。
#
# 第三个操作：第二个 4 是 [4,1,4,2,1] 中的峰值元素。
#
#
#
# 提示：
#
# 3 <= nums.length <= 105
# 1 <= nums[i] <= 105
# 1 <= queries.length <= 105
# queries[i][0] == 1 或者 queries[i][0] == 2
# 对于所有的 i ，都有：
# queries[i][0] == 1 ：0 <= queries[i][1] <= queries[i][2] <= nums.length - 1
# queries[i][0] == 2 ：0 <= queries[i][1] <= nums.length - 1, 1 <= queries[i][2] <= 105

from leetcode.allcode.competition.mypackage import *

class NumArray:
    __slots__ = 'nums', 'tree'

    def __init__(self, nums: List[int]):
        n = len(nums)
        tree = [0] * (n + 1)
        for i, x in enumerate(nums, 1):  # i 从 1 开始
            tree[i] += x
            nxt = i + (i & -i)  # 下一个关键区间的右端点
            if nxt <= n:
                tree[nxt] += tree[i]
        self.nums = nums[:]
        self.tree = tree

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        i = index + 1
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & -i

    def prefixSum(self, i: int) -> int:
        s = 0
        while i:
            s += self.tree[i]
            i &= i - 1  # i -= i & -i 的另一种写法
        return s

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum(right + 1) - self.prefixSum(left)

class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        arr = [0] * n
        for i in range(1, n - 1):
            if nums[i - 1] < nums[i] > nums[i + 1]:
                arr[i] = 1
        na = NumArray(arr)
        ans = []
        def check(i):
            if 0 < i < n - 1 and arr[i] != int(nums[i - 1] < nums[i] > nums[i + 1]):
                return True  # 表示有变化
            return False

        for type, a, b in queries:
            if type == 1:
                v = na.sumRange(a, b)
                if arr[a]: v -= 1
                if arr[b]: v -= 1
                ans.append(max(v, 0))
            if type == 2:
                i, val = a, b
                nums[i] = val
                if check(i - 1):
                    na.update(i - 1, 1 - arr[i - 1])
                    arr[i - 1] = 1 - arr[i - 1]
                if check(i):
                    na.update(i, 1 - arr[i])
                    arr[i] = 1 - arr[i]
                if check(i + 1):
                    na.update(i + 1, 1 - arr[i + 1])
                    arr[i + 1] = 1 - arr[i + 1]
        return ans



so = Solution()
print(so.countOfPeaks([3,9,5,4], [[1,0,3],[2,1,4],[2,0,6],[1,2,3]]))
print(so.countOfPeaks([5,4,8,6], [[1,2,2],[1,1,2],[2,1,6]]))
print(so.countOfPeaks([3,1,4,2,5], [[2,3,4],[1,0,4]]))
print(so.countOfPeaks(nums = [4,1,4,2,1,5], queries = [[2,2,4],[1,0,2],[1,0,4]]))
print(so.countOfPeaks(nums = [3,1,4,2,5], queries = [[2,3,4],[1,0,4]]))




