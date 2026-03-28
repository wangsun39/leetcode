

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class STree2:
    # 非动态开点，单点更新，区间查询
    def __init__(self, n: int):
        # self.n = n
        self.max = [0] * (2 << n.bit_length())  # 相比 4n 空间更小
        self.min = [0] * (2 << n.bit_length())  # 相比 4n 空间更小
        self.n = n

    # 线段树：把下标 i 上的元素值增加 val，单点更新
    # o 是当前区间对应的下标，[l, r]当前区间的范围
    # 调用入口update(1,1,n,...) 或 update(1,0,n-1,...) 根据实际需要填写，l和r一般和L和R的范围一致就可以，不会产生越界
    def update(self, o: int, l: int, r: int, i: int, val: int) -> None:
        if l == r:
            self.max[o] = self.min[o] = val
            return
        m = (l + r) // 2
        if i <= m:
            self.update(o * 2, l, m, i, val)
        else:
            self.update(o * 2 + 1, m + 1, r, i, val)
        self.max[o] = MAX(self.max[o * 2], self.max[o * 2 + 1])
        self.min[o] = MIN(self.min[o * 2], self.min[o * 2 + 1])

    # 线段树：返回区间 [L,R] 内的元素和，区间查询最大值
    # 调用入口 query(1,1,n,...) 或 query(1,0,n-1,...)
    def query(self, o: int, l: int, r: int, L: int, R: int) -> [int, int]:
        if L <= l and r <= R:
            return [self.max[o], self.min[o]]
        res = [0, inf]
        m = (l + r) // 2
        if L <= m:
            mx, mn = self.query(o * 2, l, m, L, R)
            res = MAX(res[0], mx), MIN(res[1], mn)
        if R > m:
            mx, mn = self.query(o * 2 + 1, m + 1, r, L, R)
            res = MAX(res[0], mx), MIN(res[1], mn)
        return res

    def query2(self, L, R):
        mx, mn = self.query(1, 0, self.n - 1, L, R)
        return mx - mn

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        st = STree2(n)
        for i, x in enumerate(nums):
            st.update(1, 0, n - 1, i, x)

        hp = []
        for i in range(n):
            heappush(hp, [-st.query2(i, n - 1), i, n - 1])

        ans = 0
        for _ in range(k):
            x, L, R = heappop(hp)
            ans += -x
            if L < R:
                heappush(hp, [-st.query2(L, R - 1), L, R - 1])

        return ans



so = Solution()
print(so.maxTotalValue(nums = [1,3,2], k = 2))
print(so.maxTotalValue(nums = [4,2,5,1], k = 3))




