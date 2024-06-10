# 给你一个下标从 1 开始、长度为 n 的整数数组 nums 。
#
# 现定义函数 greaterCount ，使得 greaterCount(arr, val) 返回数组 arr 中 严格大于 val 的元素数量。
#
# 你需要使用 n 次操作，将 nums 的所有元素分配到两个数组 arr1 和 arr2 中。在第一次操作中，将 nums[1] 追加到 arr1 。在第二次操作中，将 nums[2] 追加到 arr2 。之后，在第 i 次操作中：
#
# 如果 greaterCount(arr1, nums[i]) > greaterCount(arr2, nums[i]) ，将 nums[i] 追加到 arr1 。
# 如果 greaterCount(arr1, nums[i]) < greaterCount(arr2, nums[i]) ，将 nums[i] 追加到 arr2 。
# 如果 greaterCount(arr1, nums[i]) == greaterCount(arr2, nums[i]) ，将 nums[i] 追加到元素数量较少的数组中。
# 如果仍然相等，那么将 nums[i] 追加到 arr1 。
# 连接数组 arr1 和 arr2 形成数组 result 。例如，如果 arr1 == [1,2,3] 且 arr2 == [4,5,6] ，那么 result = [1,2,3,4,5,6] 。
#
# 返回整数数组 result 。
#
#
#
# 示例 1：
#
# 输入：nums = [2,1,3,3]
# 输出：[2,3,1,3]
# 解释：在前两次操作后，arr1 = [2] ，arr2 = [1] 。
# 在第 3 次操作中，两个数组中大于 3 的元素数量都是零，并且长度相等，因此，将 nums[3] 追加到 arr1 。
# 在第 4 次操作中，两个数组中大于 3 的元素数量都是零，但 arr2 的长度较小，因此，将 nums[4] 追加到 arr2 。
# 在 4 次操作后，arr1 = [2,3] ，arr2 = [1,3] 。
# 因此，连接形成的数组 result 是 [2,3,1,3] 。
# 示例 2：
#
# 输入：nums = [5,14,3,1,2]
# 输出：[5,3,1,2,14]
# 解释：在前两次操作后，arr1 = [5] ，arr2 = [14] 。
# 在第 3 次操作中，两个数组中大于 3 的元素数量都是一，并且长度相等，因此，将 nums[3] 追加到 arr1 。
# 在第 4 次操作中，arr1 中大于 1 的元素数量大于 arr2 中的数量（2 > 1），因此，将 nums[4] 追加到 arr1 。
# 在第 5 次操作中，arr1 中大于 2 的元素数量大于 arr2 中的数量（2 > 1），因此，将 nums[5] 追加到 arr1 。
# 在 5 次操作后，arr1 = [5,3,1,2] ，arr2 = [14] 。
# 因此，连接形成的数组 result 是 [5,3,1,2,14] 。
# 示例 3：
#
# 输入：nums = [3,3,3,3]
# 输出：[3,3,3,3]
# 解释：在 4 次操作后，arr1 = [3,3] ，arr2 = [3,3] 。
# 因此，连接形成的数组 result 是 [3,3,3,3] 。
#
#
# 提示：
#
# 3 <= n <= 105
# 1 <= nums[i] <= 109

from leetcode.allcode.competition.mypackage import *

class Fenwick:
    __slots__ = 'nums', 'tree'

    def __init__(self, n: int):
        tree = [0] * (n + 1)
        self.nums = [0] * n
        self.tree = tree

    def update(self, index: int, val: int) -> None:
        # delta = val - self.nums[index]
        delta = val
        self.nums[index] = val
        i = index + 1
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & -i  # lowbit

    def prefixSum(self, i: int) -> int:
        s = 0
        while i:
            s += self.tree[i]
            i &= i - 1  # i -= i & -i 的另一种写法
        return s

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum(right + 1) - self.prefixSum(left)


class Solution:
    def resultArray1(self, nums: List[int]) -> List[int]:
        arr1, arr2 = [nums[0]], [nums[1]]
        sa1, sa2 = SortedList([nums[0]]), SortedList([nums[1]])
        for x in nums[2:]:
            n1, n2 = len(arr1), len(arr2)
            p1 = sa1.bisect_right(x)
            p2 = sa2.bisect_right(x)
            if n1 - p1 > n2 - p2:
                arr1.append(x)
                sa1.add(x)
            elif n1 - p1 < n2 - p2:
                arr2.append(x)
                sa2.add(x)
            else:
                if n1 <= n2:
                    arr1.append(x)
                    sa1.add(x)
                else:
                    arr2.append(x)
                    sa2.add(x)
        return arr1 + arr2

    def resultArray(self, nums: List[int]) -> List[int]:
        sub = sorted(list(set(nums)))
        x2i = {x: i for i, x in enumerate(sub)}
        n = len(nums)
        arr1, arr2 = [nums[0]], [nums[1]]
        for i, x in enumerate(nums):
            nums[i] = x2i[x]
        f1, f2 = Fenwick(n), Fenwick(n)
        f1.update(nums[0], 1)
        f2.update(nums[1], 1)
        for x in nums[2:]:
            v1, v2 = f1.prefixSum(n) - f1.prefixSum(x+1), f2.prefixSum(n) - f2.prefixSum(x+1)
            if v1 > v2:
                arr1.append(sub[x])
                f1.update(x, 1)
            elif v1 < v2:
                arr2.append(sub[x])
                f2.update(x, 1)
            elif len(arr1) > len(arr2):
                arr2.append(sub[x])
                f2.update(x, 1)
            else:
                arr1.append(sub[x])
                f1.update(x, 1)
        return arr1 + arr2



so = Solution()
print(so.resultArray([2,38,2]))
print(so.resultArray([2,1,3,3]))
print(so.resultArray([2,38,2]))
print(so.resultArray([5,14,3,1,2]))
print(so.resultArray([3,3,3,3]))




