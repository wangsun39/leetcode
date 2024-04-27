# 给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。
#
# 你需要返回给定数组中的重要翻转对的数量。
#
# 示例 1:
#
# 输入: [1,3,2,3,1]
# 输出: 2
# 示例 2:
#
# 输入: [2,4,3,5,1]
# 输出: 3
# 注意:
#
# 给定数组的长度不会超过50000。
# 输入数组中的所有数字都在32位整数的表示范围内。


from leetcode.allcode.competition.mypackage import *

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        sortList = []
        res = 0
        for n, e in enumerate(nums): # n 代表sortList个数
            pos = bisect_right(sortList, e * 2)
            res += (n - pos)
            # pos = bisect.bisect_right(sortList, e)
            # sortList = sortList[:pos] + [e] + sortList[pos:]
            insort_right(sortList, e)
        return res

# 归并排序的方法
    def reversePairs1(self, nums: List[int]) -> int:
        def helper(nums):  # 返回 nums 的翻转对数目，并将nums 排序
            N = len(nums)
            if N < 2:
                return 0, nums
            print(nums[:N//2])
            res1, nums1 = helper(nums[:N//2])  # 把nums分成两半，每段递归
            res2, nums2 = helper(nums[N//2:])
            i, j, res = 0, 0, 0
            N1, N2 = len(nums1), len(nums2)
            while i < N1 and j < N2:  # 计算出  nums1 和 nums2 之间的翻转对
                if nums1[i] > nums2[j] * 2:
                    res += (N1 - i)
                    j += 1
                else:
                    i += 1
            i, j = 0, 0
            numsRes = []
            while i < N1 and j < N2:  # 归并排序
                if nums1[i] <= nums2[j]:
                    numsRes.append(nums1[i])
                    i += 1
                else:
                    numsRes.append(nums2[j])
                    j += 1
            if i == N1:
                while j < N2:
                    numsRes.append(nums2[j])
                    j += 1
            else:
                while i < N1:
                    numsRes.append(nums1[i])
                    i += 1
            return res + res1 + res2, numsRes
        return helper(nums)[0]


    def reversePairs2(self, nums: List[int]) -> int:
        # 2024/4/27 SortedList
        sl = SortedList()
        n = len(nums)
        ans = 0
        for i in range(n - 1, -1, -1):
            p = sl.bisect_left(nums[i])
            ans += p
            sl.add(nums[i] * 2)
        return ans



so = Solution()
print(so.reversePairs2([1,3,2,3,1]))   # 2
print(so.reversePairs2([1,3,2,3,1]))  # 2

