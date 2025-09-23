# 给定一个32位整数 num，你可以将一个数位从0变为1。请编写一个程序，找出你能够获得的最长的一串1的长度。
#
# 示例 1：
#
# 输入: num = 1775(110111011112)
# 输出: 8
# 示例 2：
#
# 输入: num = 7(01112)
# 输出: 4


from typing import List

class Solution:
    def reverseBits(self, num: int) -> int:
        arr = []
        for i in range(32):
            if num & (1 << i): arr.append(1)
            else: arr.append(0)
        right = [32] * 32
        for i in range(30, -1, -1):
            if arr[i + 1] == 0: right[i] = i + 1
            else: right[i] = right[i + 1]
        left = [-1] * 32
        ans = right[0]
        for i in range(1, 32):
            if arr[i - 1] == 0:
                left[i] = i - 1
            else:
                left[i] = left[i - 1]
            ans = max(ans, right[i] - left[i] - 1)
        return ans



so = Solution()
print(so.reverseBits(-4))
print(so.reverseBits(-2))






