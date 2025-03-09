

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



