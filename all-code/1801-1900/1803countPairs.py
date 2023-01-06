# 给你三个正整数 n、index 和 maxSum 。你需要构造一个同时满足下述所有条件的数组 nums（下标 从 0 开始 计数）：
#
# nums.length == n
# nums[i] 是 正整数 ，其中 0 <= i < n
# abs(nums[i] - nums[i+1]) <= 1 ，其中 0 <= i < n-1
# nums 中所有元素之和不超过 maxSum
# nums[index] 的值被 最大化
# 返回你所构造的数组中的 nums[index] 。
#
# 注意：abs(x) 等于 x 的前提是 x >= 0 ；否则，abs(x) 等于 -x 。
#
#
#
# 示例 1：
#
# 输入：n = 4, index = 2,  maxSum = 6
# 输出：2
# 解释：数组 [1,1,2,1] 和 [1,2,2,1] 满足所有条件。不存在其他在指定下标处具有更大值的有效数组。
# 示例 2：
#
# 输入：n = 6, index = 1,  maxSum = 10
# 输出：3
#
#
# 提示：
#
# 1 <= n <= maxSum <= 109
# 0 <= index < n


from typing import List
import heapq


class Trie:

    def __init__(self):
        self.root = [0, {}]

    def insert(self, word: str) -> None:
        print(word)
        cur = self.root
        for e in word:
            if e not in cur[1]:
                cur[1][e] = [0, {}]
            cur[0] += 1
            cur = cur[1][e]

    def startsWith(self, prefix: str) -> int:
        cur = self.root
        for e in prefix:
            if e in cur[1]:
                cur = cur[1][e]
            else:
                return 0
        return cur[0] + 1

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        def trans(x):
            x = bin(x)[2:]
            l = len(x)
            return '0' * (15 - l) + x
        low, high = trans(low - 1), trans(high)
        for i, x in enumerate(nums):
            nums[i] = trans(x)
        tr = Trie()
        for num in nums:
            tr.insert(num)
        # print(tr.root)
        def f(x, y):  # Trie 树上与x异或的结果 <= y的元素个数
            ans = 0
            xx = ''
            for i, e in enumerate(y):
                if e == '0':
                    xx += x[i]
                    continue
                ans += tr.startsWith(xx + x[i])  # 保持最后一位为0
                xx += '0' if e == '1' else '1'
            print(x, y, ans)
            return ans

        mi, mx = 0, 0
        for num in nums:
            mx += f(num, high)
            mi += f(num, low)
        return (mx - mi) // 2


so = Solution()

print(so.countPairs(nums = [1,4,2,7], low = 2, high = 6))  #




