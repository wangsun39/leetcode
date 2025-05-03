# 给定一个整数数组，编写一个函数，找出索引m和n，只要将索引区间[m,n]的元素排好序，整个数组就是有序的。注意：n-m尽量最小，也就是说，找出符合条件的最短序列。函数返回值为[m,n]，若不存在这样的m和n（例如整个数组是有序的），请返回[-1,-1]。
#
# 示例：
#
# 输入： [1,2,4,7,10,11,7,12,6,7,16,18,19]
# 输出： [3,9]
# 提示：
#
# 0 <= len(array) <= 1000000

from leetcode.allcode.competition.mypackage import *

class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        n = len(array)
        mx = -inf
        left = right = -1
        for i, x in enumerate(array):
            if x < mx:
                right = i
            else:
                mx = x
        mn = inf
        for i in range(n - 1, -1, -1):
            x = array[i]
            if x > mn:
                left = i
            else:
                mn = x
        return [left, right]

so = Solution()
print(so.subSort([1,2,4,7,10,11]))
print(so.subSort([1,2,4,7,10,11,7,12,6,7,16,18,19]))





