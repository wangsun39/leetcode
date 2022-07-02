# 在整数数组 nums 中，是否存在两个下标 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值小于等于 t ，且满足 i 和 j 的差的绝对值也小于等于 ķ 。
#
# 如果存在则返回 true，不存在返回 false。
#
#  
#
# 示例 1:
#
# 输入: nums = [1,2,3,1], k = 3, t = 0
# 输出: true
# 示例 2:
#
# 输入: nums = [1,0,1,1], k = 1, t = 2
# 输出: true
# 示例 3:
#
# 输入: nums = [1,5,9,1,5,9], k = 2, t = 3
# 输出: false


from typing import List
class Solution:
    def containsNearbyAlmostDuplicate1(self, nums: List[int], k: int, t: int) -> bool:
        N = len(nums)
        if k > N:
            k = N
        if N <= 1 or 0 == k:
            return False
        kList = [nums[0]]
        low, high = 0, k
        def find(k_list, e):
            N = len(k_list)
            i, j = 0, N - 1
            if k_list[j] < e:
                return False, N
            if k_list[i] > e:
                return False, 0
            if k_list[i] == e:
                return True, i
            if k_list[j] == e:
                return True, j
            while i < j - 1:
                mid = (i + j) // 2
                if k_list[mid] == e:
                    return True, mid
                elif k_list[mid] < e:
                    i = mid
                else:
                    j = mid
            return False, j
        def delete(kList, pos):
            return kList[:pos] + kList[pos+1:]
        for x in nums[1:]:
            if len(kList) <= k:
                ifFind, pos = find(kList, x - t)
                if ifFind:
                    return True
                if pos < len(kList) and kList[pos] <= x + t:
                    return True
                kList = kList[:pos] + [x] + kList[pos:]
            else:
                ifFind, pos = find(kList, nums[low])
                kList = delete(kList, pos)
                low += 1
                ifFind, pos = find(kList, x - t)
                if ifFind:
                    return True
                if pos < len(kList) and kList[pos] <= x + t:
                    return True
                kList = kList[:pos] + [x] + kList[pos:]
        return False
import math
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if 0 == len(nums):
            return False
        lower, upper = min(nums), max(nums)
        numOfBucket = math.ceil((upper - lower + 1) / (t + 1))
        bucket = {} # [[] for _ in range(numOfBucket)]

        def getBucketIndex(val):
            return (val - lower) // (t + 1)  # 题目要求小于等于t，所以这边是 t + 1
        for i, e in enumerate(nums):
            if i > k:  # 先从bucket中删掉一个最老的元素
                popIdx = getBucketIndex(nums[i - k - 1])
                del bucket[popIdx] # = []
            index = getBucketIndex(e)
            if index in bucket: # len(bucket[index]) > 0:
                return True
            if index > 0 and index - 1 in bucket and abs(bucket[index - 1][0] - e) <= t and i - bucket[index - 1][1] <= k:
                return True
            if index < numOfBucket - 1 and index + 1 in bucket and abs(bucket[index + 1][0] - e) <= t and i - bucket[index + 1][1] <= k:
                return True
            bucket[index] = [e, i]
        return False



so = Solution()
print(so.containsNearbyAlmostDuplicate([7, 2, 8], 2, 1))  # True
print(so.containsNearbyAlmostDuplicate([4, 2], 2, 1))  # False
print(so.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3))  # False
print(so.containsNearbyAlmostDuplicate([1,2,2,3,4,5], 3, 0))  # True
print(so.containsNearbyAlmostDuplicate([], 0, 0))  # False
print(so.containsNearbyAlmostDuplicate([1,2,3,1], 3, 3))  # True
print(so.containsNearbyAlmostDuplicate([1,0,1,1], 1, 2))  # True
print(so.containsNearbyAlmostDuplicate([-2147483648,2147483647], 1, 1))  # False

