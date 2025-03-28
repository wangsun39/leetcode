# 给你一个整数数组 arr ，你一开始在数组的第一个元素处（下标为 0）。
#
# 每一步，你可以从下标 i 跳到下标 i + 1 、i - 1 或者 j ：
#
# i + 1 需满足：i + 1 < arr.length
# i - 1 需满足：i - 1 >= 0
# j 需满足：arr[i] == arr[j] 且 i != j
# 请你返回到达数组最后一个元素的下标处所需的 最少操作次数 。
#
# 注意：任何时候你都不能跳到数组外面。
#
#
#
# 示例 1：
#
# 输入：arr = [100,-23,-23,404,100,23,23,23,3,404]
# 输出：3
# 解释：那你需要跳跃 3 次，下标依次为 0 --> 4 --> 3 --> 9 。下标 9 为数组的最后一个元素的下标。
# 示例 2：
#
# 输入：arr = [7]
# 输出：0
# 解释：一开始就在最后一个元素处，所以你不需要跳跃。
# 示例 3：
#
# 输入：arr = [7,6,9,6,9,6,9,7]
# 输出：1
# 解释：你可以直接从下标 0 处跳到下标 7 处，也就是数组的最后一个元素处。
#
#
# 提示：
#
# 1 <= arr.length <= 5 * 104
# -108 <= arr[i] <= 108

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        d = defaultdict(list)
        for i, x in enumerate(arr):
            d[x].append(i)
        dq1 = deque([n - 1])
        vis = [0] * n
        vis[-1] = 1

        while dq1:
            dq2 = deque()
            while dq1:
                x = dq1.popleft()
                if x == 0: return ans
                for y in d[arr[x]]:
                    if y != x:
                        if vis[y]:
                            break
                        dq2.append(y)
                        vis[y] = 1
                if x - 1 >= 0 and not vis[x - 1]:
                    dq2.append(x - 1)
                    vis[x - 1] = 1
                if x + 1 < n and not vis[x + 1]:
                    dq2.append(x + 1)
                    vis[x + 1] = 1
            ans += 1
            dq1 = dq2
        return ans




so = Solution()
print(so.minJumps(arr = [100,-23,-23,404,100,23,23,23,3,404]))
print(so.minJumps(arr = [7]))
print(so.minJumps(arr = [7,6,9,6,9,6,9,7]))




