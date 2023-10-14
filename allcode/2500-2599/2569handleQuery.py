# 给你两个下标从 0 开始的数组 nums1 和 nums2 ，和一个二维数组 queries 表示一些操作。总共有 3 种类型的操作：
#
# 操作类型 1 为 queries[i] = [1, l, r] 。你需要将 nums1 从下标 l 到下标 r 的所有 0 反转成 1 以及所有 1 反转成 0 。l 和 r 下标都从 0 开始。
# 操作类型 2 为 queries[i] = [2, p, 0] 。对于 0 <= i < n 中的所有下标，令 nums2[i] = nums2[i] + nums1[i] * p 。
# 操作类型 3 为 queries[i] = [3, 0, 0] 。求 nums2 中所有元素的和。
# 请你返回一个数组，包含所有第三种操作类型的答案。
#
#
#
# 示例 1：
#
# 输入：nums1 = [1,0,1], nums2 = [0,0,0], queries = [[1,1,1],[2,1,0],[3,0,0]]
# 输出：[3]
# 解释：第一个操作后 nums1 变为 [1,1,1] 。第二个操作后，nums2 变成 [1,1,1] ，所以第三个操作的答案为 3 。所以返回 [3] 。
# 示例 2：
#
# 输入：nums1 = [1], nums2 = [5], queries = [[2,0,0],[3,0,0]]
# 输出：[5]
# 解释：第一个操作后，nums2 保持不变为 [5] ，所以第二个操作的答案是 5 。所以返回 [5] 。
#
#
# 提示：
#
# 1 <= nums1.length,nums2.length <= 105
# nums1.length = nums2.length
# 1 <= queries.length <= 105
# queries[i].length = 3
# 0 <= l <= r <= nums1.length - 1
# 0 <= p <= 106
# 0 <= nums1[i] <= 1
# 0 <= nums2[i] <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        todo = [False] * (4 * n)
        cnt = [0] * (4 * n)  # 记录每个特殊区间和

        def mt(o):
            cnt[o] = cnt[o * 2] + cnt[o * 2 + 1]

        def do(o, l, r):
            cnt[o] = (r - l + 1) - cnt[o]
            todo[o] = not todo[o]

        # 初始化线段树   o,l,r=1,1,n
        def build(o: int, l: int, r: int) -> None:
            if l == r:
                cnt[o] = nums1[l - 1]
                return
            m = (l + r) // 2
            build(o * 2, l, m)
            build(o * 2 + 1, m + 1, r)
            mt(o)


        # 反转区间 [L,R]   o,l,r=1,1,n
        def update(o: int, l: int, r: int, L: int, R: int) -> None:
            if L <= l and r <= R:
                # ...
                do(o, l, r)
                return
            m = (l + r) // 2
            if todo[o]:
                # ...
                do(o * 2, l, m)
                do(o * 2 + 1, m + 1, r)
                todo[o] = False
            if m >= L: update(o * 2, l, m, L, R)
            if m < R: update(o * 2 + 1, m + 1, r, L, R)
            mt(o)

        cur = 0
        s2 = sum(nums2)
        build(1, 1, n)
        ans = []
        for t, L, R in queries:
            if t == 1: update(1, 1, n, L + 1, R + 1)
            elif t == 2: cur += L * cnt[1]
            else: ans.append(cur + s2)

        return ans





so = Solution()
print(so.handleQuery(nums1 = [1,0,1], nums2 = [0,0,0], queries = [[1,1,1],[2,1,0],[3,0,0]]))
print(so.handleQuery(nums1 = [1], nums2 = [5], queries = [[2,0,0],[3,0,0]]))




