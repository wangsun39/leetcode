# 给出基数为 -2 的两个数 arr1 和 arr2，返回两数相加的结果。
#
# 数字以 数组形式 给出：数组由若干 0 和 1 组成，按最高有效位到最低有效位的顺序排列。例如，arr = [1,1,0,1] 表示数字 (-2)^3 + (-2)^2 + (-2)^0 = -3。数组形式 中的数字 arr 也同样不含前导零：即 arr == [0] 或 arr[0] == 1。
#
# 返回相同表示形式的 arr1 和 arr2 相加的结果。两数的表示形式为：不含前导零、由若干 0 和 1 组成的数组。
#
#
#
# 示例 1：
#
# 输入：arr1 = [1,1,1,1,1], arr2 = [1,0,1]
# 输出：[1,0,0,0,0]
# 解释：arr1 表示 11，arr2 表示 5，输出表示 16 。
# 示例 2：
#
# 输入：arr1 = [0], arr2 = [0]
# 输出：[0]
# 示例 3：
#
# 输入：arr1 = [0], arr2 = [1]
# 输出：[1]
#
#
# 提示：
#
# 1 <= arr1.length, arr2.length <= 1000
# arr1[i] 和 arr2[i] 都是 0 或 1
# arr1 和 arr2 都没有前导0
from leetcode.allcode.competition.mypackage import *


class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1, arr2 = arr1[::-1], arr2[::-1]
        n1, n2 = len(arr1), len(arr2)
        n = max(n1, n2) + 2
        arr1 += [0] * (n - n1)
        arr2 += [0] * (n - n2)
        s = [0] * (max(n1, n2) + 2)
        i = 0
        for i in range(n):
            c = arr1[i] + arr2[i]
            if c <= 1:
                s[i] = c
                continue
            if arr1[i+1] == 1:
                arr1[i+1] = 0
                continue
            if arr2[i+1] == 1:
                arr2[i+1] = 0
                continue
            arr1[i+1] = 1
            if arr1[i + 2] == 0:
                arr1[i + 2] = 1
                continue
            if arr2[i + 2] == 0:
                arr2[i + 2] = 1
                continue
            s[i + 2] = 1

        if s[-1] == -1:
            s.pop()
            s.append(1)
            s.append(1)
        s = s[::-1]
        for i in range(len(s)):
            if s[i]:
                break
        if i == len(s):
            return [0]
        return s[i:]

so = Solution()
print(so.addNegabinary(arr1 = [1], arr2 = [1,0,1]))
print(so.addNegabinary(arr1 = [1], arr2 = [1]))
print(so.addNegabinary(arr1 = [1,1,1,1,1], arr2 = [1,0,1]))
print(so.addNegabinary(arr1 = [0], arr2 = [0]))
print(so.addNegabinary(arr1 = [0], arr2 = [1]))

