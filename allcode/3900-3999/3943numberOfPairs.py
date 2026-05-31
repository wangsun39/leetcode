# 给你两个整数数组 nums1 和 nums2，以及一个二维整数数组 queries。
#
# [1, x, y, val]：将 nums2[x..y] 中的每个元素都 增加 val。
# [2, tot]：计算 满足 nums1[j] + nums2[k] == tot 的数对 (j, k) 的数量。
# 返回一个整数数组 answer，其中 answer[j] 表示第 jth 个类型 2 查询的数对数量。
#
#
#
# 示例 1：
#
# 输入： nums1 = [1,2], nums2 = [3,4], queries = [[2,5],[1,0,0,2],[2,5]]
#
# 输出： [2,1]
#
# 解释：
#
# queries[0] = [2, 5]：有效数对为 nums1[0] + nums2[1] = 1 + 4 = 5 和 nums1[1] + nums2[0] = 2 + 3 = 5。
# queries[1] = [1, 0, 0, 2]：将 nums2[0] 增加 2，得到 nums2 = [5, 4]。
# queries[2] = [2, 5]：有效数对为 nums1[0] + nums2[1] = 1 + 4 = 5。
# 因此，answer = [2, 1]。
# 示例 2：
#
# 输入： nums1 = [1,1], nums2 = [2,2,3], queries = [[2,4],[1,0,1,1],[2,4]]
#
# 输出： [2,6]
#
# 解释：
#
# queries[0] = [2, 4]：有效数对为 nums1[0] + nums2[2] = 1 + 3 和 nums1[1] + nums2[2] = 1 + 3。
# queries[1] = [1, 0, 1, 1]：将 nums2[0] 和 nums2[1] 各增加 1，得到 nums2 = [3, 3, 3]。
# queries[2] = [2, 4]：nums1 = [1, 1] 中的每个元素都可以与 nums2 = [3, 3, 3] 中的每个元素配对，因为 1 + 3 = 4，总共有 2 × 3 = 6 个数对。
# 因此，answer = [2, 6]。
# 示例 3：
#
# 输入： nums1 = [2,5,8,4], nums2 = [1,3,8], queries = [[2,9],[1,1,2,1],[2,10]]
#
# 输出： [1,0]
#
# 解释：
#
# queries[0] = [2, 9]：唯一有效数对为 nums1[2] + nums2[0] = 8 + 1 = 9。
# queries[1] = [1, 1, 2, 1]：将 nums2[1] 和 nums2[2] 各增加 1，得到 nums2 = [1, 4, 9]。
# queries[2] = [2, 10]：没有数对的和为 10。
# 因此，answer = [1, 0]。
#
#
# 提示：
#
# 1 <= nums1.length <= 5
# 1 <= nums2.length <= 5 * 104
# 1 <= nums1[i], nums2[i] <= 105
# 1 <= queries.length <= 5 * 104
# queries[i].length == 2 or 4
# queries[i] == [1, x, y, val]，或
# queries[i] == [2, tot]
# 0 <= x <= y < nums2.length
# 1 <= val <= 105
# 1 <= tot <= 109
# 保证每次查询后，nums2 中的每个元素不超过 2 * 109。

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def numberOfPairs1(self, nums1: list[int], nums2: list[int], queries: list[list[int]]) -> list[int]:
        n1, n2 = len(nums1), len(nums2)
        b = int(n2 ** 0.5)  # 分块大小
        m = (n2 + b - 1) // b  # 分块个数
        mc = [Counter() for _ in range(m)]  # m个分块上的counter
        ml = [0] * m  # m个分块上的lazy tag

        for i, x in enumerate(nums2):
            j = i // b
            mc[j][x] += 1

        ans = []
        for i in range(len(queries)):
            if queries[i][0] == 1:
                x, y, val = queries[i][1:]
                bx, by = x // b, y // b
                for v in range(x, MIN((bx + 1) * b, y + 1)):  # 第一个分块，单独处理
                    mc[bx][nums2[v]] -= 1
                    nums2[v] += val
                    mc[bx][nums2[v]] += 1
                for bi in range(bx + 1, by):
                    ml[bi] += val
                if bx != by:
                    for v in range(by * b, y + 1):  # 最后一个分块，单独处理
                        mc[by][nums2[v]] -= 1
                        nums2[v] += val
                        mc[by][nums2[v]] += 1
            else:
                tot = queries[i][1]
                res = 0
                for z in nums1:
                    for bi in range(m):
                        exp = tot - ml[bi] - z
                        res += mc[bi][exp]
                ans.append(res)
        return ans


    def numberOfPairs(self, nums1: list[int], nums2: list[int], queries: list[list[int]]) -> list[int]:
        # 优化了第一个分块和最后一个分块是否能整块处理
        n1, n2 = len(nums1), len(nums2)
        b = int(n2 ** 0.5)  # 分块大小
        m = (n2 + b - 1) // b  # 分块个数
        mc = [Counter() for _ in range(m)]  # m个分块上的counter
        ml = [0] * m  # m个分块上的lazy tag

        for i, x in enumerate(nums2):
            j = i // b
            mc[j][x] += 1

        ans = []
        for i in range(len(queries)):
            if queries[i][0] == 1:
                x, y, val = queries[i][1:]
                bx, by = x // b, y // b
                if bx * b != x or bx == by:
                    for v in range(x, MIN((bx + 1) * b, y + 1)):  # 第一个分块，单独处理
                        mc[bx][nums2[v]] -= 1
                        nums2[v] += val
                        mc[bx][nums2[v]] += 1
                if bx != by and by * b - 1 != y:
                    for v in range(by * b, y + 1):  # 最后一个分块，单独处理
                        mc[by][nums2[v]] -= 1
                        nums2[v] += val
                        mc[by][nums2[v]] += 1
                lower = bx if bx * b == x else bx + 1
                upper = by + 1 if by * b - 1 == y else by
                for bi in range(lower, upper):
                    ml[bi] += val

            else:
                tot = queries[i][1]
                res = 0
                for z in nums1:
                    for bi in range(m):
                        exp = tot - ml[bi] - z
                        res += mc[bi][exp]
                ans.append(res)
        return ans



so = Solution()
print(so.numberOfPairs(nums1 = [10], nums2 = [1,18,46,69,64,14,45,33,5,27,81,18,6,81,58,30,83,22,3,3,30,2,93,48,13,53,85,68,87,82,60,7,9,48,88,42,15,57,71,22,91,14,47,3,10,72,41], queries = [[1,13,14,99],[1,17,17,62],[2,93]]))
print(so.numberOfPairs(nums1 = [1], nums2 = [1,9,11,11,1,18,26,1,3,6,12,13,25], queries = [[2,21],[2,24],[1,12,12,13]]))
print(so.numberOfPairs(nums1 = [1,2], nums2 = [3,4], queries = [[2,5],[1,0,0,2],[2,5]]))




