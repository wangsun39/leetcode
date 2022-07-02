# 给你一个整数数组 queries 和一个 正 整数 intLength ，请你返回一个数组 answer ，其中 answer[i] 是长度为 intLength 的 正回文数 中第 queries[i] 小的数字，如果不存在这样的回文数，则为 -1 。
#
# 回文数 指的是从前往后和从后往前读一模一样的数字。回文数不能有前导 0 。
#
#  
#
# 示例 1：
#
# 输入：queries = [1,2,3,4,5,90], intLength = 3
# 输出：[101,111,121,131,141,999]
# 解释：
# 长度为 3 的最小回文数依次是：
# 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, ...
# 第 90 个长度为 3 的回文数是 999 。
# 示例 2：
#
# 输入：queries = [2,4,6], intLength = 4
# 输出：[1111,1331,1551]
# 解释：
# 长度为 4 的前 6 个回文数是：
# 1001, 1111, 1221, 1331, 1441 和 1551 。
#  
#
# 提示：
#
# 1 <= queries.length <= 5 * 104
# 1 <= queries[i] <= 109
# 1 <= intLength <= 15




from typing import List
from collections import deque
# Definition for a binary tree node.
from collections import Counter
class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        # if intLength <= 1:
        #     return queries
        even = True if intLength % 2 == 0 else False
        half = intLength // 2 if even else intLength // 2 + 1
        firstHalf = '1' + ('0' * (half - 1))
        def find(idx):
            idx -= 1
            # if len(str(idx)) > half:
            #     return -1
            s = str(int(firstHalf) + idx)
            if len(s) > half:
                return -1
            if even:
                res = s + s[::-1]
            else:
                res = s[:-1] + s[-1] + s[:-1][::-1]
            return int(res)
        res = []
        for i in range(len(queries)):
            res.append(find(queries[i]))
        return res

so = Solution()
print(so.kthPalindrome([2,9,7,6], intLength = 1))
print(so.kthPalindrome([2,201429812,8,520498110,492711727,339882032,462074369,9,7,6], intLength = 1))
print(so.kthPalindrome([1,100,3,4,5,90], intLength = 3))
print(so.kthPalindrome([1,2,3,4,5,90], intLength = 3))
print(so.kthPalindrome([2,4,6], intLength = 4))

