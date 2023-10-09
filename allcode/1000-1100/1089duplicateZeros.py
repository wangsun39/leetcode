# 给你一个长度固定的整数数组 arr，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。
#
# 注意：请不要在超过该数组长度的位置写入元素。
#
# 要求：请对输入的数组 就地 进行上述修改，不要从函数返回任何东西。
#
#  
#
# 示例 1：
#
# 输入：[1,0,2,3,0,4,5,0]
# 输出：null
# 解释：调用函数后，输入的数组将被修改为：[1,0,0,2,3,0,0,4]
# 示例 2：
#
# 输入：[1,2,3]
# 输出：null
# 解释：调用函数后，输入的数组将被修改为：[1,2,3]
#  
#
# 提示：
#
# 1 <= arr.length <= 10000
# 0 <= arr[i] <= 9

from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        count0 = 0
        n = len(arr)
        last0 = False
        for i, e in enumerate(arr):
            if i + count0 >= n - 1:
                break
            if e == 0:
                count0 += 1
                if i + count0 >= n - 1:
                    last0 = True
                    break
        if last0:
            i = n - count0 - 1
            j = n - 1
        else:
            arr[n - 1] = arr[n - count0 - 1]
            i = n - count0 - 2
            j = n - 2
        while i < j:
            if arr[i] == 0:
                arr[j] = 0
                j -= 1
            arr[j] = arr[i]
            j -= 1
            i -= 1
        print(arr)



obj = Solution()
print(obj.duplicateZeros([1,0,2,3,0,4,5,0]))

