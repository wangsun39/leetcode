# 给定一个长度为 n 的整数数组 nums ，其中 nums 是范围为 [1，n] 的整数的排列。还提供了一个 2D 整数数组 sequences ，其中 sequences[i] 是 nums 的子序列。
# 检查 nums 是否是唯一的最短 超序列 。最短 超序列 是 长度最短 的序列，并且所有序列 sequences[i] 都是它的子序列。对于给定的数组 sequences ，可能存在多个有效的 超序列 。
#
# 例如，对于 sequences = [[1,2],[1,3]] ，有两个最短的 超序列 ，[1,2,3] 和 [1,3,2] 。
# 而对于 sequences = [[1,2],[1,3],[1,2,3]] ，唯一可能的最短 超序列 是 [1,2,3] 。[1,2,3,4] 是可能的超序列，但不是最短的。
# 如果 nums 是序列的唯一最短 超序列 ，则返回 true ，否则返回 false 。
# 子序列 是一个可以通过从另一个序列中删除一些元素或不删除任何元素，而不改变其余元素的顺序的序列。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,2,3], sequences = [[1,2],[1,3]]
# 输出：false
# 解释：有两种可能的超序列：[1,2,3]和[1,3,2]。
# 序列 [1,2] 是[1,2,3]和[1,3,2]的子序列。
# 序列 [1,3] 是[1,2,3]和[1,3,2]的子序列。
# 因为 nums 不是唯一最短的超序列，所以返回false。
# 示例 2：
#
# 输入：nums = [1,2,3], sequences = [[1,2]]
# 输出：false
# 解释：最短可能的超序列为 [1,2]。
# 序列 [1,2] 是它的子序列：[1,2]。
# 因为 nums 不是最短的超序列，所以返回false。
# 示例 3：
#
# 输入：nums = [1,2,3], sequences = [[1,2],[1,3],[2,3]]
# 输出：true
# 解释：最短可能的超序列为[1,2,3]。
# 序列 [1,2] 是它的一个子序列：[1,2,3]。
# 序列 [1,3] 是它的一个子序列：[1,2,3]。
# 序列 [2,3] 是它的一个子序列：[1,2,3]。
# 因为 nums 是唯一最短的超序列，所以返回true。
#  
#
# 提示：
#
# n == nums.length
# 1 <= n <= 104
# nums 是 [1, n] 范围内所有整数的排列
# 1 <= sequences.length <= 104
# 1 <= sequences[i].length <= 104
# 1 <= sum(sequences[i].length) <= 105
# 1 <= sequences[i][j] <= n
# sequences 的所有数组都是 唯一 的
# sequences[i] 是 nums 的一个子序列




from leetcode.allcode.competition.mypackage import *


class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        n = len(nums)

        d = {nums[i]: i + 1 for i in range(n)}
        seq = [[0 for _ in range(len(sequences[i]))] for i in range(len(sequences))]
        for i in range(len(sequences)):
            for j in range(len(sequences[i])):
                seq[i][j] = d[sequences[i][j]]
        def find(x, y):
            m = len(seq)
            for i in range(m):
                pos = bisect.bisect_left(seq[i], x)
                if pos + 1 < len(seq[i]) and seq[i][pos] == x and seq[i][pos + 1] == y:
                    return True
            return False
        nu = [i + 1 for i in range(n)]
        for i in range(n - 1):
            if not find(nu[i], nu[i + 1]):
                return False
        return True

    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        # 2023/1/15 拓扑排序模板法
        def buildTopo(conditions, n):
            tree = defaultdict(set)
            preNum = [0] * n
            for x, y in conditions:
                if y - 1 not in tree[x - 1]:
                    tree[x - 1].add(y - 1)
                    preNum[y - 1] += 1
            queue = []
            for i in range(n):
                if preNum[i] == 0:
                    queue.append(i)
            ans = []
            while len(queue) == 1:   # 这里把模板稍作修改
                q = queue.pop(0)
                ans.append(q)
                for x in tree[q]:
                    preNum[x] -= 1
                    if preNum[x] == 0:
                        queue.append(x)
            if len(ans) != n:
                return []  # 存在圈
            return ans

        seqs = []
        for seq in sequences:
            for i in range(1, len(seq)):
                seqs.append([seq[i - 1], seq[i]])
        new = buildTopo(seqs, len(nums))
        if len(new) < len(nums): return False

        print(new)
        return True





so = Solution()
print(so.sequenceReconstruction([5,4,8,9,1,6,3,2,7,10], [[8,9,1],[6,3,2,7,10],[5,4]]))
print(so.sequenceReconstruction([1,2,3,4,5], [[1,2,3,4,5],[1,2,3,4],[1,2,3],[1],[4],[5]]))
print(so.sequenceReconstruction(nums = [4,1,5,2,6,3], sequences = [[5,2,6,3],[4,1,5,2]]))
print(so.sequenceReconstruction(nums = [1,2,3], sequences = [[1,2],[1,3],[2,3]]))
print(so.sequenceReconstruction(nums = [1,2,3], sequences = [[1,2],[1,3]]))
print(so.sequenceReconstruction(nums = [1,2,3], sequences = [[1,2]]))




