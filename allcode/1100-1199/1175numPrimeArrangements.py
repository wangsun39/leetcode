# 请你帮忙给从 1 到 n的数设计排列方案，使得所有的「质数」都应该被放在「质数索引」（索引从 1 开始）上；你需要返回可能的方案总数。
#
# 让我们一起来回顾一下「质数」：质数一定是大于 1 的，并且不能用两个小于它的正整数的乘积来表示。
#
# 由于答案可能会很大，所以请你返回答案 模 mod10^9 + 7之后的结果即可。
#
#
#
# 示例 1：
#
# 输入：n = 5
# 输出：12
# 解释：举个例子，[1,2,5,4,3] 是一个有效的排列，但 [5,2,3,4,1] 不是，因为在第二种情况里质数 5 被错误地放在索引为 1 的位置上。
# 示例 2：
#
# 输入：n = 100
# 输出：682289015
#
#
# 提示：
#
# 1 <= n <= 100


from typing import List
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        N = int(1e9 + 7)
        prime = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
        num = 0
        for i in range(1, n + 1):
            if i in prime:
                num += 1
        def factorial(k):
            ans = 1
            for i in range(2, k + 1):
                ans = ((ans * i) % N)
            return ans
        return (factorial(num) * factorial(n - num)) % N


obj = Solution()
#print(obj.kConcatenationMaxSum([1,-2], 3))


