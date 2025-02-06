# 给你一个整数数组nums和一个整数k。
#
# 找到nums中满足以下要求的最长子序列：
#
# 子序列 严格递增
# 子序列中相邻元素的差值 不超过k。
# 请你返回满足上述要求的 最长子序列的长度。
#
# 子序列是从一个数组中删除部分元素后，剩余元素不改变顺序得到的数组。
# 
#
#
# 示例 1：
#
# 输入：nums = [4,2,1,4,3,4,5,8,15], k = 3
# 输出：5
# 解释：
# 满足要求的最长子序列是 [1,3,4,5,8] 。
# 子序列长度为 5 ，所以我们返回 5 。
# 注意子序列 [1,3,4,5,8,15] 不满足要求，因为 15 - 8 = 7 大于 3 。
# 示例 2：
#
# 输入：nums = [7,4,5,1,8,12,4,7], k = 5
# 输出：4
# 解释：
# 满足要求的最长子序列是 [4,5,8,12] 。
# 子序列长度为 4 ，所以我们返回 4 。
# 示例 3：
#
# 输入：nums = [1,5], k = 1
# 输出：1
# 解释：
# 满足要求的最长子序列是 [1] 。
# 子序列长度为 1 ，所以我们返回 1 。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i], k <= 105

from leetcode.allcode.competition.mypackage import *

class STree:
    # 动态开点

    def __init__(self):
        self.tree = defaultdict(int)

    def pushup(self, id: int):
        self.tree[id] = max(self.tree[id << 1], self.tree[(id << 1) | 1])

    def update(self, id: int, start: int, end: int, l: int, r: int, val: int):
        if start > r or end < l:
            return
        if start >= l and end <= r:
            self.tree[id] = val
            return
        mid = (start + end) >> 1
        self.update(id << 1, start, mid, l, r, val)
        self.update((id << 1) | 1, mid + 1, end, l, r, val)
        self.pushup(id)

    def query(self, id: int, start: int, end: int, l: int, r: int):
        if start > r or end < l:
            return 0
        if start >= l and end <= r:
            return self.tree[id]
        mid = (start + end) >> 1
        return max(self.query(id << 1, start, mid, l, r), self.query((id << 1) | 1, mid + 1, end, l, r))

class Solution:


    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        ans = 0
        st = STree()
        for num in nums:
            val = st.query(1, 1, int(1e5), max(1, num - k), num - 1) + 1
            st.update(1, 1, int(1e5), num, num, val)
            ans = max(ans, val)
        return ans

class STree2:
    # 非动态开点，单点更新，区间查询
    def __init__(self, n: int):
        self.n = n
        self.max = [0] * (2 << n.bit_length())  # 相比 4n 空间更小

    # 线段树：把下标 i 上的元素值增加 val，单点更新
    # o 是当前区间对应的下标，[l, r]当前区间的范围
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
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        st = STree2(max(nums) + 1)
        for num in nums:
            if num == 1:
                st.update(1, 1, mx, num, 1)
            else:
                val = st.query(1, 1, mx, max(1, num - k), num - 1) + 1
                st.update(1, 1, mx, num, val)
        return st.max[1]

so = Solution()
print(so.lengthOfLIS(nums = [4,2,1,4,3,4,5,8,15], k = 3))
print(so.lengthOfLIS(nums = [7,4,5,1,8,12,4,7], k = 5))
print(so.lengthOfLIS(nums = [1,5], k = 1))




