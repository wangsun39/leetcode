

from leetcode.allcode.competition.mypackage import *

class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        n = len(nums)
        ans = [False] * n
        if k <= n: ans[0] = True
        counter = Counter(nums)
        s = set(range(1, counter[1] + 1))  # 记录nums中所有(<=i)的元素的所有子序列和
        cnt = n - counter[1]  # 记录>i的元素个数
        for i in range(2, n + 1):
            ci = counter[i]
            s2 = set(range(0, i * ci + 1, i))
            if k in s or k in s2:
                ans[i - 1] = True
                s |= s2
                continue
            for x in s:
                for j in range(ci + 1):
                    if x + j * i > k: break
                    s2.add(x + j * i)
            cnt -= ci
            if k in s2:
                ans[i - 1] = True
            else:
                for j in range(1, cnt + 1):
                    if k - j * i in s2:
                        ans[i - 1] = True
                        break
            s = s2
        return ans


so = Solution()
print(so.subsequenceSumAfterCapping(nums = [2,2,2,2,2,2,2,2,2,2,1,1,1,1,1], k = 13))
print(so.subsequenceSumAfterCapping(nums = [1,2,3], k = 2))
print(so.subsequenceSumAfterCapping(nums = [4,3,2,4], k = 5))




