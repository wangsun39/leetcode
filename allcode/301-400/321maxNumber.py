# 给你两个整数数组 nums1 和 nums2，它们的长度分别为 m 和 n。数组 nums1 和 nums2 分别代表两个数各位上的数字。同时你也会得到一个整数 k。
#
# 请你利用这两个数组中的数字中创建一个长度为 k <= m + n 的最大数，在这个必须保留来自同一数组的数字的相对顺序。
#
# 返回代表答案的长度为 k 的数组。
#
#
#
# 示例 1：
#
# 输入：nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5
# 输出：[9,8,6,5,3]
# 示例 2：
#
# 输入：nums1 = [6,7], nums2 = [6,0,4], k = 5
# 输出：[6,7,6,0,4]
# 示例 3：
#
# 输入：nums1 = [3,9], nums2 = [8,9], k = 3
# 输出：[9,8,9]
#
#
# 提示：
#
# m == nums1.length
# n == nums2.length
# 1 <= m, n <= 500
# 0 <= nums1[i], nums2[i] <= 9
# 1 <= k <= m + n

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        len1, len2 = len(nums1), len(nums2)
        def select(l, m): # 从l中选m个数，使其最大
            if m == 0: return []
            drop = len(l) - m
            stack = []
            cnt = 0
            for x in l:
                while stack and stack[-1] < x and cnt < drop:
                    stack.pop()
                    cnt += 1
                stack.append(x)
            while cnt < drop:
                stack.pop()
                cnt += 1
            return stack
        def merge(l1, l2):
            @cache
            def dfs(i, j):
                if i == len(l1):
                    return l2[j:]
                if j == len(l2):
                    return l1[i:]
                if l1[i] > l2[j]:
                    return [l1[i]] + dfs(i + 1, j)
                if l1[i] < l2[j]:
                    return [l2[j]] + dfs(i, j + 1)
                return [l1[i]] + max(dfs(i + 1, j), dfs(i, j + 1))
            res = dfs(0, 0)
            # dfs.cache_clear()
            return res
        ans = []
        for i in range(min(k + 1, len1 + 1)):
            # 从nums1中选i个数字，从nums2中选j个数字
            j = k - i
            if j > len2: continue
            l1 = select(nums1, i)
            l2 = select(nums2, j)
            ans = max(ans, merge(l1, l2))
        return ans





so = Solution()
print(so.maxNumber(nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5))
print(so.maxNumber(nums1 = [6,7], nums2 = [6,0,4], k = 5))
print(so.maxNumber(nums1 = [3,9], nums2 = [8,9], k = 3))




