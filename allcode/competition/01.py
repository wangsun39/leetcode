

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counter = [0] * 32  # counter[i][j]  表示前i个树中第j列累计有多少个1
        right = 1
        def trans():  # 把counter转换成对应的数字
            v = 0
            for i in range(32):
                if counter[i]:
                    v += (1 << i)
            return v
        def add(v):  # 把v加到counter中
            for i in range(32):
                if v & (1 << i):
                    counter[i] += 1
        def sub(v):  # 把v减到counter中
            for i in range(32):
                if v & (1 << i):
                    counter[i] -= 1
        if k == 0:
            return 1
        ans = inf
        add(nums[0])
        for i, x in enumerate(nums):
            if i > 0:
                sub(nums[i - 1])
            while right < n:
                if trans() < k:
                    add(nums[right])
                    right += 1
                else:
                    break
            if trans() < k:
                break
            ans = min(ans, right - i)
        if ans < inf:
            return ans
        return -1




so = Solution()
print(so.minimumSubarrayLength(nums = [1,2], k = 0))
print(so.minimumSubarrayLength(nums = [1,2,3], k = 2))
print(so.minimumSubarrayLength(nums = [2,1,8], k = 10))




