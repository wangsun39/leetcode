# 给你两个长度为 n 的整数数组，fruits 和 baskets，其中 fruits[i] 表示第 i 种水果的 数量，baskets[j] 表示第 j 个篮子的 容量。
#
# 你需要对 fruits 数组从左到右按照以下规则放置水果：
#
# 每种水果必须放入第一个 容量大于等于 该水果数量的 最左侧可用篮子 中。
# 每个篮子只能装 一种 水果。
# 如果一种水果 无法放入 任何篮子，它将保持 未放置。
# 返回所有可能分配完成后，剩余未放置的水果种类的数量。
#
#
#
# 示例 1
#
# 输入： fruits = [4,2,5], baskets = [3,5,4]
#
# 输出： 1
#
# 解释：
#
# fruits[0] = 4 放入 baskets[1] = 5。
# fruits[1] = 2 放入 baskets[0] = 3。
# fruits[2] = 5 无法放入 baskets[2] = 4。
# 由于有一种水果未放置，我们返回 1。
#
# 示例 2
#
# 输入： fruits = [3,6,1], baskets = [6,4,7]
#
# 输出： 0
#
# 解释：
#
# fruits[0] = 3 放入 baskets[0] = 6。
# fruits[1] = 6 无法放入 baskets[1] = 4（容量不足），但可以放入下一个可用的篮子 baskets[2] = 7。
# fruits[2] = 1 放入 baskets[1] = 4。
# 由于所有水果都已成功放置，我们返回 0。
#
#
#
# 提示：
#
# n == fruits.length == baskets.length
# 1 <= n <= 100
# 1 <= fruits[i], baskets[i] <= 1000

from leetcode.allcode.competition.mypackage import *

class Fenwick1:
    def __init__(self, n):
        self.n = n
        self.f = [0] * (n + 1)
        self.nums = [0] * (n + 1)

    def update(self, idx, value):
        self.nums[idx] = value

        while idx <= self.n:
            max_val = self.nums[idx]
            parent_idx = idx - (idx & -idx) + 1
            for i in range(parent_idx, idx + 1):
                max_val = max(max_val, self.nums[i])

            self.f[idx] = max_val
            idx += idx & -idx

    def query(self, idx):
        max_val = 0
        while idx > 0:
            max_val = max(max_val, self.f[idx])
            idx -= idx & -idx
        return max_val

class Fenwick2:
    def __init__(self, n):
        self.n = n
        self.f = [0] * (n + 1)
        self.nums = [0] * (n + 1)

    def build(self, arr):
        self.nums = [0] + arr
        for idx in range(1, len(arr) + 1):
            self.update(idx, self.nums[idx], force=True)

    def update(self, idx, value, force=False):
        self.nums[idx] = value

        while idx <= self.n:
            if not force:
                left = idx - (idx & -idx) + 1
                right = idx
                max_val = max(self.nums[left:right + 1])
                if self.f[idx] == max_val:
                    break
                self.f[idx] = max_val
            else:
                self.f[idx] = max(self.f[idx], value)

            idx += idx & -idx

    def query(self, idx):
        max_val = 0
        while idx > 0:
            max_val = max(max_val, self.f[idx])
            idx -= idx & -idx
        return max_val


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n, m = len(fruits), len(baskets)
        fw = Fenwick2(m)
        fw.build(baskets)
        # for i, x in enumerate(baskets):
        #     fw.update(i + 1, x)
        ans = 0
        for x in fruits:
            if fw.query(m) < x:
                ans += 1
            else:
                if fw.query(1) >= x:
                    i = 1
                else:
                    lo, hi = 1, m
                    while lo + 1 < hi:
                        mid = (lo + hi) // 2
                        if fw.query(mid) < x:
                            lo = mid
                        else:
                            hi = mid
                    i = hi
                # baskets[i - 1] -= x
                fw.update(i, 0)

        return ans

# class Solution:
#     def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
#         n, m = len(fruits), len(baskets)


so = Solution()
print(so.numOfUnplacedFruits(fruits = [1,4], baskets = [8,1]))
print(so.numOfUnplacedFruits(fruits = [4,2,5], baskets = [3,5,4]))
print(so.numOfUnplacedFruits(fruits = [3,6,1], baskets = [6,4,7]))



