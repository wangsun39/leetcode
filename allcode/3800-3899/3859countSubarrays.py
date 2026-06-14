# 给你一个整数数组 nums 和两个整数 k 和 m。
#
# 返回一个整数，表示满足以下条件的 子数组 的数量：
#
# 子数组 恰好 包含 k 个不同的 整数。
# 在子数组中，每个 不同的 整数 至少 出现 m 次。
# 子数组 是数组中一个连续的、非空 元素序列。
#
#
#
# 示例 1：
#
# 输入： nums = [1,2,1,2,2], k = 2, m = 2
#
# 输出： 2
#
# 解释：
#
# 满足条件的子数组为：
#
# 子数组	不同整数	频率
# [1, 2, 1, 2]	{1, 2} → 2	{1: 2, 2: 2}
# [1, 2, 1, 2, 2]	{1, 2} → 2	{1: 2, 2: 3}
# 因此，答案是 2。
#
# 示例 2：
#
# 输入： nums = [3,1,2,4], k = 2, m = 1
#
# 输出： 3
#
# 解释：
#
# 满足条件的子数组为：
#
# 子数组	不同整数	频率
# [3, 1]	{3, 1} → 2	{3: 1, 1: 1}
# [1, 2]	{1, 2} → 2	{1: 1, 2: 1}
# [2, 4]	{2, 4} → 2	{2: 1, 4: 1}
# 因此，答案是 3。
#
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
# 1 <= k, m <= nums.length

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countSubarrays(self, nums: list[int], k: int, m: int) -> int:
        pos = defaultdict(list)
        for i, x in enumerate(nums):
            pos[x].append(i)
        R = defaultdict(lambda: -1)  # R[x] 表示滑窗内最右侧的x的下标为pos[x][R[x]]

        l = 0
        counter1 = Counter()  # 窗口内满足计数>=m的数
        counter2 = Counter()  # 窗口内计数<m的数
        last = defaultdict(lambda: -1)  # 记录窗口中从右向左第m个x在pos中的下标，即 pos[x][last[x]] 是 x 在窗口中从右向左的位置
        sl = SortedList()  # 对last数组的排序，存放的是 [pos[x][last[x]], x]
        ans = 0

        for r, x in enumerate(nums):
            if x in counter1:
                counter1[x] += 1
            elif x in counter2:
                counter2[x] += 1
                if counter2[x] >= m:
                    counter1[x] = counter2[x]
                    del(counter2[x])
            else:
                if m == 1:
                    counter1[x] = 1
                else:
                    counter2[x] = 1
            while len(counter1) + len(counter2) > k:
                y = nums[l]  # 窗口移除 y
                if y in counter2:
                    counter2[y] -= 1
                    if counter2[y] == 0:
                        del(counter2[y])
                else:
                    counter1[y] -= 1
                    if counter1[y] < m:
                        if counter1[y]:
                            counter2[y] = counter1[y]
                        del(counter1[y])

                # 更新 last[y]
                if pos[y][last[y]] == l:
                    sl.remove([pos[y][last[y]], y])
                    if last[y] < len(pos[y]) - 1 and pos[y][last[y] + 1] < r:
                        last[y] += 1
                        sl.add([pos[y][last[y]], y])
                # 更新 R[y]
                # if pos[y][R[y]] == l:
                #     R[y] = -1
                l += 1

            # 更新last[x]
            if R[x] == -1:
                R[x] = 0
                last[x] = 0
                sl.add([pos[x][last[x]], x])
            else:
                R[x] += 1
                if R[x] - last[x] + 1 > m:  # 窗口内数字超过 m 个时，要右移last，否则last位置不变
                    if [pos[x][last[x]], x] in sl:  # 虽然R[x]不是-1，但也可能曾经出现过，现在已移除窗口
                        sl.remove([pos[x][last[x]], x])
                    last[x] += 1
                    sl.add([pos[x][last[x]], x])

            if len(counter1) == k:
                j, y = sl[0]  # 窗口中last值最小的元素是 y, 下标是 j
                ans += j - l + 1  # 右端点固定 r， 左端点 [l, j] 都是合法的区间，j+1的左端点，y的个数就不足m了
                
        return ans



so = Solution()
print(so.countSubarrays(nums = [1,2,4,3,5,6,7,8,9,10,95505,48946,30887,54807,95565,26274,33387,91886,90046,16239,40382,14290,29965,12,11,14,13,15,16,17,18,87312,45751,83373,92182,87048,6285,16,87876,19495,27827,71375,84693,19,20,21,22,24,23,25,26,28,27,29,30,31,32,34,33,36,35,38,37,39,40,41,42,34883,44,43,46,45], k = 2, m = 1))   # 10
print(so.countSubarrays(nums = [2,2,2,1,1,2,2,3,3], k = 2, m = 2))   # 10
print(so.countSubarrays(nums = [3,1,2,4], k = 2, m = 1))   # 3
print(so.countSubarrays(nums = [1,2,1,2,2], k = 2, m = 2))  # 2





