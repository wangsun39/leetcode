# 给你一个数组nums，我们可以将它按一个非负整数 k 进行轮调，这样可以使数组变为[nums[k], nums[k + 1], ... nums[nums.length - 1], nums[0], nums[1], ..., nums[k-1]]的形式。此后，任何值小于或等于其索引的项都可以记作一分。
#
# 例如，数组为nums = [2,4,1,3,0]，我们按k = 2进行轮调后，它将变成[1,3,0,2,4]。这将记为 3 分，因为 1 > 0 [不计分]、3 > 1 [不计分]、0 <= 2 [计 1 分]、2 <= 3 [计 1 分]，4 <= 4 [计 1 分]。
# 在所有可能的轮调中，返回我们所能得到的最高分数对应的轮调下标 k 。如果有多个答案，返回满足条件的最小的下标 k 。
#
#
#
# 示例 1：
#
# 输入：nums = [2,3,1,4,0]
# 输出：3
# 解释：
# 下面列出了每个 k 的得分：
# k = 0,  nums = [2,3,1,4,0],    score 2
# k = 1,  nums = [3,1,4,0,2],    score 3
# k = 2,  nums = [1,4,0,2,3],    score 3
# k = 3,  nums = [4,0,2,3,1],    score 4
# k = 4,  nums = [0,2,3,1,4],    score 3
# 所以我们应当选择k = 3，得分最高。
# 示例 2：
#
# 输入：nums = [1,3,0,2,4]
# 输出：0
# 解释：
# nums 无论怎么变化总是有 3 分。
# 所以我们将选择最小的 k，即 0。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 0 <= nums[i] < nums.length
from bisect import bisect_left, insort_left
from typing import List
from sortedcontainers import SortedList

class Solution:
    def bestRotation1(self, nums: List[int]) -> int:
        N = len(nums)
        l = [0] * N
        for i, e in enumerate(nums):
            if i >= e:
                # for j in range(i - e + 1):
                #     l[j] += 1
                l[0] += 1
                if i - e + 1 < N:
                    l[i - e + 1] -= 1
                # for j in range(i + 1, N):
                #     l[j] += 1
                if i + 1 < N:
                    l[i + 1] += 1
            else:
                # for j in range(i + 1, i + N - e + 1):
                #     l[j] += 1
                if i + 1 < N:
                    l[i + 1] += 1
                if i < e - 1:
                    l[i + N - e + 1] -= 1
        print(l)
        s = [l[0]]
        for e in l[1:]:
            s.append(e + s[-1])
        print(s)
        maxV = 0
        idx = 0
        for i in range(N):
            if maxV < s[i]:
                idx = i
                maxV = s[i]
        return idx

    def bestRotation(self, nums: List[int]) -> int:
        # 二分法，可以通过，但性能不高
        l, r = SortedList(), SortedList(i - x for i, x in enumerate(nums))  # 将 nums 分成左右两部分考虑，l 会移动到 r 右侧
        n = len(nums)
        mx = base = sum(x >= 0 for x in r)
        ans = 0
        for k in range(n):
            # l 中的元素移动后，每项都会增加 n - k
            # r 中的元素移动后，每项都会减少 k
            pl1 = l.bisect_left(-(n - k))
            pl2 = l.bisect_left(0)  # l[pl1: pl2] 中的元素都会增加1分
            pr1 = r.bisect_left(0)
            pr2 = r.bisect_left(k)  # l[pl1: pl2] 中的元素都会减少1分
            if base + (pl2 - pl1) - (pr2 - pr1) > mx:
                mx = base + (pl2 - pl1) - (pr2 - pr1)
                ans = k
            l.add(k - nums[k])
            r.remove(k - nums[k])
        return ans



so = Solution()
print(so.bestRotation([2,3,1,4,0]))   # 3
print(so.bestRotation([1,3,0,2,4]))   # 0

