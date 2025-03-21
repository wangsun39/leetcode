# 给你一个整数 n 和一个在范围 [0, n - 1] 以内的整数 p ，它们表示一个长度为 n 且下标从 0 开始的数组 arr ，数组中除了下标为 p 处是 1 以外，其他所有数都是 0 。
#
# 同时给你一个整数数组 banned ，它包含数组中的一些位置。banned 中第 i 个位置表示 arr[banned[i]] = 0 ，题目保证 banned[i] != p 。
#
# 你可以对 arr 进行 若干次 操作。一次操作中，你选择大小为 k 的一个 子数组 ，并将它 翻转 。在任何一次翻转操作后，你都需要确保 arr 中唯一的 1 不会到达任何 banned 中的位置。换句话说，arr[banned[i]] 始终 保持 0 。
#
# 请你返回一个数组 ans ，对于 [0, n - 1] 之间的任意下标 i ，ans[i] 是将 1 放到位置 i 处的 最少 翻转操作次数，如果无法放到位置 i 处，此数为 -1 。
#
# 子数组 指的是一个数组里一段连续 非空 的元素序列。
# 对于所有的 i ，ans[i] 相互之间独立计算。
# 将一个数组中的元素 翻转 指的是将数组中的值变成 相反顺序 。
#
#
# 示例 1：
#
# 输入：n = 4, p = 0, banned = [1,2], k = 4
# 输出：[0,-1,-1,1]
# 解释：k = 4，所以只有一种可行的翻转操作，就是将整个数组翻转。一开始 1 在位置 0 处，所以将它翻转到位置 0 处需要的操作数为 0 。
# 我们不能将 1 翻转到 banned 中的位置，所以位置 1 和 2 处的答案都是 -1 。
# 通过一次翻转操作，可以将 1 放到位置 3 处，所以位置 3 的答案是 1 。
# 示例 2：
#
# 输入：n = 5, p = 0, banned = [2,4], k = 3
# 输出：[0,-1,-1,-1,-1]
# 解释：这个例子中 1 一开始在位置 0 处，所以此下标的答案为 0 。
# 翻转的子数组长度为 k = 3 ，1 此时在位置 0 处，所以我们可以翻转子数组 [0, 2]，但翻转后的下标 2 在 banned 中，所以不能执行此操作。
# 由于 1 没法离开位置 0 ，所以其他位置的答案都是 -1 。
# 示例 3：
#
# 输入：n = 4, p = 2, banned = [0,1,3], k = 1
# 输出：[-1,-1,0,-1]
# 解释：这个例子中，我们只能对长度为 1 的子数组执行翻转操作，所以 1 无法离开初始位置。
#
#
# 提示：
#
# 1 <= n <= 105
# 0 <= p <= n - 1
# 0 <= banned.length <= n - 1
# 0 <= banned[i] <= n - 1
# 1 <= k <= n
# banned[i] != p
# banned 中的值 互不相同 。

from leetcode.allcode.competition.mypackage import *


class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        ans = [-1] * n
        dp1 = deque([p])
        banned = set(banned)
        sl0 = SortedList(i for i in range(0, n, 2) if i not in banned and i != p)
        sl1 = SortedList(i for i in range(1, n, 2) if i not in banned and i != p)
        step = 1
        ans[p] = 0
        while dp1:
            dp2 = deque()
            while dp1:
                x = dp1.popleft()
                lo = max(x - k + 1, k - 1 - x)   # L+R==x+y L的最小值是0，因此y的最小值是k - 1 - x
                hi = min(x + k - 1, n - 1 + n - k - x)   # R最大值为n - 1， y的最大值为 n - 1 + n - k - x
                if k & 1: # 子区间长度为奇数，那么x和y必须有相同奇偶性
                    if (lo & 1) ^ (x & 1):
                        lo += 1
                else: # 子区间长度为偶数，那么x和y必须有相反奇偶性
                    if (lo & 1) ^ (x & 1) == 0:
                        lo += 1
                if lo & 1:
                    p = sl1.bisect_left(lo)
                    arr = []
                    while p < len(sl1) and sl1[p] <= hi:
                        arr.append(sl1[p])
                        p += 1
                    for y in arr:
                        dp2.append(y)
                        ans[y] = step
                        sl1.remove(y)
                else:
                    p = sl0.bisect_left(lo)
                    arr = []
                    while p < len(sl0) and sl0[p] <= hi:
                        arr.append(sl0[p])
                        p += 1
                    for y in arr:
                        dp2.append(y)
                        ans[y] = step
                        sl0.remove(y)

            dp1 = dp2
            step += 1

        return ans

so = Solution()
print(so.minReverseOperations(n = 5, p = 0, banned = [], k = 2))  # [0,1,2,3,4]
print(so.minReverseOperations(n = 4, p = 0, banned = [], k = 4))  # [0,-1,-1,1]
print(so.minReverseOperations(n = 8, p = 6, banned = [0], k = 5))  # [-1,-1,1,-1,1,-1,0,-1]
print(so.minReverseOperations(n = 5, p = 0, banned = [2,4], k = 3))  # [0,-1,-1,-1,-1]
print(so.minReverseOperations(n = 4, p = 0, banned = [1,2], k = 4))  # [0,-1,-1,1]
print(so.minReverseOperations(n = 4, p = 2, banned = [0,1,3], k = 1))  # [-1,-1,0,-1]




