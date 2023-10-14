# 给你两个长度为 n 、下标从 0 开始的整数数组 nums1 和 nums2 ，另给你一个下标从 1 开始的二维数组 queries ，其中 queries[i] = [xi, yi] 。
#
# 对于第 i 个查询，在所有满足 nums1[j] >= xi 且 nums2[j] >= yi 的下标 j (0 <= j < n) 中，找出 nums1[j] + nums2[j] 的 最大值 ，如果不存在满足条件的 j 则返回 -1 。
#
# 返回数组 answer ，其中 answer[i] 是第 i 个查询的答案。
#
#
#
# 示例 1：
#
# 输入：nums1 = [4,3,1,2], nums2 = [2,4,9,5], queries = [[4,1],[1,3],[2,5]]
# 输出：[6,10,7]
# 解释：
# 对于第 1 个查询：xi = 4 且 yi = 1 ，可以选择下标 j = 0 ，此时 nums1[j] >= 4 且 nums2[j] >= 1 。nums1[j] + nums2[j] 等于 6 ，可以证明 6 是可以获得的最大值。
# 对于第 2 个查询：xi = 1 且 yi = 3 ，可以选择下标 j = 2 ，此时 nums1[j] >= 1 且 nums2[j] >= 3 。nums1[j] + nums2[j] 等于 10 ，可以证明 10 是可以获得的最大值。
# 对于第 3 个查询：xi = 2 且 yi = 5 ，可以选择下标 j = 3 ，此时 nums1[j] >= 2 且 nums2[j] >= 5 。nums1[j] + nums2[j] 等于 7 ，可以证明 7 是可以获得的最大值。
# 因此，我们返回 [6,10,7] 。
# 示例 2：
#
# 输入：nums1 = [3,2,5], nums2 = [2,3,4], queries = [[4,4],[3,2],[1,1]]
# 输出：[9,9,9]
# 解释：对于这个示例，我们可以选择下标 j = 2 ，该下标可以满足每个查询的限制。
# 示例 3：
#
# 输入：nums1 = [2,1], nums2 = [2,3], queries = [[3,3]]
# 输出：[-1]
# 解释：示例中的查询 xi = 3 且 yi = 3 。对于每个下标 j ，都只满足 nums1[j] < xi 或者 nums2[j] < yi 。因此，不存在答案。
#
#
# 提示：
#
# nums1.length == nums2.length
# n == nums1.length
# 1 <= n <= 105
# 1 <= nums1[i], nums2[i] <= 109
# 1 <= queries.length <= 105
# queries[i].length == 2
# xi == queries[i][1]
# yi == queries[i][2]
# 1 <= xi, yi <= 109
from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        zip_num = sorted(zip(nums1, nums2), key=lambda x: x[0], reverse=True)
        ans = [-1] * len(queries)
        q = sorted(enumerate(queries), key=lambda x: x[1][0], reverse=True)
        print(zip_num)
        print(q)
        # 单调栈，stack[i] == [a, b]  a 表示 nums2[k] 中的元素， b 表示 nums1[k] + nums2[k] 中的元素
        # 按 a 递增， b 递减的顺序存放，在栈中的元素都是满足本次查询的
        stack = []
        i = 0  # 记录 zip_num 当前要处理的下标
        for idx, [a, b] in q:
            while i < n and zip_num[i][0] >= a:
                while stack and zip_num[i][0] + zip_num[i][1] >= stack[-1][1]:
                    stack.pop()
                if len(stack) == 0 or zip_num[i][1] >= stack[-1][0]:
                    stack.append([zip_num[i][1], zip_num[i][0] + zip_num[i][1]])
                i += 1
            # 在 单调栈中的元素 对于 nums1 都是满足要求的
            pos = bisect_left(stack, [b,])
            if pos < len(stack):
                ans[idx] = stack[pos][1]
        return ans




so = Solution()
print(so.maximumSumQueries(nums1 = [89,85], nums2 = [53,32], queries = [[75,48]]))
print(so.maximumSumQueries(nums1 = [4,3,1,2], nums2 = [2,4,9,5], queries = [[4,1],[1,3],[2,5]]))
print(so.maximumSumQueries(nums1 = [3,2,5], nums2 = [2,3,4], queries = [[4,4],[3,2],[1,1]]))
print(so.maximumSumQueries(nums1 = [2,1], nums2 = [2,3], queries = [[3,3]]))




