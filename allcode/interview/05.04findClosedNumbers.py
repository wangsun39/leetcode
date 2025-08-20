# 下一个数。给定一个正整数，找出与其二进制表达式中1的个数相同且大小最接近的那两个数（一个略大，一个略小）。
#
# 示例 1：
#
#  输入：num = 2（或者0b10）
#  输出：[4, 1] 或者（[0b100, 0b1]）
# 示例 2：
#
#  输入：num = 1
#  输出：[2, -1]
# 提示：
#
# num 的范围在[1, 2147483647]之间；
# 如果找不到前一个或者后一个满足条件的正数，那么输出 -1。


from typing import List

class Solution:
    def findClosedNumbers(self, num: int) -> List[int]:
        s = bin(num)[2:]
        n = len(s)
        if num == 2147483647: return [-1, -1]

        def pre(arr):  # 前一个小的数
            if arr[-1] == '0':
                for i in range(n - 1, -1, -1):
                    if arr[i] == '0': continue
                    arr[i] = '0'
                    arr[i + 1] = '1'
                    return arr
            l = r = -1
            for i in range(n - 1, -1, -1):
                if r == -1:
                    if arr[i] == '1':
                        r = i
                        arr[i] = '0'
                else:
                    if arr[i] == '0':
                        l = i
                        break
                    else:
                        arr[i] = '0'
            for i in range(l, -1, -1):
                if arr[i] == '1':
                    ll = i
                    arr[i] = '0'
                    break
            for i in range(r - l + 1):
                arr[ll + 1 + i] = '1'
            return arr

        def after(arr):   # 后一个大到数
            arr.insert(0, '0')
            m = len(arr)
            l = r = -1
            for i in range(m - 1, -1, -1):
                if r == -1:
                    if arr[i] == '1':
                        r = i
                        arr[i] = '0'
                else:
                    if arr[i] == '0':
                        l = i
                        break
                    else:
                        arr[i] = '0'
            arr[l] = '1'
            for i in range(r - l - 1):
                arr[m - 1 - i] = '1'
            return arr

        if s.count('10') == 1 and s.count('01') == 0 and n == 31:
            # last = (num & -num).bit_length() - 1
            arr = pre(list(s))
            return [-1, int(''.join(arr), 2)]
        if '0' not in s:
            arr2 = after(list(s))
            return [int(''.join(arr2), 2), -1]

        arr1 = pre(list(s))
        arr2 = after(list(s))
        return [int(''.join(arr2), 2), int(''.join(arr1), 2)]


so = Solution()
print(so.findClosedNumbers(67))
print(so.findClosedNumbers(2))


