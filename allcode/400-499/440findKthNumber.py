# 给定整数n和k，返回[1, n]中字典序第k小的数字。
#
#
#
# 示例 1:
#
# 输入: n = 13, k = 2
# 输出: 10
# 解释: 字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。
# 示例 2:
#
# 输入: n = 1, k = 1
# 输出: 1
#
#
# 提示:
#
# 1 <= k <= n <= 109


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        def helper(s, k):
            for i in range(10):
                if int(s) * 10 + i <= n:
                    helper(s + str(i), k - 1)
                    break
        s = str(n)
        N = len(s)
        s1 = 1
        s2 = 0
        s3 = []
        for i in range(N):
            s1 = '1' * (N - i)
            s3.append(int(s1) * int(s[i]))
        print(s3)
        print(s2)


so = Solution()
print(so.findKthNumber(121,1))
#print(so.diffWaysToCompute("2*3-4*5"))

