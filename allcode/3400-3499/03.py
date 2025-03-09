

from leetcode.allcode.competition.mypackage import *

class STree2:
    # 非动态开点，单点更新，区间查询
    def __init__(self, n: int):
        # self.n = n
        self.max = [0] * (2 << n.bit_length())  # 相比 4n 空间更小

    # 线段树：把下标 i 上的元素值增加 val，单点更新
    # o 是当前区间对应的下标，[l, r]当前区间的范围
    # 调用入口update(1,1,n,...) 或 update(1,0,n-1,...) 根据实际需要填写，l和r一般和L和R的范围一致就可以，不会产生越界
    def update(self, o: int, l: int, r: int, i: int, val: int) -> None:
        if l == r:
            self.max[o] = val
            return
        m = (l + r) // 2
        if i <= m:
            self.update(o * 2, l, m, i, val)
        else:
            self.update(o * 2 + 1, m + 1, r, i, val)
        self.max[o] = max(self.max[o * 2], self.max[o * 2 + 1])

    # 线段树：返回区间 [L,R] 内的元素和，区间查询最大值
    # 调用入口 query(1,1,n,...) 或 query(1,0,n-1,...)
    def query(self, o: int, l: int, r: int, L: int, R: int) -> int:
        if L <= l and r <= R:
            return self.max[o]
        res = 0
        m = (l + r) // 2
        if L <= m:
            res = max(res, self.query(o * 2, l, m, L, R))
        if R > m:
            res = max(res, self.query(o * 2 + 1, m + 1, r, L, R))
        return res


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n, m = len(fruits), len(baskets)
        st = STree2(m)
        for i, x in enumerate(baskets):
            st.update(1,1,m,i + 1, x)
        ans = 0
        for x in fruits:
            if st.query(1,1,m,1,m) < x:
                ans += 1
            else:
                if st.query(1,1,m,1,1) >= x:
                    i = 1
                else:
                    lo, hi = 1, m
                    while lo + 1 < hi:
                        mid = (lo + hi) // 2
                        if st.query(1,1,m,1,mid) < x:
                            lo = mid
                        else:
                            hi = mid
                    i = hi
                # baskets[i - 1] -= x
                st.update(1,1,m,i, 0)

        return ans


so = Solution()
print(so.numOfUnplacedFruits(fruits = [1,4], baskets = [8,1]))
print(so.numOfUnplacedFruits(fruits = [4,2,5], baskets = [3,5,4]))
print(so.numOfUnplacedFruits(fruits = [3,6,1], baskets = [6,4,7]))




