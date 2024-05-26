import math

from leetcode.allcode.competition.mypackage import *

# MX = 10 ** 6 + 1
# divisors = [[] for _ in range(MX)]  # divisors[i] 表示 i 的所有因子
# for i in range(1, MX):  # 预处理每个数的所有因子，时间复杂度 O(MlogM)，M=1e5
#     for j in range(i, MX, i):
#         divisors[j].append(i)


class Solution:
    def numberOfPairs1(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums1 = [x // k for x in nums1 if x % k == 0]
        ans = 0
        cnt = defaultdict(int)  # cnt[i] 表示处理的过的数中含有因子i的数的个数
        for x in nums1:
            for v in divisors[x]:
                cnt[v] += 1
        for x in nums2:
            ans += cnt[x]
        return ans
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def factors(x):
            res = []
            i = 1
            while i * i <= x:
                if x % i == 0:
                    res.append(i)
                    if i * i != x:
                        res.append(x // i)
                i += 1
            return res
        nums1 = [x // k for x in nums1 if x % k == 0]
        ans = 0
        cnt = defaultdict(int)  # cnt[i] 表示处理的过的数中含有因子i的数的个数
        for x in nums1:
            divisors = factors(x)
            for v in divisors:
                cnt[v] += 1
        for x in nums2:
            ans += cnt[x]
        return ans


so = Solution()
print(so.numberOfPairs(nums1 = [1,2,4,12], nums2 = [2,4], k = 3))
print(so.numberOfPairs(nums1 = [1,3,4], nums2 = [1,3,4], k = 1))




