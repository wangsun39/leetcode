# 给你一个整数数组 nums （下标 从 0 开始 计数）以及两个整数：low 和 high ，请返回 漂亮数对 的数目。
#
# 漂亮数对 是一个形如 (i, j) 的数对，其中 0 <= i < j < nums.length 且 low <= (nums[i] XOR nums[j]) <= high 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,4,2,7], low = 2, high = 6
# 输出：6
# 解释：所有漂亮数对 (i, j) 列出如下：
#     - (0, 1): nums[0] XOR nums[1] = 5
#     - (0, 2): nums[0] XOR nums[2] = 3
#     - (0, 3): nums[0] XOR nums[3] = 6
#     - (1, 2): nums[1] XOR nums[2] = 6
#     - (1, 3): nums[1] XOR nums[3] = 3
#     - (2, 3): nums[2] XOR nums[3] = 5
# 示例 2：
#
# 输入：nums = [9,8,4,2,1], low = 5, high = 14
# 输出：8
# 解释：所有漂亮数对 (i, j) 列出如下：
#     - (0, 2): nums[0] XOR nums[2] = 13
#     - (0, 3): nums[0] XOR nums[3] = 11
#     - (0, 4): nums[0] XOR nums[4] = 8
#     - (1, 2): nums[1] XOR nums[2] = 12
#     - (1, 3): nums[1] XOR nums[3] = 10
#     - (1, 4): nums[1] XOR nums[4] = 9
#     - (2, 3): nums[2] XOR nums[3] = 6
#     - (2, 4): nums[2] XOR nums[4] = 5
#
#
# 提示：
#
# 1 <= nums.length <= 2 * 104
# 1 <= nums[i] <= 2 * 104
# 1 <= low <= high <= 2 * 104


from typing import List
import heapq

# class Node:
#     def __init__(self):
#         self.children = [None, None]
#         self

class Trie:

    def __init__(self):
        self.root = [0, {}]

    def insert(self, word: str) -> None:
        # print(word)
        cur = self.root
        for e in word:
            if e not in cur[1]:
                cur[1][e] = [1, {}]
            else:
                cur[1][e][0] += 1
            cur = cur[1][e]

    def startsWith(self, prefix: str) -> int:
        cur = self.root
        for e in prefix:
            if e in cur[1]:
                cur = cur[1][e]
            else:
                return 0
        return cur[0]

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        def trans(x):
            x = bin(x)[2:]
            l = len(x)
            return '0' * (15 - l) + x
        low, high = trans(low - 1), trans(high)
        for i, x in enumerate(nums):
            nums[i] = trans(x)

        def f(x, y):  # Trie 树上与x异或的结果 <= y的元素个数
            ans = 0
            xx = ''
            for i, e in enumerate(y):
                if e == '0':
                    xx += x[i]
                    continue
                ans += tr.startsWith(xx + x[i])  # 保持最后一位为0
                xx += '0' if x[i] == '1' else '1'
            ans += tr.startsWith(xx)
            print(x, y, ans)
            return ans

        mi, mx = 0, 0
        tr = Trie()
        # for num in nums:  注释放开是另一种写法， 总数要除以2
        #     tr.insert(num)
        # for i in range(len(nums)):
        for i in range(1, len(nums)):
            tr.insert(nums[i - 1])
            mx += f(nums[i], high)
            mi += f(nums[i], low)
        print(mi, mx)
        # return (mx - mi) // 2
        return mx - mi

so = Solution()

print(so.countPairs(nums = [3856,3174,2182,7497,6155,4589,3581,4548,3982,2508], low = 6903, high = 6946))  # 0
print(so.countPairs(nums = [9,8,4,2,1], low = 5, high = 14))  # 8
print(so.countPairs(nums = [1,4,2,7], low = 2, high = 6))  # 6




