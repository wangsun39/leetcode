

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        n = len(nums)
        enums = list([x - i, i] for i, x in enumerate(nums))
        enums.sort()
        pre = [-1] * n  # pre[i] 表示某一个满足 nums[i] - nums[j] >= i - j 的 j
        if all(x <= 0 for x in nums):
            return max(nums)
        stack = []  # [a, b, c] 其中a为nums[i]-i，b为以nums[i]结尾的最大目标和
        for x, i in enums:
            while stack and stack[-1][1] > i:
                stack.pop()
            if stack:
                pre[i] = stack[-1][1]
            stack.append([x, i])
        g = defaultdict(list)  # 建图，构造先修关系
        for i, x in enumerate(pre):
            g[x].append(i)
        dp = [max(nums[i], 0) for i in range(n)]  # 到达i点的最大值
        q1 = deque(i for i, x in enumerate(pre) if x == -1)
        q2 = deque()
        while q1:
            while q1:
                x = q1.popleft()
                for y in g[x]:
                    q2.append(y)
                    dp[y] = max(dp[y], dp[x] + nums[y])
            q1, q2 = q2, deque()
        return max(dp)




so = Solution()
print(so.maxBalancedSubsequenceSum([-1,4,8,5,8,2,-8]))
print(so.maxBalancedSubsequenceSum([3,3,5,6]))
print(so.maxBalancedSubsequenceSum([5,-1,-3,8]))
print(so.maxBalancedSubsequenceSum([-2,-1]))




