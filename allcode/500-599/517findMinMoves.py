# 假设有 n 台超级洗衣机放在同一排上。开始的时候，每台洗衣机内可能有一定量的衣服，也可能是空的。
#
# 在每一步操作中，你可以选择任意 m (1 <= m <= n) 台洗衣机，与此同时将每台洗衣机的一件衣服送到相邻的一台洗衣机。
#
# 给定一个整数数组 machines 代表从左至右每台洗衣机中的衣物数量，请给出能让所有洗衣机中剩下的衣物的数量相等的 最少的操作步数 。如果不能使每台洗衣机中衣物的数量相等，则返回 -1 。
#
#
#
# 示例 1：
#
# 输入：machines = [1,0,5]
# 输出：3
# 解释：
# 第一步:    1     0 <-- 5    =>    1     1     4
# 第二步:    1 <-- 1 <-- 4    =>    2     1     3
# 第三步:    2     1 <-- 3    =>    2     2     2
# 示例 2：
#
# 输入：machines = [0,3,0]
# 输出：2
# 解释：
# 第一步:    0 <-- 3     0    =>    1     2     0
# 第二步:    1     2 --> 0    =>    1     1     1
# 示例 3：
#
# 输入：machines = [0,2,0]
# 输出：-1
# 解释：
# 不可能让所有三个洗衣机同时剩下相同数量的衣物。
#
#
# 提示：
#
# n == machines.length
# 1 <= n <= 104
# 0 <= machines[i] <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total = sum(machines)
        n = len(machines)
        if total % n: return -1
        avg = total // n
        s = list(accumulate(machines, initial=0))
        ans = 0
        for i, x in enumerate(machines):
            left_expect = i * avg
            right_expect = (n - i - 1) * avg
            left_diff = left_expect - s[i]
            right_diff = right_expect - (s[n] - s[i + 1])
            if left_diff > 0 and right_diff > 0: # 左右两边都是少，那么所有的差值数量都要经过当前的洗衣机
                ans = max(ans, left_diff + right_diff)
            else:  # 左右两边一侧多或一侧少，那么差值大的一侧的衣服数量都要经过当前洗衣机
                # 左右两边都是多，左右两边可以同时给当前的洗衣机
                ans = max(ans, max(abs(left_diff), abs(right_diff)))

        return ans



so = Solution()
print(so.findMinMoves(machines = [1,0,5]))  # 3
print(so.findMinMoves(machines = [0,3,0]))  # 2
print(so.findMinMoves(machines = [0,2,0]))  # -1

