# 给定两个以 非递减顺序排列 的整数数组 nums1 和 nums2 , 以及一个整数 k 。
#
# 定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2 。
#
# 请找到和最小的 k 个数对 (u1,v1),  (u2,v2)  ...  (uk,vk) 。
#
#
#
# 示例 1:
#
# 输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# 输出: [1,2],[1,4],[1,6]
# 解释: 返回序列中的前 3 对数：
#      [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# 示例 2:
#
# 输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# 输出: [1,1],[1,1]
# 解释: 返回序列中的前 2 对数：
#      [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
#
#
# 提示:
#
# 1 <= nums1.length, nums2.length <= 105
# -109 <= nums1[i], nums2[i] <= 109
# nums1 和 nums2 均为 升序排列
# 1 <= k <= 104
# k <= nums1.length * nums2.length

from leetcode.allcode.competition.mypackage import *

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        hp = [[nums1[0] + nums2[0],0,0]]
        vis = set((0, 0))
        ans = []
        for _ in range(k):
            s, i, j = heappop(hp)
            ans.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2) and (i, j + 1) not in vis:
                heappush(hp, [nums1[i] + nums2[j + 1], i, j + 1])
                vis.add((i, j + 1))
            if i + 1 < len(nums1) and (i + 1, j) not in vis:
                heappush(hp, [nums1[i + 1] + nums2[j], i + 1, j])
                vis.add((i + 1, j))
        return ans


so = Solution()
# print(so.removeDigit())




