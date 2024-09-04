

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)

        xor_pair = [[0] * n for _ in range(n)]  # 计算区间的[i, j] xor 结果
        xor_max = [[0] * n for _ in range(n)]  # 计算区间的[i, j] 的子区间的 xor 最大值
        for i in range(n):
            xor_pair[i][i] = nums[i]
            xor_max[i][i] = nums[i]

        # 区间DP
        for d in range(1, n):
            for i in range(n - d):
                xor_pair[i][i + d] = xor_pair[i][i + d - 1] ^ xor_pair[i + 1][i + d]

        for d in range(1, n):
            for i in range(n - d):
                xor_max[i][i + d] = max(xor_pair[i][i + d], xor_max[i][i + d - 1], xor_max[i + 1][i + d])

        ans = []
        for i, j in queries:
            ans.append(xor_max[i][j])
        return ans


so = Solution()
print(so.maximumSubarrayXor(nums = [0,7,3,2,8,5,1], queries = [[0,3],[1,5],[2,4],[2,6],[5,6]]))
print(so.maximumSubarrayXor(nums = [2,8,4,32,16,1], queries = [[0,2],[1,4],[0,5]]))




