

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        horizontalCut = deque(horizontalCut)
        verticalCut = deque(verticalCut)
        rseg = cseg = 1 # 剩余的每行有多少段，每列有多少段
        ans = 0
        while horizontalCut and verticalCut:
            if horizontalCut[0] > verticalCut[0]:
                ans += horizontalCut[0] * rseg
                horizontalCut.popleft()
                cseg += 1
            else:
                ans += verticalCut[0] * cseg
                verticalCut.popleft()
                rseg += 1
        if horizontalCut:
            ans += sum(horizontalCut) * rseg
        else:
            ans += sum(verticalCut) * cseg
        return ans


so = Solution()
print(so.minimumCost(7,4,[13,6,12,14,4,7],[14,15,11]))
print(so.minimumCost(6,3,[2,3,2,3,1],[1,2]))
print(so.minimumCost(m = 3, n = 2, horizontalCut = [1,3], verticalCut = [5]))
print(so.minimumCost(m = 2, n = 2, horizontalCut = [7], verticalCut = [4]))




