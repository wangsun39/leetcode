

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        pos = defaultdict(list)  # 记录所有数字x出现的位置
        for i, x in enumerate(nums):
            pos[x].append(i)
        n = len(nums)
        right = [n] * n  # 记录nums[i]右侧第一个比它大的元素位置
        stack = []
        for i, x in enumerate(nums):
            while stack and nums[stack[-1]] < x:
                j = stack.pop()
                right[j] = i
            stack.append(i)
        ans = 0
        for x in pos.keys():
            for i, j in enumerate(pos[x]):
                # i 是x在pos中的下标，j是x在nums中的下标
                p = bisect_left(pos[x], right[j])
                if p < len(pos[x]):
                    ans += p - i
                else:
                    ans += len(pos[x]) - i
        return ans



so = Solution()
print(so.numberOfSubarrays(nums = [6,26,6]))
print(so.numberOfSubarrays(nums = [1,4,3,3,2]))
print(so.numberOfSubarrays(nums = [3,3,3]))
print(so.numberOfSubarrays(nums = [1]))




