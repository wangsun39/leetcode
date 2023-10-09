# 给定一个非负整数数组 nums 和一个整数 m ，你需要将这个数组分成 m 个非空的连续子数组。
#
# 设计一个算法使得这 m 个子数组各自和的最大值最小。
#
#  
#
# 示例 1：
#
# 输入：nums = [7,2,5,10,8], m = 2
# 输出：18
# 解释：
# 一共有四种方法将 nums 分割为 2 个子数组。 其中最好的方式是将其分为 [7,2,5] 和 [10,8] 。
# 因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
# 示例 2：
#
# 输入：nums = [1,2,3,4,5], m = 2
# 输出：9
# 示例 3：
#
# 输入：nums = [1,4,4], m = 3
# 输出：4
#  
#
# 提示：
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 106
# 1 <= m <= min(50, nums.length)

from typing import List
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # 二分法
        N = len(nums)
        low, high = max(nums), sum(nums)
        def canSplit(maxSeg):
            numSeg, partialSum = 1, 0
            for i in range(N):
                partialSum += nums[i]
                if partialSum > maxSeg:
                    numSeg += 1
                    partialSum = nums[i]
            return numSeg <= m
        if canSplit(low):
            return low
        while low < high - 1:
            mid = (low + high) // 2
            if canSplit(mid):
                high = mid
            else:
                low = mid
        return high

    def splitArray1(self, nums: List[int], m: int) -> int:  # 这个方法会超时
        N = len(nums)
        D = {}
        # s1 = time.time()
        preSum = nums[0]
        preSumList = [preSum]
        for i in range(1, N):
            preSum += nums[i]
            preSumList.append(preSum)
        # print(preSumList)

        for j in range(N):
            D[(j, 1)] = sum([nums[k] for k in range(j + 1)])
        # print('s1', time.time() - s1)
        # print(D)
        for k in range(2, m + 1):
            for j in range(k - 1, N):
                # print(i, j)
                minMax = 999999999999
                for t in range(k - 2, j):
                    # print('xx', i, i + t, i + t + 1, j, k - 1)
                    minMax = min(minMax, max(D[(t, k - 1)], preSumList[j] - preSumList[t]))
                D[(j, k)] = minMax

        # print('s1', time.time() - s1)

        # print(D)
        return D[(N - 1, m)]
