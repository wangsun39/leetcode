# 给定一个长度为偶数的整数数组 arr，只有对 arr 进行重组后可以满足 “对于每个 0 <= i < len(arr) / 2，都有 arr[2 * i + 1] = 2 * arr[2 * i]” 时，返回 true；否则，返回 false。
#
#  
#
# 示例 1：
#
# 输入：arr = [3,1,3,6]
# 输出：false
# 示例 2：
#
# 输入：arr = [2,1,2,6]
# 输出：false
# 示例 3：
#
# 输入：arr = [4,-2,2,-4]
# 输出：true
# 解释：可以用 [-2,-4] 和 [2,4] 这两组组成 [-2,-4,2,4] 或是 [2,4,-2,-4]
#  
#
# 提示：
#
# 0 <= arr.length <= 3 * 104
# arr.length 是偶数
# -105 <= arr[i] <= 105


from typing import List
import bisect
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr1, arr2 = [], []
        for e in arr:
            if e >= 0:
                arr1.append(e)
            else:
                arr2.append(-e)
        def judge(array):
            if len(array) % 2 == 1:
                return False
            array.sort()
            print(array)
            while len(array) > 0:
                pos = bisect.bisect_left(array, array[0] * 2)
                if pos >= len(array) or array[pos] != array[0] * 2:
                    return False
                del(array[pos])
                del(array[0])
            return True
        res = judge(arr1)
        # arr2 = -arr2
        return res and judge(arr2)



so = Solution()
print(so.canReorderDoubled([-33, 0]))
print(so.canReorderDoubled([-5, -3]))
print(so.canReorderDoubled([3,1,3,6]))
print(so.canReorderDoubled([2,1,2,6]))
print(so.canReorderDoubled([4,-2,2,-4]))

