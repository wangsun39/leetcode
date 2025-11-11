# 给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。
#
# 初始化 A 和 B 的元素数量分别为 m 和 n。
#
# 示例：
#
# 输入：
# A = [1,2,3,0,0,0], m = 3
# B = [2,5,6],       n = 3
#
# 输出： [1,2,2,3,5,6]
# 说明：
#
# A.length == n + m

from leetcode.allcode.competition.mypackage import *

class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        i1, i2 = m - 1, n - 1
        for i in range(n + m - 1, -1, -1):
            if i1 >= 0 and i2 >= 0:
                if A[i1] < B[i2]:
                    A[i] = B[i2]
                    i2 -= 1
                else:
                    A[i] = A[i1]
                    i1 -= 1
            elif i1 >= 0:
                A[i] = A[i1]
                i1 -= 1
            else:
                A[i] = B[i2]
                i2 -= 1




so = Solution()





