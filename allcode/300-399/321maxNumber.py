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
        def merge1(l1, l2):
            # 这个写法性能高，但复杂
            res = []
            if 0 == len(l1):
                return l2
            if 0 == len(l2):
                return l1
            i = j = 0
            while i < len(l1) and j < len(l2):
                if l1[i] < l2[j]:
                    res.append(l2[j])
                    j += 1
                elif l1[i] > l2[j]:
                    res.append(l1[i])
                    i += 1
                else:
                    ii, jj = i, j
                    first_diffi = -1
                    while ii < len(l1) and jj < len(l2) and l1[ii] == l2[jj]:
                        ii += 1
                        jj += 1
                        if ii < len(l1) and l1[ii] != l1[i] and first_diffi == -1:
                            first_diffi = ii
                            first_diffj = jj
                    if ii == len(l1) and jj == len(l2):
                        cmp = 0  # 相等
                    elif ii == len(l1):
                        cmp = -1  # 1小
                    elif jj == len(l2):
                        cmp = 1   # 1 大
                    else:
                        if l1[ii] < l2[jj]:
                            cmp = -1  # 1小
                        else:
                            cmp = 1  # 1 大
                    if first_diffi == -1:
                        if cmp == 0:
                            return res + l1[i:] + l2[j:]
                        if cmp < 0:
                            res += l2[j: jj]
                            j = jj
                        else:
                            res += l1[i: ii]
                            i = ii
                    else:
                        if cmp == 0:
                            res += l1[i: first_diffi]
                            i = first_diffi
                        if cmp < 0:
                            res += l2[j: first_diffj]
                            j = first_diffj
                        else:
                            res += l1[i: first_diffi]
                            i = first_diffi
            if i < len(l1):
                res += l1[i:]
            if j < len(l2):
                res += l2[j:]
            return res
        def merge(l1, l2):
            # 改用这个写法更简单的merge函数,性能略低，便于理解
            res = []
            if 0 == len(l1):
                return l2
            if 0 == len(l2):
                return l1
            i = j = 0
            while i < len(l1) and j < len(l2):
                if l1[i:] < l2[j:]:
                    res.append(l2[j])
                    j += 1
                else:
                    res.append(l1[i])
                    i += 1
            if i < len(l1):
                res += l1[i:]
            if j < len(l2):
                res += l2[j:]
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
print(so.maxNumber(nums1 = [5,0,2,1,0,1,0,3,9,1,2,8,0,9,8,1,4,7,3], nums2 = [7,6,7,1,0,1,0,5,6,0,5,0], k = 31))
print(so.maxNumber(nums1 = [3,8,5,3,4], nums2 = [8,7,3,6,8], k = 5))
print(so.maxNumber(nums1 = [5,1,0], nums2 = [5,2,1], k = 3))
print(so.maxNumber(nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5))
print(so.maxNumber(nums1 = [6,7], nums2 = [6,0,4], k = 5))
print(so.maxNumber(nums1 = [3,9], nums2 = [8,9], k = 3))




