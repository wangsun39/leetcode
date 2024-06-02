

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        pos = [inf] * 32  # 记录每个bit位为0的最后下标
        ans = min(abs(x - k) for x in nums)
        for i, x in enumerate(nums):
            orig = x
            pp = []
            for j in range(32):
                if (x >> j) & 1:
                    if pos[j] < inf:
                        pp.append(pos[j])
                else:
                    pos[j] = i
            pp.sort(reverse=True)
            y = orig
            for t in pp:
                y &= nums[t]
                ans = min(ans, abs(k - y))
        return ans




so = Solution()
print(so.minimumDifference([44,60,63,79,38], 18))
print(so.minimumDifference([5,13,90,92,49], 10))  # 2
print(so.minimumDifference(nums = [1,2,4,5], k = 3))
print(so.minimumDifference(nums = [1,2,1,2], k = 2))
print(so.minimumDifference(nums = [1], k = 10))

a = [44,60,63,79,38]
for i in range(5):
    v = a[i]
    for j in range(i, 5):
        v &= a[j]
        if abs(v - 18) == 3:
            print(i, j, v)



