# 给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，长度为 n 。
#
# 数组 nums1 和 nums2 的 差值平方和 定义为所有满足 0 <= i < n 的 (nums1[i] - nums2[i])2 之和。
#
# 同时给你两个正整数 k1 和 k2 。你可以将 nums1 中的任意元素 +1 或者 -1 至多 k1 次。类似的，你可以将 nums2 中的任意元素 +1 或者 -1 至多 k2 次。
#
# 请你返回修改数组 nums1 至多 k1 次且修改数组 nums2 至多 k2 次后的最小 差值平方和 。
#
# 注意：你可以将数组中的元素变成 负 整数。
#
#
#
# 示例 1：
#
# 输入：nums1 = [1,2,3,4], nums2 = [2,10,20,19], k1 = 0, k2 = 0
# 输出：579
# 解释：nums1 和 nums2 中的元素不能修改，因为 k1 = 0 和 k2 = 0 。
# 差值平方和为：(1 - 2)2 + (2 - 10)2 + (3 - 20)2 + (4 - 19)2 = 579 。
# 示例 2：
#
# 输入：nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1
# 输出：43
# 解释：一种得到最小差值平方和的方式为：
# - 将 nums1[0] 增加一次。
# - 将 nums2[2] 增加一次。
# 最小差值平方和为：
# (2 - 5)2 + (4 - 8)2 + (10 - 7)2 + (12 - 9)2 = 43 。
# 注意，也有其他方式可以得到最小差值平方和，但没有得到比 43 更小答案的方案。
#
#
# 提示：
#
# n == nums1.length == nums2.length
# 1 <= n <= 105
# 0 <= nums1[i], nums2[i] <= 105
# 0 <= k1, k2 <= 109


from leetcode.allcode.competition.mypackage import *

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1)
        d = [abs(nums1[i] - nums2[i]) for i in range(n)]
        counter = Counter(d)
        counter = deque(sorted([[c, v] for c, v in counter.items() if c > 0], reverse=True))
        counter.append([0, 0])  # 增加一个哨兵
        k = k1 + k2  # k1和k2合并起来看
        while counter:
            if counter[0][0] == 0 or k == 0:
                break
            c0, v0 = counter[0]
            c1, v1 = counter[1]
            counter.popleft()
            if (c0 - c1) * v0 <= k:
                counter[0] = [c1, v0 + v1]  # 把差值最大的都变成差值次大的
                k -= (c0 - c1) * v0
            else:
                q, r = divmod(k, v0)  # 剩下的k不足以把差值最大的全部变成差值次大的，只能平均变化
                counter.appendleft([c0 - q - 1, r])
                counter.appendleft([c0 - q, v0 - r])
                break
        return sum(c * c * v for c, v in counter)





so = Solution()
print(so.minSumSquareDiff(nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1))
print(so.minSumSquareDiff(nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 10, k2 = 5))
print(so.minSumSquareDiff(nums1 = [1,2,3,4], nums2 = [2,10,20,19], k1 = 0, k2 = 0))




