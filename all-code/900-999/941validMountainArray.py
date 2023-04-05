from typing import List
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        if A[1] <= A[0]:
            return False
        isIncrease = True
        cur = A[1]
        for a in A[2:]:
            if a > cur:
                if not isIncrease:
                    return False
            elif a < cur:
                if isIncrease:
                    isIncrease = False
            else:
                return False
            cur = a
        return not isIncrease

so = Solution()
print(so.validMountainArray([1, 3, 2]))
print(so.validMountainArray([3, 5, 5]))
print(so.validMountainArray([0, 3, 2, 1]))
'''so.knightDialer(3)
so.knightDialer(4)
so.knightDialer(5)'''
