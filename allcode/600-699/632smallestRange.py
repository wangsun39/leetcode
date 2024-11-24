# 你有k个 非递减排列 的整数列表。找到一个 最小 区间，使得k个列表中的每个列表至少有一个数包含在其中。
#
# 我们定义如果b-a < d-c或者在b-a == d-c时a < c，则区间 [a,b] 比 [c,d] 小。
#
# 
#
# 示例 1：
#
# 输入：nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# 输出：[20,24]
# 解释：
# 列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
# 列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
# 列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
# 示例 2：
#
# 输入：nums = [[1,2,3],[1,2,3],[1,2,3]]
# 输出：[1,1]
# 
#
# 提示：
#
# nums.length == k
# 1 <= k <= 3500
# 1 <= nums[i].length <= 50
# -105 <= nums[i][j] <= 105
# nums[i] 按非递减顺序排列

from leetcode.allcode.competition.mypackage import *

class Solution:
    def smallestRange1(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        idx = [0] * n  # 记录每一行的下标
        hp = []
        mx = -inf
        for i in range(n):
            mx = max(mx, nums[i][0])
            heappush(hp, [nums[i][0], i])
        ans = mx - hp[0][0]
        res = [hp[0][0], mx]
        while True:
            x, row = heappop(hp)
            if idx[row] < len(nums[row]) - 1:
                idx[row] += 1
                v = nums[row][idx[row]]
                mx = max(mx, v)
                heappush(hp, [v, row])
                mn, _ = hp[0]
                if mx - mn < ans:
                    ans = mx - mn
                    res = [mn, mx]
            else:
                break
        return res

    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # 2024/11/24  双指针法，性能不如上面的
        arr = []
        row = len(nums)
        for i, l in enumerate(nums):
            arr += [[i, x] for x in l]
        arr.sort(key=lambda x:[x[1]])
        counter = Counter()  # 统计滑窗内每行有多少个元素
        n = len(arr)
        r = 0
        mn = inf
        for l in range(n):
            while r < n and len(counter) < row:
                a, b = arr[r]
                counter[a] += 1
                r += 1
            if len(counter) < row:
                break
            if mn > arr[r - 1][1] - arr[l][1]:
                ans = [arr[l][1], arr[r - 1][1]]
                mn = arr[r - 1][1] - arr[l][1]
            counter[arr[l][0]] -= 1
            if counter[arr[l][0]] == 0:
                del(counter[arr[l][0]])
        return ans

so = Solution()
print(so.smallestRange(nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]))
print(so.smallestRange(nums = [[1,2,3],[1,2,3],[1,2,3]]))





