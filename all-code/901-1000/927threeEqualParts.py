# 给定一个由 0 和 1 组成的数组 arr ，将数组分成  3 个非空的部分 ，使得所有这些部分表示相同的二进制值。

# 如果可以做到，请返回任何 [i, j]，其中 i+1 < j，这样一来：
#
# arr[0], arr[1], ..., arr[i] 为第一部分；
# arr[i + 1], arr[i + 2], ..., arr[j - 1] 为第二部分；
# arr[j], arr[j + 1], ..., arr[arr.length - 1] 为第三部分。
# 这三个部分所表示的二进制值相等。
# 如果无法做到，就返回 [-1, -1]。
#
# 注意，在考虑每个部分所表示的二进制时，应当将其看作一个整体。例如，[1,1,0] 表示十进制中的 6，而不会是 3。此外，前导零也是被允许的，所以 [0,1,1] 和 [1,1] 表示相同的值。
#
#  
#
# 示例 1：
#
# 输入：arr = [1,0,1,0,1]
# 输出：[0,3]
# 示例 2：
#
# 输入：arr = [1,1,0,1,1]
# 输出：[-1,-1]
# 示例 3:
#
# 输入：arr = [1,1,0,0,1]
# 输出：[0,2]
#  
#
# 提示：
#
# 3 <= arr.length <= 3 * 104
# arr[i] 是 0 或 1
#
# https://leetcode.cn/problems/three-equal-parts

from typing import List

class Solution:
    def threeEqualParts1(self, A: List[int]) -> List[int]:
        count = 0
        oneIdx = []
        print(A)
        # 把1三等分
        for i in range(len(A)):
            if 1 == A[i]:
                count += 1
                oneIdx.append(i)
        if 0 != count % 3:
            return [-1, -1]
        if 0 == count:
            if len(A) < 3:
                return [-1, -1]
            else:
                return [0, 2]
        count_13 = count // 3
        len1_min = 1 if 1 == count_13 else len(A[oneIdx[0]:oneIdx[count_13-1]+1])
        len1_max = len(A[oneIdx[0]:oneIdx[count_13]])
        len2_min = 1 if 1 == count_13 else len(A[oneIdx[count_13]:oneIdx[count_13*2-1]+1])
        len2_max = len(A[oneIdx[0]:oneIdx[count_13]])
        #len2 = len(A[oneIdx[count_13]:oneIdx[count_13*2]])
        len3 = len(A[oneIdx[count_13*2]:])
        if len1_max < len3 or len1_min > len3 or len2_max < len3 or len2_min > len3:
            return [-1, -1]
        A1 = A[oneIdx[0]:oneIdx[0]+len3]
        A2 = A[oneIdx[count_13]:oneIdx[count_13]+len3]
        A3 = A[oneIdx[count_13*2]:]
        if A1 == A2 and A2 == A3:
            return [oneIdx[0]+len3-1, oneIdx[count_13]+len3]
        return [-1, -1]
    def threeEqualParts(self, A: List[int]) -> List[int]:
        A = [str(e) for e in A]
        A = ''.join(A)
        numOfOne = A.count('1')
        if numOfOne % 3 > 0: return [-1, -1]
        each = numOfOne // 3
        if each == 0: return [0, 2]
        n = len(A)
        cnt = 0
        p = [-1, -1, -1]
        for i in range(n - 1, -1, -1):
            if A[i] == '1':
                cnt += 1
                if cnt % each == 0:
                    p.insert(0, i)

        s1, s2, s3 = A[p[0]:], A[p[1]:], A[p[2]:]
        l3 = len(s3)  # 不带前导零的s3长度
        if s1.startswith(s3) and s2.startswith(s3):
            j = p[1] + l3
            i = p[0] + l3 - 1
            return [i, j]
        return [-1, -1]


so = Solution()
print(so.threeEqualParts([1,0,1,0,1]))  # [0, 3]
print(so.threeEqualParts([1,1,0,1,1]))  # [-1, -1]
print(so.threeEqualParts([1,1,0,0,1]))  # [0, 2]
