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


so = Solution()
print(so.lengthOfLIS(nums = [4,2,1,4,3,4,5,8,15], k = 3))
print(so.lengthOfLIS(nums = [7,4,5,1,8,12,4,7], k = 5))
print(so.lengthOfLIS(nums = [1,5], k = 1))




