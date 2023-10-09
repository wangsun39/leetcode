import copy
from collections import deque
from typing import List


class Solution:
    def minKBitFlips1(self, A, K: int):
        def reverse(AA, pos):
            i = pos
            while i < pos + K:
                AA[i] = 1 - AA[i]
                i += 1
        def recur_find(AA):
            if len(AA) <= K or 0 not in AA:
                if 0 in AA and 1 in AA:
                    return -1
                return 1 if 0 == AA[0] else 0
            pos = AA.index(0)
            if pos + K > len(AA):
                return -1
            reverse(AA, pos)
            res = recur_find(AA[pos:])
            if -1 == res:
                return -1
            return res + 1
        return recur_find(A)

    def minKBitFlips2(self, A, K: int):
        N = len(A)
        flip = [0] * N
        i = 0
        res = 0
        target = 0
        while i < N:
            if 1 == flip[i]:
                target = 1 - target  # target = target ^ flip[i]
            if i + K > N and A[i] == target:
                return -1
            if target == A[i]:
                target = 1 - target
                if i + K < N:
                    flip[i+K] = 1
                res += 1
            i += 1
        return res


    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        dq = deque()  # 记录翻转的起点
        for i, x in enumerate(nums):
            while dq and dq[0] + k - 1 < i:
                dq.popleft()
            if (len(dq) & 1) ^ x:  # len(dq) & 1 表示 x 翻转的次数的奇偶性
                continue
            if i > n - k:
                return -1
            dq.append(i)
            ans += 1

        return ans



so = Solution()
print(so.minKBitFlips([0,0,0,1,0,1,1,0], 3))
print(so.minKBitFlips([0,1,0], 1))
print(so.minKBitFlips([1,1,0], 2))
print(so.minKBitFlips([1,1,1], 2))
print(so.minKBitFlips([1,1,0,0,1,0,1], 4))

