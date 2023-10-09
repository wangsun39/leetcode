# 如果序列 X_1, X_2, ..., X_n 满足下列条件，就说它是 斐波那契式 的：
#
# n >= 3
# 对于所有 i + 2 <= n，都有 X_i + X_{i+1} = X_{i+2}
# 给定一个严格递增的正整数数组形成序列 arr ，找到 arr 中最长的斐波那契式的子序列的长度。如果一个不存在，返回  0 。
#
# （回想一下，子序列是从原序列 arr 中派生出来的，它从 arr 中删掉任意数量的元素（也可以不删），而不改变其余元素的顺序。例如， [3, 5, 8] 是 [3, 4, 5, 6, 7, 8] 的一个子序列）
#
#  
#
# 示例 1：
#
# 输入: arr = [1,2,3,4,5,6,7,8]
# 输出: 5
# 解释: 最长的斐波那契式子序列为 [1,2,3,5,8] 。
# 示例 2：
#
# 输入: arr = [1,3,7,11,12,14,18]
# 输出: 3
# 解释: 最长的斐波那契式子序列有 [1,11,12]、[3,11,14] 以及 [7,11,18] 。
#  
#
# 提示：
#
# 3 <= arr.length <= 1000
# 1 <= arr[i] < arr[i + 1] <= 10^9


from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        s = set(arr)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                cur = 2
                x0, x1 = arr[i], arr[j]
                while x0 + x1 in s:
                    cur += 1
                    x0, x1 = x1, x0 + x1
                ans = max(ans, cur)
        return 0 if ans < 3 else ans


so = Solution()
print(so.lenLongestFibSubseq([1,2,3,4,5,6,7,8]))
print(so.lenLongestFibSubseq([1,3,7,11,12,14,18]))


