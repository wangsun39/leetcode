

from leetcode.allcode.competition.mypackage import *

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = []
        l1, l2 = [x for x in nums if x > 0], [x for x in nums if x < 0]
        for i in range(len(l1)):
            ans.append(l1[i])
            ans.append(l2[i])
        return ans


so = Solution()
print(so.rearrangeArray(nums = [3,1,-2,-5,2,-4]))




