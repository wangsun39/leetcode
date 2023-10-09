from typing import List
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 2:
            return 0
        minN, maxN = min(nums), max(nums)
        average_gap = (maxN - minN) / (N - 1)
        if average_gap == 0:
            return 0
        buckets = []
        for i in range(N):
            buckets.append([None, None])
        for i in nums:
            idx = int((i - minN) / average_gap)
            if buckets[idx][0] is None:
                buckets[idx][0], buckets[idx][1] = i, i
            else:
                buckets[idx][0] = min(i, buckets[idx][0])
                buckets[idx][1] = max(i, buckets[idx][1])
        res = int(average_gap)
        last_max = buckets[0][1]
        for b in buckets[1:]:
            if b[0] is None:
                continue
            b_min, b_max = b[0], b[1]
            res = max(res, b_min - last_max)
            last_max = b_max

        return res



so = Solution();
print(so.maximumGap([1,1,1,1]))
print(so.maximumGap([3,6,9,1]))
# print(so.maximumGap(11))

